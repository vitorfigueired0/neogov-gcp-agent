# Relatório — Gestão de Dados API nos projetos LGPDWeb

Data: **29/10/2026**, fuso `America/Sao_Paulo`.

Resultado: **inventário técnico concluído no escopo acessível; documentação do ativo criada; consultas e proposta de custos preparadas. Valores monetários ainda não apurados. Nenhum recurso GCP criado ou alterado.**

## Escopo, identidade e escolhas do usuário

O pedido foi identificar os projetos LGPDWeb com o Cloud Run `gestao-de-dados-api`, compreender componentes e permissões, copiar o README e documentar o ativo em `ativos/gestao-de-dados-api/`, além de preparar apuração de custos e explicar eventual BigQuery antes de executar.

- Período escolhido durante a execução: **últimos 30 dias**.
- Limite reafirmado pelo usuário: **projetos LGPDWeb e `artefatos`**; não incluir `chequei.faturamento`.
- Autenticação existente: `desenvolvimento@neogov.com.br`; sem impersonação ou overrides de credenciais identificados. Não houve login, troca de identidade, criação de chave ou mudança de defaults.
- Projeto padrão preservado: `dashboard-admin-481516`. Operações de recursos usaram o projeto explicitamente. Região dos serviços encontrados: `us-central1`.
- O README foi tratado como documentação. Não foram executados seus comandos de ADC, deploy, IAM, criação ou migração.

## O que foi encontrado

As 26 listagens de Cloud Run nos projetos com LGPDWeb no nome/ID concluíram sem erro. Foram encontrados **23 serviços com nome exato `gestao-de-dados-api`**, todos em `us-central1`, com `Ready=True` e 100% do tráfego na revisão pronta mais recente no momento das consultas. Isso não comprova funcionamento dos fluxos de negócio.

Não foi encontrado serviço com esse nome em `cm-estrela-do-sul-lgpdweb`, `novapontelgpdweb` e `camaraituiutabalgpdweb`. Não foram inferidas ausências em projetos inacessíveis ou com outros nomes.

O inventário de projetos permaneceu com os mesmos 26 registros do mapeamento local de 20/10/2026. O arquivo preexistente `projetos-lgpdweb.md` não foi modificado.

| Componente | Evidência consolidada |
| --- | --- |
| Cloud Run | 23 serviços, 1 vCPU/1 GiB, porta 8080; 22 com limite configurado de 100 instâncias e `lgpdweb` com limite de 3 |
| Firestore | 23 bancos `gestao-de-dados`, Native/Standard, `us-central1`, todos com os quatro índices esperados `complaints` em READY |
| Backup Firestore | 22 agendas semanais aos domingos com retenção de 98 dias; `lgpdweb` sem agenda. Não foi testada restauração nem comprovada execução de backup |
| Proteção Firestore | PITR e proteção contra exclusão desabilitados nos 23 bancos; `freeTier=false` em todos |
| Storage | 23 buckets configurados, STANDARD/US-CENTRAL1, acesso uniforme e prevenção de acesso público enforced; soft delete de 7 dias |
| Secret Manager | 45 referências de segredo: duas por instalação em 22 projetos usando `latest`; `lgpdweb` referencia somente `neogov-auth-api-key:1` |
| Conta runtime | Conta própria `gestao-de-dados-api-runtime@PROJETO.iam.gserviceaccount.com` em cada projeto |
| Imagens | 22 instalações usam o digest de release `72ab7958…`; QA usa o digest `6e8f065a…`. Todos no repositório central de `artefatos` |
| Domínios | 23 mapeamentos diretos ao serviço, Ready e CertificateProvisioned verdadeiros no estado GCP. TLS externo não foi testado |
| Logs | Buckets locais `_Default` e `_Required`, com retenção consultada de 30 e 400 dias; podem receber outras aplicações do projeto |
| Autenticação central | QA aponta para `api.auth-develop.neogov.com.br`; os outros 22 serviços apontam para `api.auth.neogov.com.br`. Recursos dos projetos da central não foram inspecionados |
| Faturamento | Os 23 projetos e `artefatos` estão vinculados à conta `01017B-9A8236-AA7CA7`, com billing habilitado |

