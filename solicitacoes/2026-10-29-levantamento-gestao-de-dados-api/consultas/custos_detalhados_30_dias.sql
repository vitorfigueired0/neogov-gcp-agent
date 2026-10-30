-- GoogleSQL. PREPARADA; NÃO EXECUTADA; requer tabela-fonte autorizada.
-- Substitua SOMENTE __TABELA_EXPORT_DETALHADO__ pelo nome totalmente qualificado.
-- Parâmetros TIMESTAMP: @inicio (inclusivo), @fim (exclusivo), intervalo de 30 dias.
-- A consulta não cria views, tabelas ou rotinas. Use dry-run e maximumBytesBilled.
-- _PARTITIONTIME é usado apenas como limite inferior para não perder ajustes tardios.
-- Não misture exportações padrão e detalhada no mesmo total: geraria duplicidade.
WITH inventario AS (
  SELECT * FROM UNNEST([
    STRUCT('cachoeiradouradamglgpdweb' AS project_id, '949172226134' AS project_number, 'us-central1' AS region, 'gestao-de-dados-api' AS service_name, 'gestao-de-dados' AS database_id, 'gestao-de-dados-cachoeiradouradamglgpdweb' AS bucket_name, ['NEOGOV_AUTH_ALLOWED_ISSUERS', 'NEOGOV_AUTH_API_KEY'] AS secret_names),
    STRUCT('camaraconceicaoalagoaslgpdweb' AS project_id, '152048161192' AS project_number, 'us-central1' AS region, 'gestao-de-dados-api' AS service_name, 'gestao-de-dados' AS database_id, 'gestao-de-dados-camaraconceicaoalagoaslgpdweb' AS bucket_name, ['NEOGOV_AUTH_ALLOWED_ISSUERS', 'NEOGOV_AUTH_API_KEY'] AS secret_names),
    STRUCT('camarafrutallgpdweb' AS project_id, '253187335391' AS project_number, 'us-central1' AS region, 'gestao-de-dados-api' AS service_name, 'gestao-de-dados' AS database_id, 'gestao-de-dados-camarafrutallgpdweb' AS bucket_name, ['NEOGOV_AUTH_ALLOWED_ISSUERS', 'NEOGOV_AUTH_API_KEY'] AS secret_names),
    STRUCT('camaraituiutabalgpdweb-a1a06' AS project_id, '955512464223' AS project_number, 'us-central1' AS region, 'gestao-de-dados-api' AS service_name, 'gestao-de-dados' AS database_id, 'gestao-de-dados-camaraituiutabalgpdweb-a1a06' AS bucket_name, ['NEOGOV_AUTH_ALLOWED_ISSUERS', 'NEOGOV_AUTH_API_KEY'] AS secret_names),
    STRUCT('camarateresopolislgpdweb' AS project_id, '428870652797' AS project_number, 'us-central1' AS region, 'gestao-de-dados-api' AS service_name, 'gestao-de-dados' AS database_id, 'gestao-de-dados-camarateresopolislgpdweb' AS bucket_name, ['NEOGOV_AUTH_ALLOWED_ISSUERS', 'NEOGOV_AUTH_API_KEY'] AS secret_names),
    STRUCT('cides-lgpdweb' AS project_id, '812458273636' AS project_number, 'us-central1' AS region, 'gestao-de-dados-api' AS service_name, 'gestao-de-dados' AS database_id, 'gestao-de-dados-cides-lgpdweb' AS bucket_name, ['NEOGOV_AUTH_ALLOWED_ISSUERS', 'NEOGOV_AUTH_API_KEY'] AS secret_names),
    STRUCT('cisalp-lgpdweb' AS project_id, '252011168537' AS project_number, 'us-central1' AS region, 'gestao-de-dados-api' AS service_name, 'gestao-de-dados' AS database_id, 'gestao-de-dados-cisalp-lgpdweb' AS bucket_name, ['NEOGOV_AUTH_ALLOWED_ISSUERS', 'NEOGOV_AUTH_API_KEY'] AS secret_names),
    STRUCT('cm-araguari-lgpdweb' AS project_id, '80441081297' AS project_number, 'us-central1' AS region, 'gestao-de-dados-api' AS service_name, 'gestao-de-dados' AS database_id, 'gestao-de-dados-cm-araguari-lgpdweb' AS bucket_name, ['NEOGOV_AUTH_ALLOWED_ISSUERS', 'NEOGOV_AUTH_API_KEY'] AS secret_names),
    STRUCT('cm-campo-florido-lgpdweb' AS project_id, '223688126013' AS project_number, 'us-central1' AS region, 'gestao-de-dados-api' AS service_name, 'gestao-de-dados' AS database_id, 'gestao-de-dados-cm-campo-florido-lgpdweb' AS bucket_name, ['NEOGOV_AUTH_ALLOWED_ISSUERS', 'NEOGOV_AUTH_API_KEY'] AS secret_names),
    STRUCT('frutallgpdweb-3dab8' AS project_id, '722099604113' AS project_number, 'us-central1' AS region, 'gestao-de-dados-api' AS service_name, 'gestao-de-dados' AS database_id, 'gestao-de-dados-frutallgpdweb-3dab8' AS bucket_name, ['NEOGOV_AUTH_ALLOWED_ISSUERS', 'NEOGOV_AUTH_API_KEY'] AS secret_names),
    STRUCT('lgpdweb' AS project_id, '824046366491' AS project_number, 'us-central1' AS region, 'gestao-de-dados-api' AS service_name, 'gestao-de-dados' AS database_id, 'lgpdweb-gestao-de-dados' AS bucket_name, ['neogov-auth-api-key'] AS secret_names),
    STRUCT('lgpdwebsaaeituiutaba' AS project_id, '917044735941' AS project_number, 'us-central1' AS region, 'gestao-de-dados-api' AS service_name, 'gestao-de-dados' AS database_id, 'gestao-de-dados-lgpdwebsaaeituiutaba' AS bucket_name, ['NEOGOV_AUTH_ALLOWED_ISSUERS', 'NEOGOV_AUTH_API_KEY'] AS secret_names),
    STRUCT('pm-estreladosul-mg-lgpdweb' AS project_id, '8425592986' AS project_number, 'us-central1' AS region, 'gestao-de-dados-api' AS service_name, 'gestao-de-dados' AS database_id, 'gestao-de-dados-pm-estreladosul-mg-lgpdweb' AS bucket_name, ['NEOGOV_AUTH_ALLOWED_ISSUERS', 'NEOGOV_AUTH_API_KEY'] AS secret_names),
    STRUCT('pm-machado-lgpdweb' AS project_id, '183509511404' AS project_number, 'us-central1' AS region, 'gestao-de-dados-api' AS service_name, 'gestao-de-dados' AS database_id, 'gestao-de-dados-pm-machado-lgpdweb' AS bucket_name, ['NEOGOV_AUTH_ALLOWED_ISSUERS', 'NEOGOV_AUTH_API_KEY'] AS secret_names),
    STRUCT('pm-montecarmelo-mg-lgpdweb' AS project_id, '932352030577' AS project_number, 'us-central1' AS region, 'gestao-de-dados-api' AS service_name, 'gestao-de-dados' AS database_id, 'gestao-de-dados-pm-montecarmelo-mg-lgpdweb' AS bucket_name, ['NEOGOV_AUTH_ALLOWED_ISSUERS', 'NEOGOV_AUTH_API_KEY'] AS secret_names),
    STRUCT('pm-neogov-qa-lgpdweb' AS project_id, '115635227737' AS project_number, 'us-central1' AS region, 'gestao-de-dados-api' AS service_name, 'gestao-de-dados' AS database_id, 'gestao-de-dados-qa' AS bucket_name, ['NEOGOV_AUTH_ALLOWED_ISSUERS', 'NEOGOV_AUTH_API_KEY'] AS secret_names),
    STRUCT('pm-pedrinopolis-lgpdweb' AS project_id, '374975682507' AS project_number, 'us-central1' AS region, 'gestao-de-dados-api' AS service_name, 'gestao-de-dados' AS database_id, 'gestao-de-dados-pm-pedrinopolis-lgpdweb' AS bucket_name, ['NEOGOV_AUTH_ALLOWED_ISSUERS', 'NEOGOV_AUTH_API_KEY'] AS secret_names),
    STRUCT('pm-tupaciguara-mg-lgpdweb' AS project_id, '316815308630' AS project_number, 'us-central1' AS region, 'gestao-de-dados-api' AS service_name, 'gestao-de-dados' AS database_id, 'gestao-de-dados-pm-tupaciguara-mg-lgpdweb' AS bucket_name, ['NEOGOV_AUTH_ALLOWED_ISSUERS', 'NEOGOV_AUTH_API_KEY'] AS secret_names),
    STRUCT('pmdeltamglgpdweb' AS project_id, '363128949229' AS project_number, 'us-central1' AS region, 'gestao-de-dados-api' AS service_name, 'gestao-de-dados' AS database_id, 'gestao-de-dados-pmdeltamglgpdweb' AS bucket_name, ['NEOGOV_AUTH_ALLOWED_ISSUERS', 'NEOGOV_AUTH_API_KEY'] AS secret_names),
    STRUCT('pmsgalgpdweb-32cf8' AS project_id, '947412222933' AS project_number, 'us-central1' AS region, 'gestao-de-dados-api' AS service_name, 'gestao-de-dados' AS database_id, 'gestao-de-dados-pmsgalgpdweb-32cf8' AS bucket_name, ['NEOGOV_AUTH_ALLOWED_ISSUERS', 'NEOGOV_AUTH_API_KEY'] AS secret_names),
    STRUCT('prefeituraituiutabalgpdweb' AS project_id, '637181059585' AS project_number, 'us-central1' AS region, 'gestao-de-dados-api' AS service_name, 'gestao-de-dados' AS database_id, 'gestao-de-dados-prefeituraituiutabalgpdweb' AS bucket_name, ['NEOGOV_AUTH_ALLOWED_ISSUERS', 'NEOGOV_AUTH_API_KEY'] AS secret_names),
    STRUCT('prefeiturateresopolislgpdweb' AS project_id, '578760838874' AS project_number, 'us-central1' AS region, 'gestao-de-dados-api' AS service_name, 'gestao-de-dados' AS database_id, 'gestao-de-dados-prefeiturateresopolislgpdweb' AS bucket_name, ['NEOGOV_AUTH_ALLOWED_ISSUERS', 'NEOGOV_AUTH_API_KEY'] AS secret_names),
    STRUCT('saosimaolgpdweb-1a6e5' AS project_id, '986593446685' AS project_number, 'us-central1' AS region, 'gestao-de-dados-api' AS service_name, 'gestao-de-dados' AS database_id, 'gestao-de-dados-saosimaolgpdweb-1a6e5' AS bucket_name, ['NEOGOV_AUTH_ALLOWED_ISSUERS', 'NEOGOV_AUTH_API_KEY'] AS secret_names)
  ])
),
base AS (
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
