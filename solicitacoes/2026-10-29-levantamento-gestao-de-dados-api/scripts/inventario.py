"""Somente consultas gcloud. Não lê payloads de secrets nem dados de negócio."""
import concurrent.futures as cf
import datetime
import json
import pathlib
import subprocess
import sys
import threading

ROOT = pathlib.Path(__file__).resolve().parents[1]
EVID = ROOT / 'evidencias'
LOCK = threading.Lock()
SAFE_ENV = {'NODE_ENV','PORT','GOOGLE_CLOUD_PROJECT','FIRESTORE_DATABASE_ID',
            'STORAGE_BUCKET','FRONTEND_ORIGIN','NEOGOV_AUTH_BASE_URL',
            'NEOGOV_AUTH_ALLOWED_ISSUERS','NEOGOV_AUTH_TIMEOUT_MS',
            'AUTH_COOKIE_SECURE','AUTH_COOKIE_SAME_SITE','FIRESTORE_EMULATOR_HOST'}

def sanitize(x):
    if isinstance(x, list):
        return [sanitize(v) for v in x]
    if isinstance(x, dict):
        out = {}
        for k,v in x.items():
            if k == 'env' and isinstance(v,list):
                out[k]=[{**e, **({'value':'[SEGREDO OMITIDO]'} if 'value' in e and e.get('name') not in SAFE_ENV else {})} for e in v]
            elif k in ('last-applied-configuration','kubectl.kubernetes.io/last-applied-configuration'):
                out[k]='[OMITIDO: configuração duplicada]'
            elif k in ('command','args'):
                out[k]='[OMITIDO: pode conter dados sensíveis]'
            else:
                out[k]=sanitize(v)
        return out
    return x

def query(key,args):
    cmd=['gcloud',*args,'--format=json']
    now=datetime.datetime.now(datetime.timezone.utc).isoformat()
    try:
        r=subprocess.run(cmd,stdin=subprocess.DEVNULL,capture_output=True,text=True,timeout=100)
        result={'command':cmd,'timestamp_utc':now,'exit_code':r.returncode}
        if r.returncode==0:
            result['data']=sanitize(json.loads(r.stdout or 'null'))
        else:
            result['error']=r.stderr[-7000:]
    except Exception as e:
        result={'command':cmd,'timestamp_utc':now,'exit_code':-1,'error':str(e)}
    (EVID/(key+'.json')).write_text(json.dumps(result,ensure_ascii=False,indent=2))
    with LOCK:
        with (ROOT/'comandos.jsonl').open('a') as f:
            f.write(json.dumps({'key':key,**{k:v for k,v in result.items() if k!='data'}},ensure_ascii=False)+'\n')
    return result

