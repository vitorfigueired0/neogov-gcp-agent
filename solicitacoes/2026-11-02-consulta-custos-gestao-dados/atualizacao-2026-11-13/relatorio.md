# Relatório de custos — atualização de 13/11/2026

> Conservação documental — 13/11/2026: por pedido do usuário, foram mantidos o contexto, o relatório final e as entregas finais. Arquivos auxiliares, evidências separadas, scripts, verificações, diffs e backups locais foram removidos; referências a eles no histórico descrevem a execução original, não arquivos ainda disponíveis. Os resultados não foram reconsultados no GCP durante esta limpeza. Recuperação que dependa dos backups removidos exige outra cópia ou versão disponível no Git.

Revalidação dentro da solicitação de 02/11/2026, conforme correção do usuário. Período: **14/10/2026 00:00 a 13/11/2026 00:00, America/Sao_Paulo**, com fim exclusivo: 30 dias completos, até 12/11. Consulta concluída em 13/11/2026 às 10:33, coleta final às 10:34.

## Resultado

**R$ 13,75 líquidos em recursos classificados como associados à Gestão de Dados.** O total dos projetos no recorte foi **R$ 264,82**, dos quais **R$ 251,07 (94,81%)** permanecem fora do subtotal associado por falta de vínculo ou rateio confirmado. Não interpretar o total dos projetos como custo da API.

| Recorte | Bruto (R$) | Créditos (R$) | Líquido (R$) |
| --- | --- | --- | --- |
| Recursos associados | 14,350527 | -0,602495 | 13,748032 |
| Fora do subtotal associado | 253,328768 | -2,259330 | 251,069438 |
| Total do recorte | 267,679295 | -2,861825 | 264,817470 |

Secret Manager representa 63,22% do subtotal associado: R$ 8,691449. Cloud Run responde por R$ 5,046275 líquidos, após R$ 0,602495 de créditos. Firestore e Storage identificados somam menos de R$ 0,02; isso se limita às linhas reconhecidas pela classificação e não demonstra custo integral desses serviços para a aplicação.

## Composição e valores sem atribuição

| Componente | Líquido (R$) |
| --- | --- |
| artefatos sem vínculo confirmado; não atribuir à API | 125,675581 |
| Sem identificador de recurso; não atribuir à API | 75,101343 |
| Outro recurso ou vínculo ainda não reconhecido; não atribuir à API | 50,292514 |
| Secrets associados | 8,691449 |
| Cloud Run da API | 5,046275 |
| Firestore associado | 0,006661 |
| Bucket associado | 0,003647 |
| Logging do projeto (compartilhado; sem rateio) | 0,000000 |

O SQL não reconheceu linhas do repositório central como custo diretamente associado: o valor total de `artefatos` ficou sem vínculo confirmado. Isso indica limitação de atribuição, não ausência de uso do repositório. A central de autenticação e outros recursos compartilhados não foram rateados.

| Serviço GCP no recorte completo | Líquido (R$) |
| --- | --- |
| Container Registry Vulnerability Scanning | 111,871245 |
| Artifact Registry | 49,798742 |
| Cloud Run | 37,564611 |
| Cloud Storage | 16,651477 |
| Cloud Document AI API | 15,969038 |
| Vertex AI | 13,941669 |
| Secret Manager | 9,150948 |
| Cloud Scheduler | 9,131271 |
| App Engine | 0,674090 |
| Networking | 0,064372 |

Vulnerability Scanning continua sendo o maior serviço do recorte (R$ 111,871245), sem atribuição confirmada à API. Investigar quais imagens/repositórios originam a cobrança antes de propor rateio ou mudanças. Nenhuma configuração de scanning foi alterada.

## Tendência com semanas completas

| Semana completa | Total líquido (R$) | Associado bruto (R$) | Créditos associados (R$) | Associado líquido (R$) |
| --- | --- | --- | --- | --- |
| 2026-10-30 a 2026-11-05 | 49,439036 | 5,466801 | -0,602495 | 4,864306 |
| 2026-11-06 a 2026-11-12 | 41,262280 | 5,449360 | 0,000000 | 5,449360 |

O total líquido recuou **16,54%**. A principal redução foi Vulnerability Scanning: de R$ 20,624084 para R$ 9,518808 (queda de R$ 11,105276). Houve compensações por outros serviços e mudança nos créditos.

O subtotal associado líquido cresceu **12,03%**, enquanto seu valor bruto diminuiu **0,32%**. A diferença decorre da ausência, na última semana, dos R$ 0,602495 de créditos associados presentes na semana anterior. Portanto, o crescimento líquido não demonstra aumento equivalente de consumo. Custo bruto também depende de preços e composição dos SKUs; não foram consultadas métricas de carga.

