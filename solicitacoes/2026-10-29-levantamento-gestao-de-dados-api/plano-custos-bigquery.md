# Proposta de apuração de custos — últimos 30 dias

Status: **preparada, sem criação de recursos GCP e sem execução de consultas SQL**. O inventário técnico foi concluído; a apuração monetária depende de uma fonte de faturamento autorizada.

## Problema e evidências

Foram localizados 23 serviços `gestao-de-dados-api`, cada um com Firestore, bucket e segredos associados. O projeto `artefatos` fornece as imagens usadas por todos. Os 23 projetos e `artefatos` possuem faturamento habilitado e vínculo com a conta `01017B-9A8236-AA7CA7`.

Nos datasets/tabelas visíveis dos 26 projetos LGPDWeb e de `artefatos`, não foi encontrada tabela padrão ou detalhada de Cloud Billing. Isso não demonstra que a conta não possua exportação em outro lugar. O usuário restringiu expressamente o escopo aos projetos LGPDWeb e a `artefatos`; fontes fora desse escopo não serão usadas. O valor dos últimos 30 dias **não foi apurado**; falta de fonte não equivale a custo zero.

Configurações e métricas de consumo, sozinhas, não permitem reproduzir a fatura: faltam preços contratados, créditos, descontos, ajustes, franquias compartilhadas e condições de cobrança. Por isso, a proposta usa dados reais do Cloud Billing, não uma multiplicação de preços públicos pela configuração máxima.

## Abordagens e recomendação

| Alternativa | Entrega | Limite / decisão |
| --- | --- | --- |
| Relatório do console Billing com filtros e CSV | Histórico acessível sem dataset novo | Requer exportação manual; custo por projeto/SKU pode misturar aplicações e bancos. É a opção para uma apuração pontual sem nova exportação |
| Fonte detalhada já existente no escopo autorizado | Permite consulta por recurso e análise recorrente | Preferível quando disponível; não foi encontrada nos projetos autorizados |
| Nova exportação detalhada em `artefatos` | Permite apuração recorrente e identificação de recursos quando o Billing os informa | Recomendada para monitoramento contínuo, **condicionada à autorização sobre a conta inteira e à confirmação de que não substituirá exportação existente** |

A escolha definitiva sobre criar a exportação ainda não foi feita pelo usuário. A autorização inicial admitiu BigQuery, exigindo explicação prévia; esta proposta concretiza destino, funcionamento e impactos. A restrição posterior de escopo impede presumir autorização para exportar dados de todos os projetos da conta de faturamento.

## Onde ficaria e por quê

Destino proposto: **projeto `artefatos`, dataset `finops_billing`, localização multirregional `US`**. Esse dataset ainda não existe no inventário coletado; nenhuma criação foi executada.

`artefatos` já é um projeto central dentro do escopo autorizado, possui a API BigQuery habilitada e está ligado à mesma conta de faturamento dos clientes. Centralizar evita um dataset por cliente e não exige alterar as APIs, suas identidades ou o banco de dados da aplicação. O dataset armazena registros financeiros, sem copiar documentos Firestore ou arquivos dos buckets.

A localização `US` é uma proposta para o dataset financeiro, distinta de `us-central1`. O Google documenta retroatividade do mês atual e anterior para a primeira habilitação de exportação em multirregião US/EU; regiões isoladas começam na habilitação. Isso pode cobrir os 30 dias pedidos, mas depende do histórico de habilitação da exportação. Não é garantia de recuperação integral. Se houver exigência de residência específica, essa escolha deve ser revista antes da criação. [Disponibilidade e limites do export](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables).

Um projeto exclusivo de FinOps seria uma alternativa organizacional futura. Não está proposto criar outro projeto nesta solicitação.

## Como funciona

