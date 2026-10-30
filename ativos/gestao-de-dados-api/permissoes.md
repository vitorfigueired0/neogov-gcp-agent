# Permissões da API

Data: 2026-10-29T22:27:52.197786-03:00. Principal de execução de cada linha: `serviceAccount:gestao-de-dados-api-runtime@PROJETO.iam.gserviceaccount.com`.

| Projeto | Concessões no projeto | Concessões no bucket configurado | Concessões na própria conta |
| --- | --- | --- | --- |
| `cachoeiradouradamglgpdweb` | `roles/datastore.user` | `roles/storage.objectCreator`; `roles/storage.objectViewer` | `roles/iam.serviceAccountTokenCreator` |
| `camaraconceicaoalagoaslgpdweb` | `roles/datastore.user` | `roles/storage.objectCreator`; `roles/storage.objectViewer` | `roles/iam.serviceAccountTokenCreator` |
| `camarafrutallgpdweb` | `roles/datastore.user` | `roles/storage.objectCreator`; `roles/storage.objectViewer` | `roles/iam.serviceAccountTokenCreator` |
| `camaraituiutabalgpdweb-a1a06` | `roles/datastore.user` | `roles/storage.objectCreator`; `roles/storage.objectViewer` | `roles/iam.serviceAccountTokenCreator` |
| `camarateresopolislgpdweb` | `roles/datastore.user` | `roles/storage.objectCreator`; `roles/storage.objectViewer` | `roles/iam.serviceAccountTokenCreator` |
| `cides-lgpdweb` | `roles/datastore.user` | `roles/storage.objectCreator`; `roles/storage.objectViewer` | `roles/iam.serviceAccountTokenCreator` |
| `cisalp-lgpdweb` | `roles/datastore.user` | `roles/storage.objectCreator`; `roles/storage.objectViewer` | `roles/iam.serviceAccountTokenCreator` |
| `cm-araguari-lgpdweb` | `roles/datastore.user` | `roles/storage.objectCreator`; `roles/storage.objectViewer` | `roles/iam.serviceAccountTokenCreator` |
| `cm-campo-florido-lgpdweb` | `roles/datastore.user` | `roles/storage.objectCreator`; `roles/storage.objectViewer` | `roles/iam.serviceAccountTokenCreator` |
| `frutallgpdweb-3dab8` | `roles/datastore.user` | `roles/storage.objectCreator`; `roles/storage.objectViewer` | `roles/iam.serviceAccountTokenCreator` |
| `lgpdweb` | `roles/datastore.user` — condição: `resource.name=="projects/lgpdweb/databases/gestao-de-dados"` | `roles/storage.objectCreator`; `roles/storage.objectViewer` | `roles/iam.serviceAccountTokenCreator` |
| `lgpdwebsaaeituiutaba` | `roles/datastore.user` | `roles/storage.objectCreator`; `roles/storage.objectViewer` | `roles/iam.serviceAccountTokenCreator` |
| `pm-estreladosul-mg-lgpdweb` | `roles/datastore.user` | `roles/storage.objectCreator`; `roles/storage.objectViewer` | `roles/iam.serviceAccountTokenCreator` |
| `pm-machado-lgpdweb` | `roles/datastore.user` | `roles/storage.objectCreator`; `roles/storage.objectViewer` | `roles/iam.serviceAccountTokenCreator` |
| `pm-montecarmelo-mg-lgpdweb` | `roles/datastore.user` | `roles/storage.objectCreator`; `roles/storage.objectViewer` | `roles/iam.serviceAccountTokenCreator` |
| `pm-neogov-qa-lgpdweb` | `roles/datastore.user`; `roles/run.editor`; `roles/secretmanager.secretAccessor` | `roles/storage.objectCreator`; `roles/storage.objectViewer` | `roles/iam.serviceAccountTokenCreator`; `roles/iam.serviceAccountUser` |
| `pm-pedrinopolis-lgpdweb` | `roles/datastore.user` | `roles/storage.objectCreator`; `roles/storage.objectViewer` | `roles/iam.serviceAccountTokenCreator` |
| `pm-tupaciguara-mg-lgpdweb` | `roles/datastore.user` | `roles/storage.objectCreator`; `roles/storage.objectViewer` | `roles/iam.serviceAccountTokenCreator` |
| `pmdeltamglgpdweb` | `roles/datastore.user` | `roles/storage.objectCreator`; `roles/storage.objectViewer` | `roles/iam.serviceAccountTokenCreator` |
| `pmsgalgpdweb-32cf8` | `roles/datastore.user` | `roles/storage.objectCreator`; `roles/storage.objectViewer` | `roles/iam.serviceAccountTokenCreator` |
| `prefeituraituiutabalgpdweb` | `roles/datastore.user` | `roles/storage.objectCreator`; `roles/storage.objectViewer` | `roles/iam.serviceAccountTokenCreator` |
| `prefeiturateresopolislgpdweb` | `roles/datastore.user` | `roles/storage.objectCreator`; `roles/storage.objectViewer` | `roles/iam.serviceAccountTokenCreator` |
| `saosimaolgpdweb-1a6e5` | `roles/datastore.user` | `roles/storage.objectCreator`; `roles/storage.objectViewer` | `roles/iam.serviceAccountTokenCreator` |

