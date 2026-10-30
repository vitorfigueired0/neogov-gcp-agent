"""Consolida evidências locais; não faz chamadas GCP."""
import collections
import datetime
import hashlib
import json
from pathlib import Path
from zoneinfo import ZoneInfo
from inventario import ROOT, EVID

ASSET=ROOT.parents[1]/'ativos'/'gestao-de-dados-api'
STAMP=datetime.datetime.now(ZoneInfo('America/Sao_Paulo'))
DISCOVERY=json.loads((EVID/'descoberta.json').read_text())

def load(key,default=None):
    f=EVID/(key+'.json')
    if not f.exists(): return default
    r=json.loads(f.read_text())
    return r.get('data',default) if r.get('exit_code',0)==0 and r.get('status',200)==200 else default

def roles(policy,principal):
    return [{'role':b['role'],**({'condition':b['condition']} if 'condition' in b else {})}
            for b in (policy or {}).get('bindings',[]) if principal in b.get('members',[])]

def roletext(rs):
    return '; '.join('`'+r['role']+'`'+(' — condição: `'+r['condition'].get('expression','')+'`' if r.get('condition') else '') for r in rs) or 'Nenhuma concessão direta encontrada'

def table(headers,rows):
    return '\n'.join(['| '+' | '.join(headers)+' |','| '+' | '.join(['---']*len(headers))+' |']+['| '+' | '.join(str(c).replace('|','\\|').replace('\n',' ') for c in r)+' |' for r in rows])+'\n'

def write(path,text):
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(text)

