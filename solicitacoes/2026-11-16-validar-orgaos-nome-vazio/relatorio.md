# Validação de nomes em orgaos — LGPDWeb

Status: concluído em 2026-11-16T14:22:30.298114-03:00 (America/Sao_Paulo).

## Resultado

Consultados os **27 projetos do escopo**, banco Firestore `modules`, coleção raiz `orgaos`: **246 documentos verificados**. Não foi encontrado documento com `nome` vazio (`""`), composto apenas de espaços, nulo ou ausente. Todos os 246 documentos possuem `nome` string com conteúdo após remoção de espaços nas extremidades. Nenhum tipo divergente foi identificado.

Excluídos do escopo: `pm-neogov-qa-lgpdweb` (QA) e `neogov-default` (esclarecimento do usuário). Incluído `lgpdweb`, de apresentação de produção. Nenhum recurso ou documento GCP foi alterado.

## Ações e verificação

- Consultados mapeamento local de 09/11/2026 e referências pertinentes de `ativos/`; não havia documentação específica de `orgaos` no catálogo. A seleção do escopo foi confirmada no chat; não houve atualização do catálogo.
- Identidade ativa confirmada: `desenvolvimento@neogov.com.br`, sem impersonação ou overrides de credenciais identificados. Projeto padrão `dashboard-admin-481516` preservado; todas as URLs da API indicaram explicitamente projeto e banco.
- A consulta inicial `gcloud auth list` no sandbox falhou por restrição de escrita no diretório interno do CLI. A execução com permissão apropriada confirmou a conta existente; nenhum login, troca de identidade ou configuração foi executado.
- Confirmada a existência de `modules` em todos os 27 projetos. Todos os bancos retornaram Firestore Native, edição Standard. A localização consta na tabela.
- Sondagem em `lgpdweb`: leitura de três documentos com projeção `nome`/`name`; o campo observado foi `nome`. A coleta completa posterior projetou apenas `nome`, além dos metadados automáticos do documento, sem exportar documentos completos.
- Para cada projeto, uma consulta `runQuery` de até um documento em `orgaos` obteve o `readTime` do servidor. Em seguida, `listDocuments` percorreu a coleção nesse mesmo instante, com página máxima de 250 e tratamento de `nextPageToken`. Todas as coleções couberam em uma página, sem página pendente ou IDs repetidos.
- Critérios separados: `nome == ""`; string não vazia cujo `.strip()` é vazio; `nullValue`; campo ausente; tipo diferente de string; string preenchida. Não houve achado que exigisse releitura individual.
- Conferidas cobertura exata dos 27 projetos, ausência de erros, conclusão da paginação e igualdade entre soma das classificações e total de documentos.

Coleta principal: 2026-11-16T14:21:52.824130-03:00 a 2026-11-16T14:22:30.298114-03:00. Os snapshots são fixos por projeto, não simultâneos entre projetos.

## Cobertura por projeto

Todos os casos têm zero nomes vazios, só espaços, nulos, ausentes ou de tipo divergente.