## Secrets referenciados

| Projeto | Secret:versão | Variável | Concessão local à runtime |
| --- | --- | --- | --- |
| `cachoeiradouradamglgpdweb` | `NEOGOV_AUTH_API_KEY:latest` | NEOGOV_AUTH_API_KEY | `roles/secretmanager.secretAccessor` |
| `cachoeiradouradamglgpdweb` | `NEOGOV_AUTH_ALLOWED_ISSUERS:latest` | NEOGOV_AUTH_ALLOWED_ISSUERS | `roles/secretmanager.secretAccessor` |
| `camaraconceicaoalagoaslgpdweb` | `NEOGOV_AUTH_API_KEY:latest` | NEOGOV_AUTH_API_KEY | `roles/secretmanager.secretAccessor` |
| `camaraconceicaoalagoaslgpdweb` | `NEOGOV_AUTH_ALLOWED_ISSUERS:latest` | NEOGOV_AUTH_ALLOWED_ISSUERS | `roles/secretmanager.secretAccessor` |
| `camarafrutallgpdweb` | `NEOGOV_AUTH_API_KEY:latest` | NEOGOV_AUTH_API_KEY | `roles/secretmanager.secretAccessor` |
| `camarafrutallgpdweb` | `NEOGOV_AUTH_ALLOWED_ISSUERS:latest` | NEOGOV_AUTH_ALLOWED_ISSUERS | `roles/secretmanager.secretAccessor` |
| `camaraituiutabalgpdweb-a1a06` | `NEOGOV_AUTH_API_KEY:latest` | NEOGOV_AUTH_API_KEY | `roles/secretmanager.secretAccessor` |
| `camaraituiutabalgpdweb-a1a06` | `NEOGOV_AUTH_ALLOWED_ISSUERS:latest` | NEOGOV_AUTH_ALLOWED_ISSUERS | `roles/secretmanager.secretAccessor` |
| `camarateresopolislgpdweb` | `NEOGOV_AUTH_API_KEY:latest` | NEOGOV_AUTH_API_KEY | `roles/secretmanager.secretAccessor` |
| `camarateresopolislgpdweb` | `NEOGOV_AUTH_ALLOWED_ISSUERS:latest` | NEOGOV_AUTH_ALLOWED_ISSUERS | `roles/secretmanager.secretAccessor` |
| `cides-lgpdweb` | `NEOGOV_AUTH_API_KEY:latest` | NEOGOV_AUTH_API_KEY | `roles/secretmanager.secretAccessor` |
| `cides-lgpdweb` | `NEOGOV_AUTH_ALLOWED_ISSUERS:latest` | NEOGOV_AUTH_ALLOWED_ISSUERS | `roles/secretmanager.secretAccessor` |
| `cisalp-lgpdweb` | `NEOGOV_AUTH_API_KEY:latest` | NEOGOV_AUTH_API_KEY | `roles/secretmanager.secretAccessor` |
| `cisalp-lgpdweb` | `NEOGOV_AUTH_ALLOWED_ISSUERS:latest` | NEOGOV_AUTH_ALLOWED_ISSUERS | `roles/secretmanager.secretAccessor` |
| `cm-araguari-lgpdweb` | `NEOGOV_AUTH_API_KEY:latest` | NEOGOV_AUTH_API_KEY | `roles/secretmanager.secretAccessor` |
| `cm-araguari-lgpdweb` | `NEOGOV_AUTH_ALLOWED_ISSUERS:latest` | NEOGOV_AUTH_ALLOWED_ISSUERS | `roles/secretmanager.secretAccessor` |
| `cm-campo-florido-lgpdweb` | `NEOGOV_AUTH_API_KEY:latest` | NEOGOV_AUTH_API_KEY | `roles/secretmanager.secretAccessor` |
| `cm-campo-florido-lgpdweb` | `NEOGOV_AUTH_ALLOWED_ISSUERS:latest` | NEOGOV_AUTH_ALLOWED_ISSUERS | `roles/secretmanager.secretAccessor` |
| `frutallgpdweb-3dab8` | `NEOGOV_AUTH_API_KEY:latest` | NEOGOV_AUTH_API_KEY | `roles/secretmanager.secretAccessor` |
| `frutallgpdweb-3dab8` | `NEOGOV_AUTH_ALLOWED_ISSUERS:latest` | NEOGOV_AUTH_ALLOWED_ISSUERS | `roles/secretmanager.secretAccessor` |
| `lgpdweb` | `neogov-auth-api-key:1` | NEOGOV_AUTH_API_KEY | `roles/secretmanager.secretAccessor` |
| `lgpdwebsaaeituiutaba` | `NEOGOV_AUTH_API_KEY:latest` | NEOGOV_AUTH_API_KEY | `roles/secretmanager.secretAccessor` |
| `lgpdwebsaaeituiutaba` | `NEOGOV_AUTH_ALLOWED_ISSUERS:latest` | NEOGOV_AUTH_ALLOWED_ISSUERS | `roles/secretmanager.secretAccessor` |
| `pm-estreladosul-mg-lgpdweb` | `NEOGOV_AUTH_API_KEY:latest` | NEOGOV_AUTH_API_KEY | `roles/secretmanager.secretAccessor` |
| `pm-estreladosul-mg-lgpdweb` | `NEOGOV_AUTH_ALLOWED_ISSUERS:latest` | NEOGOV_AUTH_ALLOWED_ISSUERS | `roles/secretmanager.secretAccessor` |
| `pm-machado-lgpdweb` | `NEOGOV_AUTH_API_KEY:latest` | NEOGOV_AUTH_API_KEY | `roles/secretmanager.secretAccessor` |
| `pm-machado-lgpdweb` | `NEOGOV_AUTH_ALLOWED_ISSUERS:latest` | NEOGOV_AUTH_ALLOWED_ISSUERS | `roles/secretmanager.secretAccessor` |
| `pm-montecarmelo-mg-lgpdweb` | `NEOGOV_AUTH_API_KEY:latest` | NEOGOV_AUTH_API_KEY | `roles/secretmanager.secretAccessor` |
| `pm-montecarmelo-mg-lgpdweb` | `NEOGOV_AUTH_ALLOWED_ISSUERS:latest` | NEOGOV_AUTH_ALLOWED_ISSUERS | `roles/secretmanager.secretAccessor` |
| `pm-neogov-qa-lgpdweb` | `NEOGOV_AUTH_API_KEY:latest` | NEOGOV_AUTH_API_KEY | Nenhuma concessão direta encontrada |
| `pm-neogov-qa-lgpdweb` | `NEOGOV_AUTH_ALLOWED_ISSUERS:latest` | NEOGOV_AUTH_ALLOWED_ISSUERS | Nenhuma concessão direta encontrada |
| `pm-pedrinopolis-lgpdweb` | `NEOGOV_AUTH_API_KEY:latest` | NEOGOV_AUTH_API_KEY | `roles/secretmanager.secretAccessor` |
| `pm-pedrinopolis-lgpdweb` | `NEOGOV_AUTH_ALLOWED_ISSUERS:latest` | NEOGOV_AUTH_ALLOWED_ISSUERS | `roles/secretmanager.secretAccessor` |
| `pm-tupaciguara-mg-lgpdweb` | `NEOGOV_AUTH_API_KEY:latest` | NEOGOV_AUTH_API_KEY | `roles/secretmanager.secretAccessor` |
| `pm-tupaciguara-mg-lgpdweb` | `NEOGOV_AUTH_ALLOWED_ISSUERS:latest` | NEOGOV_AUTH_ALLOWED_ISSUERS | `roles/secretmanager.secretAccessor` |
| `pmdeltamglgpdweb` | `NEOGOV_AUTH_API_KEY:latest` | NEOGOV_AUTH_API_KEY | `roles/secretmanager.secretAccessor` |
| `pmdeltamglgpdweb` | `NEOGOV_AUTH_ALLOWED_ISSUERS:latest` | NEOGOV_AUTH_ALLOWED_ISSUERS | `roles/secretmanager.secretAccessor` |
| `pmsgalgpdweb-32cf8` | `NEOGOV_AUTH_API_KEY:latest` | NEOGOV_AUTH_API_KEY | `roles/secretmanager.secretAccessor` |
| `pmsgalgpdweb-32cf8` | `NEOGOV_AUTH_ALLOWED_ISSUERS:latest` | NEOGOV_AUTH_ALLOWED_ISSUERS | `roles/secretmanager.secretAccessor` |
| `prefeituraituiutabalgpdweb` | `NEOGOV_AUTH_API_KEY:latest` | NEOGOV_AUTH_API_KEY | `roles/secretmanager.secretAccessor` |
| `prefeituraituiutabalgpdweb` | `NEOGOV_AUTH_ALLOWED_ISSUERS:latest` | NEOGOV_AUTH_ALLOWED_ISSUERS | `roles/secretmanager.secretAccessor` |
| `prefeiturateresopolislgpdweb` | `NEOGOV_AUTH_API_KEY:latest` | NEOGOV_AUTH_API_KEY | `roles/secretmanager.secretAccessor` |
| `prefeiturateresopolislgpdweb` | `NEOGOV_AUTH_ALLOWED_ISSUERS:latest` | NEOGOV_AUTH_ALLOWED_ISSUERS | `roles/secretmanager.secretAccessor` |
| `saosimaolgpdweb-1a6e5` | `NEOGOV_AUTH_API_KEY:latest` | NEOGOV_AUTH_API_KEY | `roles/secretmanager.secretAccessor` |
| `saosimaolgpdweb-1a6e5` | `NEOGOV_AUTH_ALLOWED_ISSUERS:latest` | NEOGOV_AUTH_ALLOWED_ISSUERS | `roles/secretmanager.secretAccessor` |