1. Um dataset é um contêiner de tabelas. **Criá-lo sozinho não coleta faturamento.**
2. Um administrador configura a exportação **detalhada** da conta `01017B-9A8236-AA7CA7` para o dataset. O Billing cria a tabela `gcp_billing_export_resource_v1_01017B_9A8236_AA7CA7`; confirmar o nome efetivo quando surgir.
3. A exportação abrange **todos os projetos pagos por essa conta**, sem filtro por aplicação na origem. Somente as consultas e as permissões de leitura podem limitar o relatório da Gestão de Dados.
4. A conta gerenciada `billing-export-bigquery@system.gserviceaccount.com` precisa das permissões do mecanismo de exportação no dataset. Não é necessário conceder esse acesso às contas runtime da API. Há requisitos próprios de acesso à conta Billing e ao BigQuery. [Configuração da exportação](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-setup).
5. A consulta preparada relaciona os IDs dos recursos inventariados às linhas de faturamento e soma custo bruto e créditos, preservando moeda, SKU e tipo de custo. O relatório não exige agendamento nem dashboard neste primeiro momento.

Não se deve trocar o destino de uma exportação existente sem avaliar consumidores e histórico. Caso já exista exportação detalhada fora do escopo autorizado, manter esse destino e interromper a configuração proposta. É possível entregar CSV filtrado pelo responsável, sem consultar diretamente o outro projeto.

## Consulta preparada e interpretação

- [custos_detalhados_30_dias.sql](consultas/custos_detalhados_30_dias.sql): mapeamento explícito dos 23 projetos, serviço, banco, bucket e segredos; categorias de recursos associados, repositório central compartilhado, logging compartilhado e valores sem atribuição confirmada.
- [mapeamento-recursos.json](consultas/mapeamento-recursos.json): relação legível por máquina usada na consulta.
- [custos_padrao_30_dias.sql](consultas/custos_padrao_30_dias.sql): alternativa se o responsável fornecer exportação padrão. Produz **contexto por projeto/SKU**, sem afirmar que esses totais pertencem à API.

Ambas são consultas SELECT. Não criam tabelas, views, permissões ou jobs agendados. O marcador de tabela deve ser substituído pelo nome efetivo da fonte autorizada. Parâmetros `@inicio` e `@fim` são TIMESTAMP, início inclusivo e fim exclusivo, separados por 30 dias. A apresentação de dias usa `America/Sao_Paulo`. Para um relatório fechado, registrar os dois instantes e reutilizá-los na comparação posterior; a consulta não assume que o mês de uso seja o mês da fatura.

O custo líquido é `cost + SUM(credits.amount)` por linha. Os créditos normalmente têm sinal negativo. A subconsulta de créditos evita multiplicar o custo quando há vários créditos na mesma linha. Não somar exportações padrão e detalhada nem misturar moedas. Categorias de ajuste e impostos permanecem explícitas quando vinculadas aos projetos filtrados; itens da conta sem projeto não são distribuídos automaticamente. Este relatório representa consumo e créditos dos recursos, não reconciliação completa da fatura da conta.

Há granularidade documentada para Cloud Run, Storage, Firestore/Datastore e Secret Manager, mas identificadores podem faltar em algumas linhas. Firestore/Datastore pode aparecer sob `service.description = 'App Engine'`; a consulta considera essa representação. [Granularidade por serviço](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage).

O mapeamento é baseado nas configurações atuais, incluindo as revisões ainda existentes consultadas. Não reconstitui recursos removidos ou alterações históricas não preservadas. Recursos antigos sem correspondência devem ser investigados antes de classificar seu custo.

## Recursos compartilhados e cobertura

| Componente | Tratamento proposto |
| --- | --- |
| Cloud Run `gestao-de-dados-api` | Associar por identificador do serviço ou label de sistema reconhecida; não somar outros serviços do projeto |
| Firestore `gestao-de-dados` | Associar pelo banco, incluindo SKUs reconhecidos de operações, armazenamento e backups; validar os identificadores de backup quando houver cobrança |
| Bucket configurado | Associar pelo nome exato; o relatório mede o bucket, não garante que todo acesso foi feito pela API |
| Segredos configurados | Associar por nome; conferir versões ativas e operações, sem ler o payload |
| Artifact Registry e análise de imagens | Compartilhados entre instalações; se não houver identificador do repositório na linha, manter sem atribuição. Não atribuir todo `artefatos` à API |
| Cloud Logging | `_Default` recebe outras aplicações; mostrar como compartilhado, fora do subtotal associado, até haver critério medido |
| neogov-auth | Dependência configurada, mas projetos da central estão fora do escopo de leitura. Não apurar nem inventar rateio |
| DNS, TLS, balanceadores, rede e tráfego | Mapeamentos diretos confirmados; nenhum balanceador vinculado foi encontrado. Eventuais cobranças sem associação permanecem separadas |
| BigQuery financeiro | Custo operacional novo do relatório, não do runtime da API; reportar separadamente |