def main():
    inventory=[]
    for item in DISCOVERY:
        pid=item['project']['projectId']
        for s in item['targets']:
            spec=s['spec']['template']['spec']; sa=spec['serviceAccountName']; member='serviceAccount:'+sa
            env=[e for c in spec['containers'] for e in c.get('env',[])]
            values={e['name']:e.get('value') for e in env if 'value' in e}
            refs=[{'env':e['name'],**e['valueFrom']['secretKeyRef']} for e in env if e.get('valueFrom',{}).get('secretKeyRef')]
            annotations=s['metadata'].get('annotations',{})
            tann=s['spec']['template'].get('metadata',{}).get('annotations',{})
            db=next((x for x in load(pid+'--databases',[]) if x['name'].endswith('/'+values.get('FIRESTORE_DATABASE_ID','(default)'))),{})
            domains=[x for x in load(pid+'--domains-beta',[]) if x.get('spec',{}).get('routeName')=='gestao-de-dados-api']
            revision_specs=load(pid+'--run-revisions',[])
            inventory.append({
              'project_id':pid,'project_number':item['project']['projectNumber'],'project_name':item['project']['name'],
              'environment':'QA (confirmado pelo usuário)' if pid=='pm-neogov-qa-lgpdweb' else ('production-test (label GCP)' if pid=='lgpdweb' else 'não confirmado; configuração aponta auth produção'),
              'region':s['metadata']['labels']['cloud.googleapis.com/location'],
              'service_name':'gestao-de-dados-api','creation_time':s['metadata']['creationTimestamp'],
              'ready':next((x['status'] for x in s['status'].get('conditions',[]) if x['type']=='Ready'),None),
              'traffic':s['status'].get('traffic',[]),'latest_ready_revision':s['status'].get('latestReadyRevisionName'),
              'runtime_service_account':sa,'run_url':s['status'].get('url'),'domains':domains,
              'image':spec['containers'][0]['image'],'cpu_memory':spec['containers'][0].get('resources'),
              'concurrency':spec.get('containerConcurrency'),'timeout_seconds':spec.get('timeoutSeconds'),
              'service_min_instances':annotations.get('run.googleapis.com/minScale','não explicitado'),
              'service_max_instances':annotations.get('run.googleapis.com/maxScale','não explicitado'),
              'revision_min_instances':tann.get('autoscaling.knative.dev/minScale','não explicitado'),
              'revision_max_instances':tann.get('autoscaling.knative.dev/maxScale','não explicitado'),
              'ingress':annotations.get('run.googleapis.com/ingress'),
              'invoker_iam_disabled':annotations.get('run.googleapis.com/invoker-iam-disabled'),
              'network_annotations':{k:v for k,v in {**annotations,**tann}.items() if any(w in k for w in ['vpc','network','egress'])},
              'environment_values':values,'secret_references':refs,
              'database':db,'database_indexes':load(pid+'--indexes',[]),'database_backup_schedules':load(pid+'--backup-schedules',[]),
              'bucket':load(pid+'--bucket',{}),'project_runtime_roles':roles(load(pid+'--project-iam'),member),
              'bucket_runtime_roles':roles(load(pid+'--bucket-iam'),member),
              'self_service_account_roles':roles(load(pid+'--sa-iam'),member),
              'run_iam':load(pid+'--run-iam',{}),
              'secrets':[{ 'reference':ref,'metadata':load(pid+'--secret-'+ref['name']),
                'versions_metadata':load(pid+'--secret-versions-'+ref['name']),
                'runtime_roles':roles(load(pid+'--secret-iam-'+ref['name']),member)} for ref in refs],
              'billing':load(pid+'--billing',{}),'logging_sinks':load(pid+'--log-sinks',[]),
              'logging_buckets':load(pid+'--logging-buckets',[]),'revision_count':len(revision_specs),
              'compute_inventory_readable':all(load(pid+'--'+k) is not None for k in ['neg','backends','urlmaps','forwarding']),
              'compute_resources':{k:load(pid+'--'+k) for k in ['neg','backends','urlmaps','forwarding']},
            })
    inventory.sort(key=lambda x:x['project_id'])
    absent=sorted(x['project']['projectId'] for x in DISCOVERY if not x['targets'] and x['exit_code']==0)
    snapshot={'collected_at':STAMP.isoformat(),'scope':'26 projetos visíveis com lgpdweb no nome/ID e dependências em artefatos; outros projetos excluídos',
              'projects_scanned':len(DISCOVERY),'services_found':len(inventory),'absent_exact_name':absent,'services':inventory,
              'limitations':['IAM consultado não inclui grupos transitivos, condições avaliadas, políticas Deny ou herança de organização/pasta.',
                 'Configuração e estado Ready não comprovam funcionamento de login, dados, uploads ou conectividade.',
                 'Metadados atuais não reconstituem todos os recursos excluídos ou configurações históricas dos últimos 30 dias.',
                 'Valores de segredos, documentos Firestore, conteúdo de objetos e linhas de faturamento não foram lidos.']}
    write(ASSET/'inventario.json',json.dumps(snapshot,ensure_ascii=False,indent=2)+'\n')
    write(ROOT/'inventario-consolidado.json',json.dumps(snapshot,ensure_ascii=False,indent=2)+'\n')
    invrows=[]
    for x in inventory:
        env=x['environment_values'];dom=', '.join(d['metadata']['name'] for d in x['domains'])
        invrows.append([f"`{x['project_id']}`",dom,f"`{env.get('STORAGE_BUCKET')}`",'; '.join(f"`{r['name']}:{r['key']}`" for r in x['secret_references'])])
    write(ASSET/'inventario.md','# Inventário de instalações\n\nData de coleta: '+STAMP.isoformat()+'.\n\n'+
      f"Foram consultados {len(DISCOVERY)} projetos LGPDWeb; {len(inventory)} contêm o serviço de nome exato `gestao-de-dados-api`. Todos estão em `us-central1`, com `Ready=True` e tráfego de 100% na revisão pronta mais recente no momento da coleta.\n\n"+
      'Cada linha usa o banco Firestore `gestao-de-dados` no próprio projeto e a conta `gestao-de-dados-api-runtime@PROJETO.iam.gserviceaccount.com`.\n\n'+
      table(['Projeto','Domínio da API','Bucket configurado','Secrets (nome:versão)'],invrows)+
      '\n## Sem serviço com esse nome\n\n'+', '.join('`'+x+'`' for x in absent)+'. As listagens foram bem-sucedidas em todas as regiões; isso não exclui serviços com outros nomes.\n\n'+
      '## Ambientes e versões\n\nQA confirmado: `pm-neogov-qa-lgpdweb`. `lgpdweb` possui label `environment=production-test`. O ambiente dos outros 21 projetos não foi confirmado; todos apontam para a autenticação de produção.\n\n'+
      '22 instalações usam o digest `72ab7958af9cf666d167d39f5ae68c5562fa3613c034a6e9688a545e16f8a439`. QA usa `6e8f065a970cd5fa1a279701894d1f3ae740e15dfd540c36e5caf3ab3892ad5d`. Ambos estão em `us-central1-docker.pkg.dev/artefatos/gestao-de-dados-api/gestao-de-dados-api`.\n\n'+
      'Detalhes completos por instalação, revisões, horários, tráfego e políticas: [inventario.json](inventario.json). Evidências originais sanitizadas e comandos: [pasta da solicitação](../../solicitacoes/'+ROOT.name+'/).\n')

    components='''# Componentes de Gestão de Dados — API

Inventário baseado no README fornecido e em consultas GCP em 29/10/2026. O [README.md](README.md) foi copiado integralmente; suas instruções de implantação foram tratadas como documentação. O estado implantado prevalece nas conclusões abaixo.

## Fluxo e dependências

```mermaid
flowchart LR
  Browser[Frontend do cliente] -->|HTTPS e cookie| Domain[Domínio mapeado diretamente no Cloud Run]
  Domain --> Run[gestao-de-dados-api / us-central1]
  Run -->|sessão validada na central| Auth[neogov-auth / produção ou desenvolvimento]
  Run -->|SDK e IAM da conta runtime| Firestore[Firestore / gestao-de-dados]
  Run -->|metadados e URLs assinadas| Storage[Bucket de mídias do cliente]
  Browser -->|PUT e GET com URL assinada| Storage
  Secrets[Secret Manager / referências de versão] --> Run
  Run --> Logs[Cloud Logging / buckets compartilhados do projeto]
  CI[GitHub Actions / Workload Identity] --> AR[Artifact Registry / artefatos]
  AR -->|leitura pelo agente Cloud Run| Run
```

O diagrama descreve o fluxo documentado e os vínculos configurados. Não foram executados login, chamadas funcionais, leitura/escrita de documentos ou uploads.

| Componente | Papel e estado encontrado | Relevância de custo |
| --- | --- | --- |
| Cloud Run | 23 serviços NestJS, porta 8080, 1 vCPU e 1 GiB; configuração completa no inventário | CPU, memória, requisições e transferência, conforme SKUs efetivos |
| Firestore | Um banco nomeado `gestao-de-dados` por instalação, Native/Standard, `us-central1`; quatro índices `complaints` READY em cada banco | Leituras, escritas, exclusões, armazenamento, índices, backups e transferência |
| Cloud Storage | Um bucket configurado por instalação, STANDARD em US-CENTRAL1, acesso uniforme e prevenção de acesso público enforced | Armazenamento, operações, transferência e dados retidos por soft delete |
| Secret Manager | 22 instalações referenciam `NEOGOV_AUTH_API_KEY` e `NEOGOV_AUTH_ALLOWED_ISSUERS` por `latest`; `lgpdweb` usa `neogov-auth-api-key:1` | Versões ativas, acessos e eventual replicação; não foram lidos valores |
| Conta de execução | `gestao-de-dados-api-runtime@PROJETO.iam.gserviceaccount.com` | Define acessos SDK e assinatura de URLs; ver matriz IAM |
| neogov-auth | QA: `https://api.auth-develop.neogov.com.br`; demais: `https://api.auth.neogov.com.br` | Dependência externa ao escopo de inspeção; custo da central não apurado nem rateado |
| Artifact Registry | Repositório central `artefatos/us-central1/gestao-de-dados-api`, imagem fixada por digest | Armazenamento, transferência e análise de vulnerabilidades; compartilhado entre instalações |
| Domínio e TLS | 23 mapeamentos diretos de domínio no Cloud Run, certificados provisionados e Ready=True | Não foi identificada dependência de balanceador para esses mapeamentos; DNS externo não auditado |
| Cloud Logging | Sinks locais para `_Default` e `_Required`; retenções consultadas de 30 e 400 dias | Ingestão/retenção são por bucket e podem misturar aplicações; não atribuir todo o projeto à API |

## Configuração e segurança observadas

Todos os serviços têm `ingress=all` e `run.googleapis.com/invoker-iam-disabled=true`. A invocação pública é permitida sem checagem IAM Google, mesmo com política do serviço sem `allUsers`. O README descreve validação de cookie na neogov-auth; essa validação não foi testada. Exposição de `/docs` e `/docs-json` também não foi testada.

22 serviços têm limites configurados de 100 instâncias no serviço e revisão. `lgpdweb` limita o serviço a 3. Não foi encontrada configuração de mínimo positivo. Esses são limites configurados, não medições de instâncias nem garantia de teto financeiro. O timeout da central é 20.000 ms em 22 instalações e 5.000 ms em `lgpdweb`.

22 bancos têm agenda semanal de backup aos domingos, retenção de 98 dias; `lgpdweb` não possui agenda. Agenda configurada não comprova backup já produzido ou restauração válida. Todos os 23 bancos têm PITR e proteção contra exclusão desabilitados; todos informam `freeTier=false`.

Todos os buckets de mídias têm soft delete de 7 dias no estado coletado. A maioria configura cache CORS de 3.600 segundos; o README sugere 300. As origens estão registradas por instalação no JSON. Não foram lidos objetos ou comprovados uploads pelo navegador.

Não foram encontrados conectores VPC/Direct VPC ou configuração especial de egress nas configurações dos 23 serviços. As listagens Compute de 21 projetos retornaram vazias para NEGs, backends, URL maps e forwarding rules; em `cides-lgpdweb` e QA a API Compute está desabilitada e as consultas falharam. Ela não foi habilitada. Isso não descarta infraestrutura ou DNS em outros projetos.

## Permissões e diferenças a revisar

As concessões da conta runtime estão em [permissoes.md](permissoes.md). Em 22 projetos o papel Firestore é concedido sem condição de banco e alcança outros bancos do projeto; `lgpdweb` possui condição ao banco `gestao-de-dados`. QA também concede `roles/run.editor` e `roles/secretmanager.secretAccessor` no projeto. O escopo desses papéis é maior que o descrito para o funcionamento normal da API. Nenhuma concessão foi alterada.

Quase todas as referências de segredos usam `latest`, em desacordo com a recomendação de versão numérica do README. A troca da versão apontada por `latest` pode afetar novas instâncias; uma reversão de revisão pode continuar dependendo do valor resolvido no segredo. Não foi feita rotação nem leitura de payload.

O publicador central aceita Workload Identity de vários repositórios GitHub, incluindo `neogovbr/gestao-de-dados-api`. Assim, a identidade de publicação é compartilhada. O agente gerenciado de Cloud Run de cada um dos 23 projetos possui leitura no repositório central. A conta runtime de QA também possui leitura no repositório.

## Limites

O levantamento cobre os 26 projetos visíveis com LGPDWeb no nome/ID e o repositório central em `artefatos`. Projetos inacessíveis ou com outros nomes podem existir. Não se trata de teste de disponibilidade funcional nem de auditoria completa de todas as permissões efetivas. Herança, políticas Deny, participação em grupos e mudanças durante a coleta podem alterar o resultado.

Veja [inventario.md](inventario.md), [inventario.json](inventario.json) e [custos.md](custos.md).
'''
    write(ASSET/'componentes.md',components)
    permission_rows=[]
    for x in inventory:
        permission_rows.append([f"`{x['project_id']}`",roletext(x['project_runtime_roles']),roletext(x['bucket_runtime_roles']),roletext(x['self_service_account_roles'])])
    secrets_rows=[]
    for x in inventory:
        for secret in x['secrets']:
            ref=secret['reference']
            secrets_rows.append([f"`{x['project_id']}`",f"`{ref['name']}:{ref['key']}`",ref['env'],roletext(secret['runtime_roles'])])
    write(ASSET/'permissoes.md','# Permissões da API\n\nData: '+STAMP.isoformat()+'. Principal de execução de cada linha: `serviceAccount:gestao-de-dados-api-runtime@PROJETO.iam.gserviceaccount.com`.\n\n'+
      table(['Projeto','Concessões no projeto','Concessões no bucket configurado','Concessões na própria conta'],permission_rows)+
      '\n## Secrets referenciados\n\n'+table(['Projeto','Secret:versão','Variável','Concessão local à runtime'],secrets_rows)+
      '\nEm QA há também `roles/secretmanager.secretAccessor` no projeto, que pode conceder acesso além dos segredos listados. `latest` é referência móvel; os estados e números das versões estão no inventário JSON, sem payloads.\n\n'+
      '## Imagens e publicação\n\nAgentes `service-NUMERO@serverless-robot-prod.iam.gserviceaccount.com` dos 23 projetos: `roles/artifactregistry.reader` no repositório `artefatos/us-central1/gestao-de-dados-api`. Runtime de QA: mesmo papel no repositório. Publicador `github-publicador@artefatos.iam.gserviceaccount.com`: `roles/artifactregistry.writer` no repositório. A política dessa conta concede `roles/iam.workloadIdentityUser` a principalSets de vários repositórios, incluindo `neogovbr/gestao-de-dados-api`.\n\n'+
      '## Entrada HTTP e alcance da evidência\n\nOs 23 serviços têm checagem IAM de invocação desabilitada e ingresso `all`; não depender de uma binding `allUsers` para identificar acesso público. CORS limita o navegador e não substitui autenticação ou IAM. As permissões da conta runtime para Storage e Firestore são diferentes da permissão HTTP de invocar a API.\n\n'+
      'Esta matriz relata concessões explícitas encontradas nas políticas de projeto, bucket, segredo e conta de serviço. Condições são reproduzidas, não avaliadas em uma operação real. Não inclui IAM herdado de pastas/organização, Deny, grupos, permissões administrativas de todos os usuários, nem prova de mínimo privilégio. Não foram criadas chaves ou alteradas identidades.\n')
    build_queries(inventory)
    write(ASSET/'custos.md','# Custos da API e dependências\n\nPeríodo solicitado: **últimos 30 dias**. Ainda não há total monetário apurado: não foi encontrada tabela Cloud Billing nos datasets visíveis dos projetos LGPDWeb e `artefatos`; fontes fora desse escopo foram excluídas conforme orientação do usuário. Ausência de exportação acessível não significa gasto zero.\n\n'+
      'Foram preparadas uma consulta detalhada que associa Cloud Run, banco, bucket e segredos de cada instalação e uma consulta padrão que mostra somente totais de contexto por projeto/SKU, sem atribuí-los à API. Ambas incluem créditos e preservam a moeda. Não foram executadas ou validadas por dry-run no BigQuery porque falta a tabela-fonte autorizada.\n\n'+
      f'[Proposta de BigQuery, funcionamento, impactos e reversão](../../solicitacoes/{ROOT.name}/plano-custos-bigquery.md).\n\n'+
      f'[Consulta detalhada — últimos 30 dias](../../solicitacoes/{ROOT.name}/consultas/custos_detalhados_30_dias.sql).\n\n'+
      f'[Consulta padrão — contexto por projeto/SKU](../../solicitacoes/{ROOT.name}/consultas/custos_padrao_30_dias.sql).\n')
    print('Documentação e inventário gerados para',len(inventory),'instalações.')