| Projeto | Documentos | Localização de modules | Instante de leitura (America/Sao_Paulo) |
| --- | ---: | --- | --- |
| `pm-itaguai-rj-lgpdweb` | 1 | `us-central1` | `2026-11-16T14:21:57.438243-03:00` |
| `lgpdweb` | 16 | `us-central1` | `2026-11-16T14:21:57.259257-03:00` |
| `camaraconceicaoalagoaslgpdweb` | 1 | `us-central1` | `2026-11-16T14:21:55.533846-03:00` |
| `pm-tupaciguara-mg-lgpdweb` | 17 | `us-central1` | `2026-11-16T14:22:00.058774-03:00` |
| `pm-pedrinopolis-lgpdweb` | 14 | `us-central1` | `2026-11-16T14:22:01.116797-03:00` |
| `frutallgpdweb-3dab8` | 16 | `nam5` | `2026-11-16T14:22:01.445040-03:00` |
| `cm-campo-florido-lgpdweb` | 1 | `us-central1` | `2026-11-16T14:22:03.860906-03:00` |
| `prefeiturateresopolislgpdweb` | 28 | `us-central1` | `2026-11-16T14:22:05.103939-03:00` |
| `pmsgalgpdweb-32cf8` | 14 | `us-central1` | `2026-11-16T14:22:06.792135-03:00` |
| `pmdeltamglgpdweb` | 1 | `us-central1` | `2026-11-16T14:22:09.421317-03:00` |
| `prefeituraituiutabalgpdweb` | 15 | `us-central1` | `2026-11-16T14:22:09.419387-03:00` |
| `novapontelgpdweb` | 8 | `us-central1` | `2026-11-16T14:22:10.938868-03:00` |
| `cm-estrela-do-sul-lgpdweb` | 1 | `us-central1` | `2026-11-16T14:22:12.969982-03:00` |
| `pm-estreladosul-mg-lgpdweb` | 20 | `us-central1` | `2026-11-16T14:22:13.129738-03:00` |
| `cm-araguari-lgpdweb` | 1 | `us-central1` | `2026-11-16T14:22:14.454750-03:00` |
| `pm-machado-lgpdweb` | 14 | `us-central1` | `2026-11-16T14:22:16.649961-03:00` |
| `lgpdwebsaaeituiutaba` | 39 | `nam5` | `2026-11-16T14:22:15.967540-03:00` |
| `camarafrutallgpdweb` | 1 | `us-central1` | `2026-11-16T14:22:17.759905-03:00` |
| `saosimaolgpdweb-1a6e5` | 1 | `us-central1` | `2026-11-16T14:22:19.387035-03:00` |
| `camarateresopolislgpdweb` | 1 | `us-central1` | `2026-11-16T14:22:20.723268-03:00` |
| `pm-sao-joao-del-rei-mg` | 16 | `us-central1` | `2026-11-16T14:22:21.541914-03:00` |
| `pm-montecarmelo-mg-lgpdweb` | 1 | `us-central1` | `2026-11-16T14:22:23.657652-03:00` |
| `cides-lgpdweb` | 1 | `us-central1` | `2026-11-16T14:22:24.736588-03:00` |
| `cisalp-lgpdweb` | 15 | `us-central1` | `2026-11-16T14:22:25.709354-03:00` |
| `cachoeiradouradamglgpdweb` | 1 | `us-central1` | `2026-11-16T14:22:27.181240-03:00` |
| `camaraituiutabalgpdweb-a1a06` | 1 | `us-central1` | `2026-11-16T14:22:28.386378-03:00` |
| `pm-coromandel-mg-lgpdweb` | 1 | `us-central1` | `2026-11-16T14:22:29.077045-03:00` |
| **Total** | **246** | | |

## Impactos, arquivos e reversão

As operações remotas foram somente leituras de metadados e documentos. Podem consumir leituras faturáveis do Firestore; custo monetário não foi apurado. Não houve escrita de documentos, criação de índices, alteração de IAM, habilitação de API ou mudança de configuração. O token do CLI foi mantido apenas em memória, sem impressão ou gravação. Os nomes preenchidos não foram incluídos nas entregas.

Arquivos locais entregues: [contexto.md](contexto.md) e este [relatorio.md](relatorio.md). A pasta foi criada exclusivamente para esta solicitação. Os quatro arquivos auxiliares desta execução foram removidos após a conferência dos resultados; a remoção da pasta temporária exclusiva foi verificada. Nenhum auxiliar permanece como entrega.

Não há mudança remota a reverter. A reversão local consiste em remover somente a pasta desta solicitação se o registro deixar de ser necessário. Leituras consumidas e seus eventuais custos não podem ser revertidos.

## Limites e pendências

Sem pendência de acesso ou consulta dentro do escopo. O resultado se refere aos instantes da tabela e não garante o estado após a coleta. Abrange documentos diretos de `orgaos` na raiz de `modules`; não varre outras coleções, subcoleções ou campos de nome alternativos. Não comprova validade semântica dos nomes preenchidos, apenas a existência e o conteúdo do campo `nome` pelos critérios descritos. QA e neogov-default não foram consultados nesta validação.

## Referências técnicas

- [Firestore listDocuments: projeção, paginação e readTime](https://docs.cloud.google.com/firestore/docs/reference/rest/v1/projects.databases.documents/listDocuments).
- [Firestore runQuery: consulta e instante de leitura do servidor](https://docs.cloud.google.com/firestore/docs/reference/rest/v1/projects.databases.documents/runQuery).
