# Contexto da solicitação

Data de abertura: 2026-11-16T14:20:18.736386-03:00 (America/Sao_Paulo).

## Prompt original

> preciso que crie uma solicitação para validar nas collections do banco modules do proejtos de produção do lgpdwb se há um documento em orgaos com o nome vazio

Esclarecimento de escopo, em resposta à proposta de consultar a lista excluindo QA:

> não precisa incluir neogov-default

## Objetivo e escopo

Validar por consultas somente de leitura se existem documentos com nome vazio em `orgaos`, banco Firestore `modules`, nos 27 projetos abaixo. Excluir `pm-neogov-qa-lgpdweb` e `neogov-default`; incluir `lgpdweb` (apresentação de produção). A seleção decorre da lista local de 09/11/2026 e do esclarecimento do usuário; não representa recatalogação dos ambientes.

- `pm-itaguai-rj-lgpdweb`
- `lgpdweb`
- `camaraconceicaoalagoaslgpdweb`
- `pm-tupaciguara-mg-lgpdweb`
- `pm-pedrinopolis-lgpdweb`
- `frutallgpdweb-3dab8`
- `cm-campo-florido-lgpdweb`
- `prefeiturateresopolislgpdweb`
- `pmsgalgpdweb-32cf8`
- `pmdeltamglgpdweb`
- `prefeituraituiutabalgpdweb`
- `novapontelgpdweb`
- `cm-estrela-do-sul-lgpdweb`
- `pm-estreladosul-mg-lgpdweb`
- `cm-araguari-lgpdweb`
- `pm-machado-lgpdweb`
- `lgpdwebsaaeituiutaba`
- `camarafrutallgpdweb`
- `saosimaolgpdweb-1a6e5`
- `camarateresopolislgpdweb`
- `pm-sao-joao-del-rei-mg`
- `pm-montecarmelo-mg-lgpdweb`
- `cides-lgpdweb`
- `cisalp-lgpdweb`
- `cachoeiradouradamglgpdweb`
- `camaraituiutabalgpdweb-a1a06`
- `pm-coromandel-mg-lgpdweb`

## Critério e incertezas

Confirmar estrutura e campo do nome por leitura delimitada. Diferenciar string exatamente vazia, string composta apenas de espaços, nulo e campo ausente; não confundir essas condições. Não presumir resultado negativo em caso de acesso negado, banco ausente ou consulta incompleta. O catálogo em ativos/ não documenta a coleção orgaos; a referência de modules encontrada refere-se principalmente a user-data e à existência de banco em São João del-Rei.

## Restrições, impactos, verificação e reversão

Usar autenticação existente do gcloud, sem login, troca de conta/configuração ou criação de credenciais. Não modificar GCP, documentos, índices ou APIs. Leituras Firestore podem ter custo; retornar apenas campos de nome e metadados/identificadores necessários. Não salvar segredos ou documentos completos. Confirmar cobertura por projeto, paginação, critérios e caminhos dos achados. A conclusão representa o momento da coleta.

Mudanças locais autorizadas: esta pasta exclusiva com contexto e relatório. Intermediários, se necessários, em diretório temporário exclusivo e restrito, removidos após consolidação. Verificar arquivos finais e limpeza. Reversão local por remoção apenas desta pasta; nenhuma reversão de dados remotos será necessária porque não haverá escrita no GCP. Leituras já consumidas não são reversíveis.

## Contexto inicial de autenticação

Conta configurada: desenvolvimento@neogov.com.br. Projeto padrão: dashboard-admin-481516, fora dos alvos. Região/zona e impersonação não configuradas. Nenhum override CLOUDSDK_/GOOGLE_ identificado. auth list inicialmente falhou por diretório interno do CLI somente leitura no sandbox; verificar com execução permitida sem alterar identidade.

## Confirmação e execução

A conta ativa foi confirmada como desenvolvimento@neogov.com.br com a autenticação existente. A estrutura validada é a coleção raiz orgaos e o campo nome. A coleta foi concluída nos 27 projetos, sem erros; resultados e readTime por projeto constam em relatorio.md.
