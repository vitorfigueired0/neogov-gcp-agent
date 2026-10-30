# Consulta de custos — referência de uso

Destino: **`lgpdweb.finops_billing`**, multirregião **`US`**, conta Billing `01017B-9A8236-AA7CA7`.

O dataset foi criado em 29/10/2026. O usuário informou depois a ativação da exportação detalhada; a [última verificação registrada](../2026-10-29-validacao-exportacao-billing/relatorio.md) ainda encontrou zero tabelas. Este documento não afirma o estado atual da coleta.

## Consultar

1. Abra o [BigQuery no projeto lgpdweb](https://console.cloud.google.com/bigquery?project=lgpdweb) e use processamento em US.
2. Confirme a existência e o esquema da tabela detalhada. Nome esperado: `lgpdweb.finops_billing.gcp_billing_export_resource_v1_01017B_9A8236_AA7CA7`. O Billing cria essa tabela; não criar uma substituta manualmente.
3. Use a [consulta pronta para o console](consultas/custos_detalhados_30_dias_console.sql), que calcula os últimos 30 dias, ou o [SELECT parametrizado](consultas/custos_detalhados_30_dias.sql), com `@inicio` e `@fim` TIMESTAMP, início inclusivo e fim exclusivo.
4. Antes de executar a leitura, valide a versão parametrizada por dry-run e confira os bytes. O limite inicial proposto é 1 GiB (`maximumBytesBilled=1073741824`); esse valor controla a consulta, não o gasto total do projeto. Consultas podem gerar cobrança.

As consultas contêm o mapeamento dos recursos das 23 instalações da API e de suas dependências centrais, levantado em 29/10/2026. Atualize o mapeamento se os recursos mudarem. Elas somam custo e créditos sem duplicar linhas, preservam moeda e separam recursos associados, compartilhados e valores sem atribuição. Não representam todo o custo do projeto como gasto da API. Nome, esquema e identificadores faturados precisam de validação contra a fonte real. **Esses SQLs ainda não foram executados nem validados por dry-run.**

## Cuidados relevantes

A exportação inclui todos os projetos pagos pela conta. `cookies-api` e a conta Compute padrão têm permissões BigQuery herdadas do projeto; a ACL direta do dataset não elimina esse alcance. Nenhuma permissão foi alterada nesta solicitação.

A primeira carga pode levar horas e o histórico inicial pode levar dias. Dados ausentes ou parciais não significam custo zero. [Disponibilidade da exportação](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables).

Para conferir a configuração da coleta, use [Exportação de faturamento](https://console.cloud.google.com/billing/01017B-9A8236-AA7CA7/export?project=lgpdweb), sem substituir ou desativar destinos existentes inadvertidamente. [Relatório da criação](relatorio.md).
