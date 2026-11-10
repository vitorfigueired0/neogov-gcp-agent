# Contexto

Data: 2026-11-09T15:14:34.740989-03:00

## Prompt recebido

agora, precisoo que para todos, você busque no banco modules, na collection user data os usuários ativos e faça um depara para confirmar se o id do documento coom os dadoos de usuário corresponde a o uuid daquele mesmo usuário. Faça um csv para cada projeto moostrandoa relação e uma coluna que confirma que está igual oou não

## Resumo técnico

Objetivo: consultar usuários ativos no banco Firestore `modules` de cada um dos 29 projetos da lista local e gerar um CSV por projeto com o ID do documento, o identificador do usuário e a confirmação de igualdade.

Escopo: somente leitura remota; criação de artefatos nesta pasta. Preservar identidade e configuração existentes do gcloud. Não registrar tokens, chaves, senhas ou documentos completos.

Pendente: nome exato da coleção (usuário informou “user data”), critério de usuário ativo, campo uuid/uid e se a comparação desejada usa o campo do documento ou o Firebase Authentication. Pergunta enviada ao usuário.

Referências locais: catálogo ativos/ consultado; não foi encontrada documentação do banco modules nem desta coleção. Relação de projetos fornecida pelo usuário em 09/11/2026, sem revalidação prévia no GCP.

## Projetos

- `pm-itaguai-rj-lgpdweb`
- `pm-neogov-qa-lgpdweb`
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
- `neogov-default`
- `cachoeiradouradamglgpdweb`
- `camaraituiutabalgpdweb-a1a06`
- `pm-coromandel-mg-lgpdweb`

## Esclarecimentos do usuário

- Comparação: “uuid do firebase auth x id do doocumento (nãoo campoo) que correspoonde a ele no firestore”.
- Abrangência: “pode trazer todos mas evidêncie quando for um caso desativado”.
- Incluir todos os documentos de user-data, sem filtro de ativos; destacar disabled do Firebase Authentication.
- A correspondência será buscada pelo e-mail (normalizado apenas para comparação); UID do Auth comparado literalmente com ID do documento. Casos não confirmáveis serão sinalizados.

## Contexto de autenticação verificado

Conta ativa e configurada: desenvolvimento@neogov.com.br. Projeto padrão: dashboard-admin-481516. Sem overrides CLOUDSDK_/GOOGLE_APPLICATION_CREDENTIALS, região, zona ou impersonação configurados. Autenticação do gcloud existente; token apenas em memória, sem novos logins. Falha inicial no sandbox ao obter token; consulta de leitura fora do sandbox autorizada pelo mecanismo de aprovação.
