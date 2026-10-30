-- GoogleSQL. Somente CONTEXTO POR PROJETO, não é custo isolado da API.
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
  AND b.project.id IN ('cachoeiradouradamglgpdweb', 'camaraconceicaoalagoaslgpdweb', 'camarafrutallgpdweb', 'camaraituiutabalgpdweb-a1a06', 'camarateresopolislgpdweb', 'cides-lgpdweb', 'cisalp-lgpdweb', 'cm-araguari-lgpdweb', 'cm-campo-florido-lgpdweb', 'frutallgpdweb-3dab8', 'lgpdweb', 'lgpdwebsaaeituiutaba', 'pm-estreladosul-mg-lgpdweb', 'pm-machado-lgpdweb', 'pm-montecarmelo-mg-lgpdweb', 'pm-neogov-qa-lgpdweb', 'pm-pedrinopolis-lgpdweb', 'pm-tupaciguara-mg-lgpdweb', 'pmdeltamglgpdweb', 'pmsgalgpdweb-32cf8', 'prefeituraituiutabalgpdweb', 'prefeiturateresopolislgpdweb', 'saosimaolgpdweb-1a6e5', 'artefatos')
GROUP BY project_id, dia_uso, mes_fatura, moeda, servico_gcp, sku_id, sku, tipo_custo
ORDER BY project_id, dia_uso, servico_gcp, custo_liquido DESC;