def phase1():
    p=query('projetos-visiveis',['projects','list'])
    if p['exit_code']: return
    projects=[x for x in p['data'] if 'lgpdweb' in (x['projectId']+' '+x['name']).lower()]
    (EVID/'projetos-lgpdweb.json').write_text(json.dumps(projects,ensure_ascii=False,indent=2))
    def scan(p):
        pid=p['projectId']
        r=query(pid+'--run-list',['run','services','list','--platform=managed','--project='+pid])
        services=r.get('data') or []
        target=[s for s in services if s.get('metadata',{}).get('name')=='gestao-de-dados-api']
        print(pid,r['exit_code'],[(s['metadata']['name'],s['metadata'].get('labels',{}).get('cloud.googleapis.com/location')) for s in target],flush=True)
        return {'project':p,'exit_code':r['exit_code'],'targets':target}
    with cf.ThreadPoolExecutor(max_workers=4) as pool:
        out=list(pool.map(scan,projects))
    (EVID/'descoberta.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))

def phase2():
    discovery=json.loads((EVID/'descoberta.json').read_text())
    tasks=[]
    for item in discovery:
        pid=item['project']['projectId']
        if item['exit_code']:
            tasks.append((pid+'--apis-enabled',['services','list','--enabled','--project='+pid]))
        if not item['targets']: continue
        tasks.extend([
          (pid+'--project-iam',['projects','get-iam-policy',pid]),
          (pid+'--billing',['billing','projects','describe',pid]),
          (pid+'--databases',['firestore','databases','list','--project='+pid]),
          (pid+'--buckets',['storage','buckets','list','--project='+pid]),
          (pid+'--secrets',['secrets','list','--project='+pid]),
          (pid+'--neg',['compute','network-endpoint-groups','list','--project='+pid]),
          (pid+'--backends',['compute','backend-services','list','--project='+pid]),
          (pid+'--urlmaps',['compute','url-maps','list','--project='+pid]),
          (pid+'--forwarding',['compute','forwarding-rules','list','--project='+pid]),
          (pid+'--log-sinks',['logging','sinks','list','--project='+pid]),
        ])
        for s in item['targets']:
            region=s['metadata']['labels']['cloud.googleapis.com/location']
            name=s['metadata']['name']
            spec=s['spec']['template']['spec']
            sa=spec.get('serviceAccountName',item['project']['projectNumber']+'-compute@developer.gserviceaccount.com')
            env={e['name']:e.get('value') for c in spec['containers'] for e in c.get('env',[]) if 'value' in e}
            dbpid=env.get('GOOGLE_CLOUD_PROJECT',pid)
            db=env.get('FIRESTORE_DATABASE_ID','(default)')
            tasks.extend([
              (pid+'--run-iam',['run','services','get-iam-policy',name,'--region='+region,'--project='+pid]),
              (pid+'--run-revisions',['run','revisions','list','--service='+name,'--region='+region,'--project='+pid]),
              (pid+'--domains',['run','domain-mappings','list','--region='+region,'--project='+pid]),
              (pid+'--sa-iam',['iam','service-accounts','get-iam-policy',sa,'--project='+pid]),
              (pid+'--sa',['iam','service-accounts','describe',sa,'--project='+pid]),
              (pid+'--indexes',['firestore','indexes','composite','list','--database='+db,'--project='+dbpid]),
            ])
            bucket=env.get('STORAGE_BUCKET')
            if bucket:
                tasks.extend([
                  (pid+'--bucket',['storage','buckets','describe','gs://'+bucket,'--project='+dbpid]),
                  (pid+'--bucket-iam',['storage','buckets','get-iam-policy','gs://'+bucket,'--project='+dbpid]),
                ])
            refs={e['valueFrom']['secretKeyRef']['name'] for c in spec['containers'] for e in c.get('env',[]) if e.get('valueFrom',{}).get('secretKeyRef')}
            for secret in refs:
                if '/' in secret: continue
                tasks.extend([
                  (pid+'--secret-'+secret,['secrets','describe',secret,'--project='+pid]),
                  (pid+'--secret-iam-'+secret,['secrets','get-iam-policy',secret,'--project='+pid]),
                  (pid+'--secret-versions-'+secret,['secrets','versions','list',secret,'--project='+pid]),
                ])
    tasks.extend([
      ('billing-accounts',['billing','accounts','list']),
      ('artefatos--repo',['artifacts','repositories','describe','gestao-de-dados-api','--location=us-central1','--project=artefatos']),
      ('artefatos--repo-iam',['artifacts','repositories','get-iam-policy','gestao-de-dados-api','--location=us-central1','--project=artefatos']),
      ('artefatos--project-iam',['projects','get-iam-policy','artefatos']),
      ('artefatos--publisher-iam',['iam','service-accounts','get-iam-policy','github-publicador@artefatos.iam.gserviceaccount.com','--project=artefatos']),
    ])
    def perform(t):
        key,args=t
        r=query(key,args)
        print(key,r['exit_code'],flush=True)
    with cf.ThreadPoolExecutor(max_workers=4) as pool:
        list(pool.map(perform,tasks))

def phase3():
    discovery=json.loads((EVID/'descoberta.json').read_text())
    tasks=[]
    for item in discovery:
        pid=item['project']['projectId']
        for s in item['targets']:
            region=s['metadata']['labels']['cloud.googleapis.com/location']
            tasks.extend([
              (pid+'--domains-beta',['beta','run','domain-mappings','list','--platform=managed','--region='+region,'--project='+pid]),
              (pid+'--backup-schedules',['firestore','backups','schedules','list','--database=gestao-de-dados','--project='+pid]),
              (pid+'--logging-buckets',['logging','buckets','list','--location=global','--project='+pid]),
            ])
    tasks.extend([
      ('artefatos--billing',['billing','projects','describe','artefatos']),
      ('artefatos--apis-enabled',['services','list','--enabled','--project=artefatos']),
    ])
    def perform(t):
        key,args=t; r=query(key,args)
        print(key,r['exit_code'],flush=True)
    with cf.ThreadPoolExecutor(max_workers=4) as pool:
        list(pool.map(perform,tasks))

if __name__=='__main__':
    globals()[sys.argv[1]]()