Não há um total único honesto para os componentes compartilhados sem decidir um critério de rateio. O primeiro relatório deve mostrar o subtotal dos recursos associados e os custos compartilhados ou não atribuídos em colunas separadas. Nenhum rateio uniforme ou percentual foi inventado.

## Impactos negativos e controles

- **Cobrança adicional:** armazenamento da exportação e processamento das consultas no BigQuery. Não há estimativa monetária sem volume e bytes de leitura. Um dataset vazio não produz a coleta; armazenar dados e consultá-los pode cobrar.
- **Exposição de dados financeiros:** a tabela bruta inclui projetos fora do inventário. O dataset deve ter acesso explícito e restrito; inspecionar também IAM herdado do projeto. Não publicar a tabela nem conceder leitura às contas da aplicação. Relatórios compartilhados devem conter apenas os projetos/recursos autorizados.
- **Residência e retenção:** `US` armazena metadados financeiros nos EUA. Não definir expiração automática da exportação bruta sem política aprovada, pois expiração pode apagar histórico recuperável apenas de cópias existentes.
- **Histórico e integrações:** mudar destino pode interromper consumidores e não migra histórico automaticamente. Não tocar em exportações existentes sem autorização específica.
- **Latência:** a chegada dos registros não é em tempo real e não tem garantia de entrega imediata. Zero linhas recentes não prova ausência de consumo.
- **Serviços da aplicação:** esta proposta não altera Cloud Run, IAM runtime, Secret Manager, Firestore, Storage, domínio ou tráfego.

## Verificação antes e depois de eventual implantação

Antes: confirmar a exportação detalhada atual no console Billing com o responsável; verificar se o tipo já tem destino; confirmar autorização para exportar a conta inteira, localização US, leitores, IAM herdado e retenção. As APIs necessárias já foram consultadas; não habilitar outras automaticamente.

Depois de criação autorizada: consultar metadados do dataset e conferir projeto, US, ACL e ausência de expiração indevida. Verificar tabela criada pelo Billing, esquema e período coberto; aguardar dados sem declarar sucesso antecipado. Executar dry-run da consulta para validar nomes de campos, suporte a `_PARTITIONTIME` e estimar bytes; impor `maximumBytesBilled` de **1 GiB no primeiro ensaio** como limite proposto, não como custo estimado. Se a estimativa ultrapassar, reduzir o período ou apresentar o novo limite antes da execução.

Na primeira consulta real: filtrar um dia e um projeto; conferir identificadores reais e SKUs; ajustar mapeamento se necessário. Depois usar os 30 dias. Conferir créditos e moeda, analisar categorias sem atribuição e comparar com relatório Billing equivalente com mesma janela/filtros. Guardar a saída agregada nesta pasta, sem dados de outras aplicações. Não declarar cobertura completa enquanto existirem componentes sem identificação ou rateio.

## Reversão e limites

Sem implantação, a reversão atual é apenas remover os novos documentos/SQL locais. Caso o projeto avance, o rollback de configuração consiste em interromper **somente a nova exportação** e remover **somente os novos relatórios/views**. Não desabilitar uma exportação preexistente. Preservar dados financeiros até confirmar sua retenção ou backup.

Apagar o dataset ou deixar tabelas expirarem pode perder histórico que o Billing não repõe. Armazenamento já usado, consultas realizadas e exposição já ocorrida não são desfeitos. Não incluir comandos de exclusão na automação inicial.

## Decisão necessária

Autorizar ou recusar, de forma separada: **criar `artefatos.finops_billing` em `US` e configurar uma nova exportação detalhada que inclui toda a conta de faturamento**, somente se ela não substituir uma exportação existente. Alternativa: receber do responsável um CSV financeiro já filtrado ou uma fonte detalhada dentro do escopo permitido. Não foi pedida nova autorização para o projeto `chequei`, cuja inclusão o usuário recusou.