Na consulta de 02/11, o subtotal associado era R$ 5,588863 e o total R$ 278,064089. Esses valores pertencem à janela móvel de 03/10–02/11, com extremidades parciais. A janela atual é outra e incorpora mais dias posteriores às instalações: não usar a diferença entre os totais como medida isolada de crescimento. A comparação semanal acima utiliza a mesma extração atual e durações iguais.

## Distribuição por projeto

| Projeto | Total do projeto no recorte (R$) | Subtotal associado (R$) |
| --- | --- | --- |
| `artefatos` | 125,675581 | fora da atribuição |
| `camaraituiutabalgpdweb-a1a06` | 36,605873 | 0,591603 |
| `pm-montecarmelo-mg-lgpdweb` | 9,366966 | 0,602237 |
| `prefeiturateresopolislgpdweb` | 7,414871 | 0,519374 |
| `camarateresopolislgpdweb` | 6,732816 | 0,623434 |
| `frutallgpdweb-3dab8` | 5,771570 | 0,523876 |
| `saosimaolgpdweb-1a6e5` | 5,585367 | 0,825844 |
| `cm-araguari-lgpdweb` | 5,579979 | 0,524298 |
| `cisalp-lgpdweb` | 5,480530 | 0,613196 |
| `pm-estreladosul-mg-lgpdweb` | 5,261179 | 0,626186 |
| `lgpdwebsaaeituiutaba` | 5,137163 | 0,611486 |
| `pmdeltamglgpdweb` | 4,960090 | 0,505940 |
| `pm-pedrinopolis-lgpdweb` | 4,208938 | 0,591801 |
| `prefeituraituiutabalgpdweb` | 4,197217 | 0,623630 |
| `camarafrutallgpdweb` | 3,857498 | 0,512370 |
| `cachoeiradouradamglgpdweb` | 3,718803 | 0,494986 |
| `pmsgalgpdweb-32cf8` | 3,714935 | 0,712144 |
| `pm-machado-lgpdweb` | 3,619437 | 0,575456 |
| `pm-neogov-qa-lgpdweb` | 3,267515 | 0,863847 |
| `lgpdweb` | 3,202618 | 0,318962 |
| `camaraconceicaoalagoaslgpdweb` | 3,105818 | 0,580078 |
| `pm-tupaciguara-mg-lgpdweb` | 2,995435 | 0,683575 |
| `cm-campo-florido-lgpdweb` | 2,987282 | 0,677674 |
| `cides-lgpdweb` | 2,369989 | 0,546035 |

Os totais de projeto incluem outros serviços/aplicações. Os valores de cada linha não representam custo exclusivo da Gestão de Dados.

## Fonte, método e verificações

