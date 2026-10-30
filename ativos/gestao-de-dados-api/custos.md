# Custos da API e dependências

Período solicitado: **últimos 30 dias**. Ainda não há total monetário apurado: não foi encontrada tabela Cloud Billing nos datasets visíveis dos projetos LGPDWeb e `artefatos`; fontes fora desse escopo foram excluídas conforme orientação do usuário. Ausência de exportação acessível não significa gasto zero.

Foram preparadas uma consulta detalhada que associa Cloud Run, banco, bucket e segredos de cada instalação e uma consulta padrão que mostra somente totais de contexto por projeto/SKU, sem atribuí-los à API. Ambas incluem créditos e preservam a moeda. Não foram executadas ou validadas por dry-run no BigQuery porque falta a tabela-fonte autorizada.

[Proposta de BigQuery, funcionamento, impactos e reversão](../../solicitacoes/2026-10-29-levantamento-gestao-de-dados-api/plano-custos-bigquery.md).

[Consulta detalhada — últimos 30 dias](../../solicitacoes/2026-10-29-levantamento-gestao-de-dados-api/consultas/custos_detalhados_30_dias.sql).

[Consulta padrão — contexto por projeto/SKU](../../solicitacoes/2026-10-29-levantamento-gestao-de-dados-api/consultas/custos_padrao_30_dias.sql).