Lista completa com projeto, domínio, bucket e segredo: [inventario.md](../../ativos/gestao-de-dados-api/inventario.md). Detalhes e políticas por instalação: [inventario.json](../../ativos/gestao-de-dados-api/inventario.json).

## Permissões e pontos de atenção

Todas as contas runtime têm concessões de `storage.objectCreator` e `storage.objectViewer` no bucket configurado e `iam.serviceAccountTokenCreator` na própria conta para assinatura de URLs. Os agentes gerenciados Cloud Run dos 23 projetos têm leitura no repositório central. O publicador GitHub possui escrita nesse repositório e sua identidade é compartilhada com outros repositórios autorizados.

22 projetos concedem `datastore.user` sem condição de banco. `lgpdweb` apresenta condição ao banco `gestao-de-dados`, reproduzida na matriz IAM, sem simular sua avaliação. QA tem também `run.editor` e `secretmanager.secretAccessor` no projeto, escopo maior que o necessário descrito no README para uma execução típica. O acesso de QA aos dois segredos é concedido pelo projeto, sem binding local no segredo.

Todos os 23 serviços têm ingresso `all` e checagem IAM de invocação desabilitada. Isso permite entrada HTTP pública independentemente de a política do serviço possuir `allUsers`. A autenticação de aplicação descrita no README não foi testada.

As referências `latest` de 22 instalações diferem da versão numérica recomendada no README. Timeout da central: 20.000 ms em 22 instalações, 5.000 ms em `lgpdweb`; cache CORS de Storage: 3.600 segundos em 22 buckets, 300 em `lgpdweb`. São diferenças de configuração, não falhas funcionais comprovadas. Nenhuma correção foi aplicada.

[Matriz de permissões](../../ativos/gestao-de-dados-api/permissoes.md). A matriz não equivale a auditoria de autorização efetiva: herança organizacional, Deny, grupos e avaliação de condições não foram esgotados.

## Custos: entregue e pendente

Não foi encontrada exportação Cloud Billing nos datasets/tabelas visíveis dos **27 projetos autorizados**: 26 LGPDWeb e `artefatos`; as listagens de datasets tiveram HTTP 200. Não se conclui que a conta inteira não tenha exportação em outro destino.

Entregues:

- [Consulta detalhada dos recursos associados](consultas/custos_detalhados_30_dias.sql), com mapeamento dos 23 serviços, bancos, buckets e segredos, créditos, moeda, SKU e categorias separadas para compartilhados e sem atribuição.
- [Consulta padrão de contexto por projeto](consultas/custos_padrao_30_dias.sql), sem atribuir à API os gastos integrais de projetos que hospedam outras aplicações.
- [Mapa de recursos](consultas/mapeamento-recursos.json).
- [Proposta completa de BigQuery](plano-custos-bigquery.md), com destino, justificativa, alternativas, funcionamento, impactos, controles, verificação e reversão.

Destino proposto, **ainda não criado**: `artefatos.finops_billing`, multirregião `US`. A API BigQuery já está habilitada nesse projeto e o vínculo com a mesma conta Billing foi confirmado. O dataset financeiro seria separado dos dados da aplicação.

Criar um dataset vazio não habilita a coleta. A exportação detalhada inclui todos os projetos da conta de faturamento, sem filtro de origem por API. Isso exige decisão explícita sobre o alcance financeiro, leitores e confirmação de que não substituirá uma exportação existente. A localização US foi proposta considerando a possibilidade documentada de retroatividade na primeira habilitação, com os limites descritos no plano. [Documentação de disponibilidade](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables).

Não foram criados dataset, exportação, views, consultas agendadas ou dashboard. Nenhuma consulta SQL ou dry-run foi executado no BigQuery. Os marcadores de tabela e parâmetros precisam ser preenchidos depois que existir fonte autorizada; identificação real de recursos/SKUs e cobertura devem ser conferidas no primeiro ensaio. Não há total em reais ou outra moeda, e não foi estimado gasto a partir do teto de instâncias.

## Arquivos criados

Em `ativos/gestao-de-dados-api/`, conforme pedido:

| Arquivo | Conteúdo |
| --- | --- |
| [README.md](../../ativos/gestao-de-dados-api/README.md) | Cópia integral do README fornecido; links relativos continuam se referindo aos arquivos do repositório de origem |
| [componentes.md](../../ativos/gestao-de-dados-api/componentes.md) | Arquitetura, dependências, diferenças entre README e implantação, segurança e limites |
| [inventario.md](../../ativos/gestao-de-dados-api/inventario.md) | Tabela das 23 instalações e os três projetos sem o serviço |
| [inventario.json](../../ativos/gestao-de-dados-api/inventario.json) | Metadados e concessões por instalação, sem valores secretos |
| [permissoes.md](../../ativos/gestao-de-dados-api/permissoes.md) | Matriz IAM de projeto, bucket, segredo, conta runtime e repositório central |
| [custos.md](../../ativos/gestao-de-dados-api/custos.md) | Estado da apuração e links para SQL/proposta |

Nesta pasta de solicitação: `contexto.md`, cópia do README, `inventario-consolidado.json`, `comandos.jsonl`, evidências sanitizadas em `evidencias/`, scripts em `scripts/`, SQL/mapa em `consultas/`, plano financeiro e este relatório. Não foram modificados arquivos preexistentes da API nem instruções do projeto.

## Verificações e limitações de coleta

[verificacoes.txt](verificacoes.txt) registra **19 verificações locais aprovadas**: cópia do README, contagem e unicidade, estado/tráfego, 92 índices com campos e ordenações esperados, metadados dos bancos/buckets, concessões de acesso, domínios, faturamento, backups, JSON/Python válidos, mapeamento SQL e links locais.

SHA256 do README copiado: `685fa4997815b41ff82215c55dede6ba3e7ce8023137190f2bb758be3076a8d2`.

A conferência inicial exigia incorretamente binding local em cada segredo e sinalizou QA. A inspeção das políticas mostrou a concessão no projeto; o critério foi corrigido para reconhecer os dois escopos sem afirmar autorização efetiva. A saída inicial foi preservada em `verificacoes-inicial.txt`. Não houve alteração IAM para satisfazer a checagem.

As consultas Compute falharam em QA e `cides-lgpdweb` por API desabilitada; ela não foi ativada. As listagens de NEGs, backends, URL maps e forwarding rules retornaram vazias nos outros 21 projetos. As configurações runtime não apresentam VPC/egress especial. O comando GA de domínios não aceitou `--region`; a consulta foi realizada com sucesso pelo comando beta que oferece essa flag. Nenhuma dessas falhas foi tratada como prova de ausência de recursos inacessíveis.

O sandbox impediu inicialmente o acesso do gcloud ao banco de credenciais. As consultas fora do sandbox usaram a mesma sessão existente, sem criar outra configuração ou identidade.

A busca inicial de metadados BigQuery foi mais ampla que o necessário e incluiu outros projetos acessíveis. Uma consulta direcionada a `chequei.faturamento` foi **rejeitada pela revisão automática de aprovação**, por estar fora do escopo explícito. O usuário recusou incluir esse projeto. A busca em lote já havia terminado quando se tentou suspendê-la; os 236 arquivos de metadados BigQuery de projetos fora do escopo foram removidos localmente e o script foi restringido aos projetos autorizados. Nenhuma linha de dados financeiros fora do escopo foi lida. A lista de vínculos Billing foi filtrada localmente para os projetos autorizados.

Não foram lidos documentos Firestore, objetos de bucket, payloads Secret Manager ou logs de requisições. Não houve testes de login, disponibilidade de endpoints, CORS pelo navegador, assinatura de URLs, carga ou restauração. Os metadados refletem instantes diferentes da coleta e não reconstituem todo o histórico dos últimos 30 dias.

## Reversão

Não há rollback GCP: foram feitas somente consultas de metadados e políticas. Para reverter a documentação local, remover exclusivamente a pasta nova `ativos/gestao-de-dados-api/` e a pasta desta solicitação; a pasta `ativos/` só deve ser removida se permanecer vazia. A remoção perderá os registros desta coleta e não deverá atingir arquivos acrescentados por terceiros depois dela. O README de origem, configurações da aplicação e recursos GCP permanecem intactos.

Uma implantação futura do BigQuery deve seguir o plano: preservar exportações e histórico preexistentes, limitar o rollback à nova configuração e não excluir tabelas financeiras sem retenção/backup aprovado. Custos incorridos e histórico apagado podem não ser reversíveis.
