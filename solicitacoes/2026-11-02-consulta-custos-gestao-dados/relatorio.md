# Relatório — consulta de custos da Gestão de Dados

## Resultado

Foi localizado e lido o resultado já existente da consulta de custos de 30 dias em `lgpdweb`. O subtotal diretamente classificado como recurso associado à Gestão de Dados é **R$ 5,588863**; o total do recorte é **R$ 278,064089**, mas **R$ 272,475226 (97,99%)** está deliberadamente fora desse subtotal por não possuir vínculo ou rateio confirmado.

O custo associado é dominado por Cloud Run (R$ 2,902018) e Secret Manager (R$ 2,676575). O maior valor do recorte total é Vulnerability Scanning de Container Registry, R$ 140,326044, concentrado em `artefatos`; a consulta o deixa fora da atribuição à Gestão de Dados.

## Ações executadas

1. Consultado o contexto já autenticado do Google Cloud CLI, sem login, troca de configuração ou identidade.
2. Confirmada a existência da tabela de exportação detalhada de Billing no dataset `lgpdweb.finops_billing`.
3. Localizado o job concluído `job_gfpL8VVNiw7a6vvWdVxKVAzaMyx_`, com SQL correspondente à consulta local de custos preservada.
4. Lidos e agregados localmente os resultados materializados do job. Nenhuma nova consulta SQL foi enviada, evitando cobrança duplicada.
5. Produzido o resumo técnico em [evidencias/resumo-resultados.md](evidencias/resumo-resultados.md).

## Verificações e evidências

- O job estava em estado `DONE` e registrou 416.661.140 bytes processados e 417.333.248 bytes faturados.
- A janela retornada foi de 03/10/2026 a 02/11/2026; o dia final pode estar parcial.
- A comparação de semanas completas mostra R$ 64,486217 (26/10–01/11), 6,74% abaixo de R$ 69,146191 (19/10–25/10). Parte da redução é explicada por créditos de Cloud Run em 01/11.
- A evidência consolidada, incluindo limites de atribuição e concentrações, está em [evidencias/resumo-resultados.md](evidencias/resumo-resultados.md).

## Recursos e arquivos afetados

- **GCP:** nenhum recurso foi criado, alterado ou removido. A atividade foi leitura de metadados e de resultado de job já concluído.
- **Arquivos locais criados:** `contexto.md`, este relatório e `evidencias/resumo-resultados.md`, dentro desta pasta de solicitação.

## Pendências e próximos passos recomendados

1. Investigar no projeto `artefatos` a origem do Vulnerability Scanning de 27/10 e decidir se o custo é compartilhado, de outra carga ou se deve entrar em um rateio explícito.
2. Melhorar a identificação dos recursos sem nome e dos vínculos ainda não reconhecidos antes de atribuir os R$ 272,48 restantes à Gestão de Dados.
3. Acompanhar pelo menos mais um ciclo de faturamento: dados de exportação podem ser revisados antes do fechamento da fatura.

## Reversão

Não há reversão GCP, porque nada foi alterado. Os registros locais podem ser removidos somente mediante autorização explícita; sua remoção elimina a trilha de auditoria desta solicitação.