def build_queries(inventory):
    records=[]
    for x in inventory:
        env=x['environment_values']
        records.append({'project_id':x['project_id'],'project_number':x['project_number'],'region':x['region'],
            'service_name':x['service_name'],'database_id':env['FIRESTORE_DATABASE_ID'],'bucket_name':env['STORAGE_BUCKET'],
            'secret_names':sorted({r['name'] for r in x['secret_references']})})
    write(ROOT/'consultas'/'mapeamento-recursos.json',json.dumps(records,ensure_ascii=False,indent=2)+'\n')
    def q(v): return "'"+v.replace("'","\\'")+"'"
    structs=[]
    for x in records:
        fields=[q(x[k])+' AS '+k for k in ['project_id','project_number','region','service_name','database_id','bucket_name']]
        fields.append('['+', '.join(q(s) for s in x['secret_names'])+'] AS secret_names')
        structs.append('    STRUCT('+', '.join(fields)+')')
    mapping='WITH inventario AS (\n  SELECT * FROM UNNEST([\n'+',\n'.join(structs)+'\n  ])\n),\n'
    header='''-- GoogleSQL. PREPARADA; NÃO EXECUTADA; requer tabela-fonte autorizada.
-- Substitua SOMENTE __TABELA_EXPORT_DETALHADO__ pelo nome totalmente qualificado.
-- Parâmetros TIMESTAMP: @inicio (inclusivo), @fim (exclusivo), intervalo de 30 dias.
-- A consulta não cria views, tabelas ou rotinas. Use dry-run e maximumBytesBilled.
-- _PARTITIONTIME é usado apenas como limite inferior para não perder ajustes tardios.
-- Não misture exportações padrão e detalhada no mesmo total: geraria duplicidade.
'''
    body='''base AS (
  SELECT
    b.project.id AS project_id, b.service.description AS servico_gcp,
    b.sku.id AS sku_id, b.sku.description AS sku,
    b.currency AS moeda, b.cost_type AS tipo_custo,
    b.invoice.month AS mes_fatura,
    DATE(b.usage_start_time, 'America/Sao_Paulo') AS dia_uso,
    IFNULL(b.resource.name, '') AS recurso_nome,
    IFNULL(b.resource.global_name, '') AS recurso_global,
    IFNULL(b.location.region, '') AS regiao,
    b.labels AS labels,
    CAST(b.cost AS NUMERIC) AS custo_bruto,
    IFNULL((SELECT SUM(CAST(c.amount AS NUMERIC)) FROM UNNEST(b.credits) c), 0) AS creditos
  FROM `__TABELA_EXPORT_DETALHADO__` b
  WHERE b.usage_start_time >= @inicio AND b.usage_start_time < @fim
    AND b._PARTITIONTIME >= TIMESTAMP_TRUNC(@inicio, DAY)
    AND (b.project.id IN (SELECT project_id FROM inventario) OR b.project.id = 'artefatos')
), classificado AS (
  SELECT b.*,
    CASE
      WHEN i.project_id IS NOT NULL AND servico_gcp = 'Cloud Run'
        AND (regiao = i.region OR regiao = '')
        AND (recurso_nome = i.service_name
          OR REGEXP_CONTAINS(CONCAT(recurso_nome, '/', recurso_global), r'/services/gestao-de-dados-api(/|$)')
          OR EXISTS (SELECT 1 FROM UNNEST(b.labels) l
            WHERE l.key IN ('goog-cloud-run-service','cloud.googleapis.com/service_name')
              AND l.value = i.service_name)) THEN 'Cloud Run da API'
      WHEN i.project_id IS NOT NULL AND servico_gcp IN ('App Engine','Cloud Firestore','Firestore','Cloud Datastore')
        AND (recurso_nome = i.database_id
          OR REGEXP_EXTRACT(recurso_global, r'/databases/([^/]+)') = i.database_id
          OR REGEXP_EXTRACT(recurso_nome, r'/databases/([^/]+)') = i.database_id) THEN 'Firestore associado'
      WHEN i.project_id IS NOT NULL AND servico_gcp = 'Cloud Storage'
        AND (recurso_nome = i.bucket_name
          OR i.bucket_name IN UNNEST(SPLIT(recurso_global, '/'))
          OR REGEXP_EXTRACT(recurso_nome, r'/buckets/([^/]+)') = i.bucket_name) THEN 'Bucket associado'
      WHEN i.project_id IS NOT NULL AND servico_gcp = 'Secret Manager'
        AND (recurso_nome IN UNNEST(i.secret_names)
          OR REGEXP_EXTRACT(recurso_nome, r'/secrets/([^/]+)') IN UNNEST(i.secret_names)
          OR REGEXP_EXTRACT(recurso_global, r'/secrets/([^/]+)') IN UNNEST(i.secret_names)) THEN 'Secrets associados'
      WHEN b.project_id = 'artefatos' AND servico_gcp IN ('Artifact Registry','Container Analysis','Artifact Analysis')
        AND (REGEXP_CONTAINS(recurso_global, r'/repositories/gestao-de-dados-api(/|$)')
          OR REGEXP_CONTAINS(recurso_nome, r'/repositories/gestao-de-dados-api(/|$)')) THEN 'Repositório central associado (compartilhado)'
      WHEN servico_gcp = 'Cloud Logging' THEN 'Logging do projeto (compartilhado; sem rateio)'
      WHEN b.project_id = 'artefatos' THEN 'artefatos sem vínculo confirmado; não atribuir à API'
      WHEN recurso_nome = '' AND recurso_global = '' THEN 'Sem identificador de recurso; não atribuir à API'
      ELSE 'Outro recurso ou vínculo ainda não reconhecido; não atribuir à API'
    END AS componente
  FROM base b LEFT JOIN inventario i ON b.project_id = i.project_id
)
SELECT
  project_id, dia_uso, mes_fatura, moeda, servico_gcp, sku_id, sku, tipo_custo, componente,
  CASE WHEN componente IN ('Cloud Run da API','Firestore associado','Bucket associado','Secrets associados')
    THEN 'custo do recurso associado; exclusividade precisa de validação'
    ELSE 'fora do subtotal associado; exige análise ou rateio' END AS atribuicao,
  COUNT(*) AS linhas_faturamento,
  SUM(custo_bruto) AS custo_bruto,
  SUM(creditos) AS creditos,
  SUM(custo_bruto + creditos) AS custo_liquido
FROM classificado
GROUP BY project_id, dia_uso, mes_fatura, moeda, servico_gcp, sku_id, sku, tipo_custo, componente, atribuicao
ORDER BY project_id, dia_uso, componente, custo_liquido DESC;
'''
    write(ROOT/'consultas'/'custos_detalhados_30_dias.sql',header+mapping+body)
    standard='''-- GoogleSQL. Somente CONTEXTO POR PROJETO, não é custo isolado da API.
-- Fonte padrão, substitua __TABELA_EXPORT_PADRAO__; @inicio e @fim são TIMESTAMP.
-- Não somar este resultado ao da exportação detalhada.
SELECT
  b.project.id AS project_id, DATE(b.usage_start_time, 'America/Sao_Paulo') AS dia_uso,
  b.invoice.month AS mes_fatura, b.currency AS moeda,
  b.service.description AS servico_gcp, b.sku.id AS sku_id, b.sku.description AS sku,
  b.cost_type AS tipo_custo,
  SUM(CAST(b.cost AS NUMERIC)) AS custo_bruto,
  SUM(IFNULL((SELECT SUM(CAST(c.amount AS NUMERIC)) FROM UNNEST(b.credits) c), 0)) AS creditos,
  SUM(CAST(b.cost AS NUMERIC) + IFNULL((SELECT SUM(CAST(c.amount AS NUMERIC)) FROM UNNEST(b.credits) c), 0)) AS custo_liquido
FROM `__TABELA_EXPORT_PADRAO__` b
WHERE b.usage_start_time >= @inicio AND b.usage_start_time < @fim
  AND b._PARTITIONTIME >= TIMESTAMP_TRUNC(@inicio, DAY)
  AND b.project.id IN ('''+', '.join(q(x['project_id']) for x in records)+", 'artefatos')\n"+'''GROUP BY project_id, dia_uso, mes_fatura, moeda, servico_gcp, sku_id, sku, tipo_custo
ORDER BY project_id, dia_uso, servico_gcp, custo_liquido DESC;
'''
    write(ROOT/'consultas'/'custos_padrao_30_dias.sql',standard)

if __name__=='__main__': main()