- Fonte: `lgpdweb.finops_billing.gcp_billing_export_resource_v1_01017B_9A8236_AA7CA7`, multirregião `US`. Metadados retornaram HTTP 200, com 3.141.203 linhas e 2.312.228.419 bytes lógicos na tabela inteira no instante consultado; essas quantidades não equivalem ao recorte analisado.
- Sessão existente do gcloud: `desenvolvimento@neogov.com.br`, sem impersonação ou overrides detectados. Defaults preservados; projeto de execução explicitamente `lgpdweb`. O acesso ao arquivo de credenciais inicialmente bloqueado pelo sandbox foi resolvido com execução autorizada fora dele, sem login ou criação de credenciais.
- Job histórico `job_gfpL8VVNiw7a6vvWdVxKVAzaMyx_` lido por GET. Seu SQL corresponde exatamente ao arquivo de consulta para console de 29/10. O inventário de 23 projetos e o CASE de classificação são idênticos aos da consulta atual.
- Ajustes na consulta atual: janela parametrizada de dias completos, inclusão de `_PARTITIONTIME IS NULL` para dados ainda não consolidados em partições e campos de primeiro/último uso e exportação. Sem ampliação de projetos ou rateio.
- Créditos somados em subconsulta por registro, evitando multiplicar custos ao expandir arrays; cálculos SQL e consolidação em decimal. Moeda única BRL. Todas as linhas retornadas têm `cost_type=regular`; não houve custo de imposto/ajuste com outro tipo nesse recorte.
- Job atual: [`codex_custos_gestao_dados_20261113_30dias_v1`](https://console.cloud.google.com/bigquery?project=lgpdweb&j=bq:US:codex_custos_gestao_dados_20261113_30dias_v1&page=queryresults), `DONE`, sem erro, SELECT, cache não utilizado.
- Dry-run: **449.900.149 bytes**; execução: **449.900.149 bytes processados e 450.887.680 bytes faturados (430 MiB)**, abaixo do teto de 1 GiB. Bytes faturados não informam por si só o débito monetário efetivo, pois dependem de preço, franquia e modalidade de cobrança. O custo deste job de 13/11 está fora da janela de uso encerrada antes dele.
- Resultado paginado integralmente: **13.017 linhas agregadas**, em duas páginas, representando **210.543 linhas de faturamento**. Contagem conferida com `totalRows`; os somatórios por projeto, serviço, dia e componente reconciliam com o total, e bruto + créditos = líquido.
- Há registros em cada um dos 30 dias. Primeiro uso: `2026-10-14T00:00:00-03:00`. Maior fim de uso: `2026-11-13T00:00:00-03:00`. Maior `export_time` nas linhas do recorte: `2026-11-13T06:03:06.832796-03:00`. Isso não garante que todos os serviços tenham exportado todas as cobranças.

## Limites e pendências

Esta atualização mantém o escopo da referência: 23 projetos históricos mais `artefatos`, e não os 29 projetos do mapeamento de 09/11 nem a conta Billing inteira. A instalação posterior em `pm-sao-joao-del-rei-mg` não integra o SQL original e está **fora deste levantamento comparável**. Os recursos implantados não foram reinventariados; vínculos usam o mapeamento histórico. Exclusividade continua pendente mesmo para recursos classificados como associados.

A exportação possui dados atuais, mas não foi auditada a configuração de exportação no console Billing. Ausência de linhas ou valores baixos não significa ausência de custo. Atrasos, correções e créditos posteriores podem alterar os totais, que não substituem uma fatura fechada. [Documentação oficial do export detalhado](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage) e [validação e limites de consulta](https://docs.cloud.google.com/bigquery/docs/troubleshoot-queries).

Prioridades: identificar os R$ 251,069438 sem atribuição; esclarecer as cobranças de scanning e Artifact Registry por repositório; incluir novas instalações em levantamento futuro com escopo explícito; acompanhar o custo bruto e os créditos separadamente.

## Arquivos, recursos afetados e reversão

Atualização registrada nesta subpasta, sem criar uma nova solicitação. SQL, parâmetros, scripts e evidências estão preservados; CSV detalhado (auxiliar removido; resultado consolidado neste relatório), consolidado (auxiliar removido; resultado consolidado neste relatório), SQL executado (auxiliar removido; resultado consolidado neste relatório) e parâmetros (auxiliar removido; resultado consolidado neste relatório). O relatório e o contexto originais foram preservados integralmente em backups locais antes de receberem links para a atualização.

No GCP houve leitura de metadados, dry-run e um job SELECT com resultado temporário gerenciado pelo BigQuery. Não houve DDL/DML, criação de dataset, tabela permanente ou view, mudança de IAM, exportação, aplicação ou default do CLI. Nenhum segredo foi lido da aplicação ou gravado; o token do CLI existiu somente em memória. Não foram criados diretórios temporários externos nesta execução.

Para reverter somente a documentação, restaurar `relatorio-anterior-2026-11-02.md` e `contexto-anterior-2026-11-02.md` nos caminhos originais e remover apenas os arquivos desta atualização, se autorizado. Isso apaga a trilha local desta revalidação. O processamento BigQuery já realizado e sua eventual cobrança não podem ser revertidos; não excluir o dataset ou a tabela de Billing para desfazer este relatório.


## Quantidade e custo da tabela Billing — complemento de 13/11/2026

Pedido adicional do usuário:

> nãoo precisa criar solicitacao
> essa tabela do BQ está com quantos registros? e isso etsá representando quanto de custo na conta de faturamento?
> se for muitoo, conseguimos zerar ela?

Nenhuma nova solicitação criada. Consulta adicional de metadados em 13/11/2026 às 10:52 (America/Sao_Paulo), e leitura do faturamento BigQuery já exportado até a coleta. Identidade gcloud existente mantida, projeto lgpdweb/US explícito.

| Medida | Resultado |
| --- | --- |
| Registros persistidos, conforme metadados | **3.141.203** |
| Bytes lógicos | **2.312.228.419 bytes = 2,15 GiB (2,31 GB)** |
| Bytes físicos atuais, informativos | 55.014.067 bytes; não confundir com o tamanho lógico faturável |
| Armazenamento do dataset finops_billing em 14/10–12/11 | **R$ 0,000000** |
| Consultas BigQuery de todo o projeto lgpdweb em 14/10–12/11 | **R$ 0,000000** |
| Todo o BigQuery do projeto lgpdweb em 14/10–12/11 | **R$ 0,000002**, valor residual de outro dataset |
| Todo o BigQuery da conta Billing em 14/10–12/11 | **R$ 31,056695** |
| BigQuery nos demais projetos, agregados | **R$ 31,056693** |

A cobrança de armazenamento vem identificada por dataset, não por tabela. Há uso de armazenamento ativo de finops_billing com custo zero; como este dataset contém somente a tabela detalhada conforme a lista de tabelas da mesma manhã, a evidência não mostra cobrança de armazenamento desta tabela nesse período. As consultas são cobradas no projeto do job; os R$ 0,00 acima abrangem todas as consultas de lgpdweb, sem afirmar que todas consultaram Billing ou que não houve leitura dessa tabela cobrada em outro projeto.

Os R$ 31,06 da conta inteira vêm principalmente de **Long-Term Physical Storage (us-east1), R$ 17,568081**, e **Long Term Logical Storage, R$ 13,474857**, em outros projetos. Streaming Insert (us-central1) soma R$ 0,013755. Os nomes desses outros projetos não foram expostos nem foram consultados seus recursos. Esse valor é do serviço BigQuery, não o total de todos os serviços da conta. Apagar finops_billing não elimina cobranças desses outros armazenamentos.

A tabela atual tem apenas armazenamento lógico ativo, sem bytes lógicos de longo prazo. O dataset não retornou storageBillingModel explícito; o padrão documentado é LOGICAL. A tarifa pública de referência é US$ 0,000031507/GiB-hora: mantendo 2,15 GiB constantes por 730 horas, seriam aproximadamente **US$ 0,05/mês antes da franquia**, usando essa tarifa. Há franquia de 10 GiB/mês de armazenamento, compartilhada no âmbito de cobrança aplicável; não se pode tratar como 10 GiB adicionais exclusivos desta tabela. A estimativa é em USD, não uma conversão nem proposta comercial em BRL. O dado decisivo é o custo zero observado no export. [Preços oficiais](https://cloud.google.com/bigquery/pricing) e [modelo de armazenamento](https://docs.cloud.google.com/bigquery/docs/storage_overview#storage_billing_models).

**É tecnicamente possível esvaziar, mas não recomendo apagar agora: não foi identificado gasto relevante desta tabela. Nenhuma exclusão foi executada.** Esvaziar removeria o histórico usado nas análises e não cancelaria cobranças já incorridas, nem pararia a exportação de registros futuros. O Google informa que registros exportados apagados não podem ser preenchidos novamente pelo export; a retenção local de time travel (168 horas) não deve ser tratada como backup permanente ou plano de recuperação testado. Não foi criado snapshot ou backup integral da tabela; os relatórios e agregações locais não permitem reconstruir todos os registros. [Limite de recuperação do export](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables).

Se houver necessidade futura de reduzir retenção, definir primeiro qual histórico pode ser descartado e como conservar o necessário. A frase condicional sobre zerar não foi interpretada como ordem de exclusão, pois a condição de custo elevado não se confirmou. Qualquer exclusão futura requer escopo e autorização explícitos antes da ação destrutiva.

Verificação: job `codex_custo_tabela_billing_20261113_v1` em DONE, sem erro, SELECT. Dry-run e execução processaram **322.938.179 bytes**, com **322.961.408 bytes faturados (308 MiB)**, abaixo de 1 GiB; 322 linhas agregadas recebidas integralmente. Custo e créditos reconciliados. Essas estatísticas de bytes não provam débito monetário do job atual. A maior data de uso exportada para BigQuery é 12/11: as consultas realizadas em 13/11 ainda podem não estar refletidas; os valores são provisórios e podem receber correções.

Evidências: metadados atuais (auxiliar removido; resultado consolidado neste relatório), consolidado e verificações (auxiliar removido; resultado consolidado neste relatório), linhas financeiras agregadas (auxiliar removido; resultado consolidado neste relatório), job (auxiliar removido; resultado consolidado neste relatório), SQL (auxiliar removido; resultado consolidado neste relatório). Nenhum recurso GCP persistente foi alterado: apenas leituras, dry-run e um SELECT com resultado temporário gerenciado pelo BigQuery. Nenhum temporário externo criado. Para reverter a documentação, remover somente este complemento e os arquivos novos correspondentes, se autorizado; isso elimina suas evidências. O processamento já realizado e eventual cobrança não têm reversão.
