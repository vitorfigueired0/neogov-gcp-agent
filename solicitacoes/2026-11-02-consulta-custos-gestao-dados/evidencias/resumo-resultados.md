# Evidências — consulta de custos de Gestão de Dados

## Fonte e execução localizada

- Projeto de cobrança da consulta: `lgpdweb`.
- Fonte confirmada: `lgpdweb.finops_billing.gcp_billing_export_resource_v1_01017B_9A8236_AA7CA7` (particionada por dia; localização `US`).
- Job de consulta localizado: `job_gfpL8VVNiw7a6vvWdVxKVAzaMyx_`, concluído em **2026-11-02 11:24:53 -03**.
- SQL: corresponde ao SQL detalhado de 30 dias preservado em `solicitacoes/2026-10-29-custos-gestao-dados-lgpdweb/consultas/custos_detalhados_30_dias_console.sql`.
- Processamento registrado pelo job: **416.661.140 bytes**; bytes faturados: **417.333.248 bytes** (398 MiB). Nenhum novo job SQL foi enviado nesta solicitação; foram lidos os resultados já materializados.

## Cobertura e consolidação

- Janela de uso retornada: **2026-10-03 a 2026-11-02**. As extremidades podem ser parciais, pois o job foi executado durante 02/11.
- Linhas agregadas retornadas: 10.547; linhas de faturamento representadas: 187.090.
- Moeda: BRL.
- Custo bruto: **R$ 278,937617**.
- Créditos: **-R$ 0,873528**.
- Custo líquido: **R$ 278,064089**.

## Classificação da consulta

| Classificação | Custo líquido (BRL) | Observação |
| --- | ---: | --- |
| Recursos associados à Gestão de Dados | 5,588863 | Exclusividade dos recursos ainda requer validação. |
| Fora do subtotal associado; requer análise/rateio | 272,475226 | Não atribuir automaticamente à API. |

Detalhamento do subtotal associado: Cloud Run da API R$ 2,902018; Secrets associados R$ 2,676575; Firestore associado R$ 0,006828; Bucket associado R$ 0,003442.

## Concentrações e tendência

- Maiores componentes fora do subtotal: `artefatos` sem vínculo confirmado R$ 154,264355; itens sem identificador de recurso R$ 67,038652; outros vínculos não reconhecidos R$ 51,172219.
- Maiores serviços no recorte: Container Registry Vulnerability Scanning R$ 140,326044; Artifact Registry R$ 45,384295; Cloud Run R$ 37,573194; Cloud Document AI API R$ 16,529509; Vertex AI R$ 14,597890.
- Maiores projetos por custo líquido: `artefatos` R$ 154,264355; `camaraituiutabalgpdweb-a1a06` R$ 36,159144; `pm-montecarmelo-mg-lgpdweb` R$ 8,659770; `prefeiturateresopolislgpdweb` R$ 6,827788.
- Em 27/10 houve o pico diário de R$ 31,053914, dos quais R$ 26,214756 foram Container Registry Vulnerability Scanning no projeto `artefatos`.
- Sete dias completos de 26/10 a 01/11: R$ 64,486217 líquidos, contra R$ 69,146191 de 19/10 a 25/10: redução de 6,74%. A comparação inclui créditos; o crédito de Cloud Run em 01/11 foi R$ 0,609039.

## Limites da evidência

- Exportações de Billing podem ter atraso e ajustes posteriores; os valores não substituem a fatura fechada.
- A consulta separa o subtotal diretamente associado da parcela compartilhada/não identificada; portanto, R$ 278,06 não é automaticamente custo da API de Gestão de Dados.
- Não foram modificados recursos GCP, dados, IAM ou configurações.
