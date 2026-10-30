"""Verifica consistência dos artefatos/evidências. Sem chamadas GCP."""
import ast
import hashlib
import json
import re
from pathlib import Path
from inventario import ROOT, EVID

ASSET=ROOT.parents[1]/'ativos'/'gestao-de-dados-api'

def main():
    snapshot=json.loads((ASSET/'inventario.json').read_text())
    services=snapshot['services']; checks={}
    original=Path('/home/vitor/projetos/NEOGOV/gestao-de-dados-api/README.md')
    checks['README idêntico ao original']=(ASSET/'README.md').read_bytes()==original.read_bytes()==(ROOT/'README-fornecido.md').read_bytes()
    checks['26 projetos / 23 serviços / 3 ausências']=snapshot['projects_scanned']==26 and len(services)==23 and len(snapshot['absent_exact_name'])==3
    checks['23 projetos distintos']=len({s['project_id'] for s in services})==23
    checks['23 serviços Ready e tráfego 100%']=all(s['ready']=='True' and len(s['traffic'])==1 and s['traffic'][0].get('percent')==100 and s['traffic'][0]['revisionName']==s['latest_ready_revision'] for s in services)
    expected={('reportedBy','timestamp','__name__'),('reportedBy','status','timestamp','__name__'),('reportedBy','reasonCode','timestamp','__name__'),('reportedBy','status','reasonCode','timestamp','__name__')}
    checks['92 índices esperados READY']=all(len(s['database_indexes'])==4 and {tuple(f['fieldPath'] for f in i['fields']) for i in s['database_indexes']}==expected and all(i['state']=='READY' and i['queryScope']=='COLLECTION' and all(f['order']==('DESCENDING' if f['fieldPath'] in ['timestamp','__name__'] else 'ASCENDING') for f in i['fields']) for i in s['database_indexes']) for s in services)
    checks['23 bancos Native Standard / us-central1']=all(s['database']['type']=='FIRESTORE_NATIVE' and s['database']['databaseEdition']=='STANDARD' and s['database']['locationId']=='us-central1' for s in services)
    checks['23 buckets protegidos e em us-central1']=all(s['bucket']['uniform_bucket_level_access'] and s['bucket']['public_access_prevention']=='enforced' and s['bucket']['location']=='US-CENTRAL1' for s in services)
    checks['23 bindings Storage e autoassinatura']=all({'roles/storage.objectCreator','roles/storage.objectViewer'}<={r['role'] for r in s['bucket_runtime_roles']} and 'roles/iam.serviceAccountTokenCreator' in {r['role'] for r in s['self_service_account_roles']} for s in services)
    checks['23 domínios e certificados Ready']=all(len(s['domains'])==1 and all(next(c['status'] for c in d['status']['conditions'] if c['type']=='Ready')=='True' and next(c['status'] for c in d['status']['conditions'] if c['type']=='CertificateProvisioned')=='True' for d in s['domains']) for s in services)
    checks['23 vínculos Billing corretos']=all(s['billing']['billingEnabled'] and s['billing']['billingAccountName']=='billingAccounts/01017B-9A8236-AA7CA7' for s in services)
    # QA concede secretAccessor no projeto e não no segredo. Não confundir escopos.
    checks['Secrets com concessão de acesso no segredo OU projeto']=all(
        secret['metadata'] and secret['versions_metadata'] and
        any(r['role']=='roles/secretmanager.secretAccessor' and not r.get('condition')
            for r in secret['runtime_roles']+s['project_runtime_roles'])
        for s in services for secret in s['secrets'])
    checks['22 agendas de backup e lgpdweb sem agenda']=sum(bool(s['database_backup_schedules']) for s in services)==22 and not next(s for s in services if s['project_id']=='lgpdweb')['database_backup_schedules']
    checks['Snapshots request/ativo iguais']=(ROOT/'inventario-consolidado.json').read_bytes()==(ASSET/'inventario.json').read_bytes()
    for f in (ROOT/'scripts').glob('*.py'): ast.parse(f.read_text())
    checks['Sintaxe Python verificada sem executar GCP']=True
    allowed={p['projectId'] for p in json.loads((EVID/'projetos-lgpdweb.json').read_text())}|{'artefatos'}
    checks['Metadados BQ restantes só no escopo']=all(f.name.split('--bq-',1)[0] in allowed for f in EVID.glob('*--bq-*.json'))
    for f in EVID.glob('*.json'): json.loads(f.read_text())
    checks['JSONs válidos']=True
    mapping=json.loads((ROOT/'consultas/mapeamento-recursos.json').read_text())
    sql=(ROOT/'consultas/custos_detalhados_30_dias.sql').read_text()
    checks['Mapa SQL cobre 23 projetos sem duplicatas']=len(mapping)==23 and len({x['project_id'] for x in mapping})==23 and all(sql.count("'"+r['project_id']+"' AS project_id")==1 for r in mapping)
    checks['SQL somente SELECT e parâmetros pendentes']='__TABELA_EXPORT_DETALHADO__' in sql and '@inicio' in sql and '@fim' in sql and not re.search(r'^\s*(CREATE|ALTER|DROP|INSERT|DELETE|UPDATE|MERGE)\b',sql,re.I|re.M)
    broken=[]
    for f in [*ASSET.glob('*.md'),ROOT/'plano-custos-bigquery.md']:
        # O README original referencia o repositório de origem; não é modificado.
        if f.name=='README.md': continue
        for link in re.findall(r'\]\(([^)]+)\)',f.read_text()):
            if '://' not in link and not link.startswith('#') and not (f.parent/link.split('#')[0]).exists(): broken.append(str(f)+': '+link)
    checks['Links locais da documentação nova existem']=not broken
    text='\n'.join(('OK' if ok else 'FALHA')+' — '+name for name,ok in checks.items())
    text+='\n\nSHA256 README: '+hashlib.sha256((ASSET/'README.md').read_bytes()).hexdigest()
    text+='\n\nSQL não executado e sem dry-run no BigQuery: falta tabela-fonte autorizada.\n'
    text+='Verificação de Secrets confirma concessões explícitas, não simula permissões efetivas.\n'
    if broken: text+='\n'.join(broken)+'\n'
    (ROOT/'verificacoes.txt').write_text(text)
    print(text)
    if not all(checks.values()): raise SystemExit(1)

if __name__=='__main__': main()