Em QA há também `roles/secretmanager.secretAccessor` no projeto, que pode conceder acesso além dos segredos listados. `latest` é referência móvel; os estados e números das versões estão no inventário JSON, sem payloads.

## Imagens e publicação

Agentes `service-NUMERO@serverless-robot-prod.iam.gserviceaccount.com` dos 23 projetos: `roles/artifactregistry.reader` no repositório `artefatos/us-central1/gestao-de-dados-api`. Runtime de QA: mesmo papel no repositório. Publicador `github-publicador@artefatos.iam.gserviceaccount.com`: `roles/artifactregistry.writer` no repositório. A política dessa conta concede `roles/iam.workloadIdentityUser` a principalSets de vários repositórios, incluindo `neogovbr/gestao-de-dados-api`.

## Entrada HTTP e alcance da evidência

Os 23 serviços têm checagem IAM de invocação desabilitada e ingresso `all`; não depender de uma binding `allUsers` para identificar acesso público. CORS limita o navegador e não substitui autenticação ou IAM. As permissões da conta runtime para Storage e Firestore são diferentes da permissão HTTP de invocar a API.

Esta matriz relata concessões explícitas encontradas nas políticas de projeto, bucket, segredo e conta de serviço. Condições são reproduzidas, não avaliadas em uma operação real. Não inclui IAM herdado de pastas/organização, Deny, grupos, permissões administrativas de todos os usuários, nem prova de mínimo privilégio. Não foram criadas chaves ou alteradas identidades.
