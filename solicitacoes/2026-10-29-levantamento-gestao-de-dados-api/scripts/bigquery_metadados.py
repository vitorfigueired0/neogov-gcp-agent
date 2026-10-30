"""GETs de metadados BigQuery; token gcloud somente em memória; sem jobs SQL."""
import concurrent.futures as cf
import datetime
import json
import subprocess
import urllib.error
import urllib.parse
import urllib.request
from inventario import EVID, query

def main():
    # Mesma identidade/configuração do gcloud. Não usa ADC nem persiste o token.
    r=subprocess.run(['gcloud','auth','print-access-token'],capture_output=True,text=True,timeout=60)
    if r.returncode:
        raise SystemExit('Não foi possível obter autorização da sessão gcloud existente; nenhuma identidade alternativa será usada.')
    token=r.stdout.strip()
    def get(key,path):
        url='https://bigquery.googleapis.com/bigquery/v2/'+path
        req=urllib.request.Request(url,headers={'Authorization':'Bearer '+token})
        record={'method':'GET','url':url,'timestamp_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
        try:
            with urllib.request.urlopen(req,timeout=40) as resp:
                record.update(status=resp.status,data=json.load(resp))
        except urllib.error.HTTPError as e:
            record.update(status=e.code,error=json.loads(e.read().decode()))
        except Exception as e:
            record.update(status=-1,error=type(e).__name__)
        (EVID/(key+'.json')).write_text(json.dumps(record,ensure_ascii=False,indent=2))
        return record
    allowed={p['projectId'] for p in json.loads((EVID/'projetos-lgpdweb.json').read_text())}|{'artefatos'}
    projects=[p for p in json.loads((EVID/'projetos-visiveis.json').read_text())['data'] if p['projectId'] in allowed]
    def inspect(p):
        pid=p['projectId']
        found=[]; page=''; pages=0
        while True:
            suffix='?all=true&maxResults=1000'+('&pageToken='+urllib.parse.quote(page) if page else '')
            result=get(pid+'--bq-datasets-'+str(pages),'projects/'+pid+'/datasets'+suffix)
            if result['status']!=200:
                print(pid,'datasets',result['status'],flush=True)
                return
            ds=result['data'].get('datasets',[])
            for d in ds:
                did=d['datasetReference']['datasetId']; tpage=''; tpages=0
                if did.startswith('_'): continue
                while True:
                    tables=get(pid+'--bq-tables-'+did+'-'+str(tpages),'projects/'+pid+'/datasets/'+did+'/tables?maxResults=1000'+('&pageToken='+urllib.parse.quote(tpage) if tpage else ''))
                    for t in tables.get('data',{}).get('tables',[]):
                        tid=t['tableReference']['tableId']
                        if tid.startswith('gcp_billing_export') or tid=='cloud_pricing_export':
                            found.append(t['tableReference'])
                            get(pid+'--bq-billing-table-'+tid,'projects/'+pid+'/datasets/'+did+'/tables/'+tid)
                            get(pid+'--bq-billing-dataset-'+did,'projects/'+pid+'/datasets/'+did)
                    tpage=tables.get('data',{}).get('nextPageToken','')
                    if not tpage: break
                    tpages+=1
            page=result['data'].get('nextPageToken','')
            if not page: break
            pages+=1
        print(pid,'datasets',pages+1,'billing_tables',found,flush=True)
    with cf.ThreadPoolExecutor(max_workers=4) as pool:
        list(pool.map(inspect,projects))

if __name__=='__main__': main()
