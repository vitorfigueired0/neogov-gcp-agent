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

## São João del-Rei — consulta de 12/11/2026

A conta runtime `gestao-de-dados-api-runtime@pm-sao-joao-del-rei-mg.iam.gserviceaccount.com` não consta na listagem de contas do projeto. Não foram consultadas políticas IAM do projeto, herança, buckets ou repositório central nesta etapa; ausência da conta não é auditoria das permissões existentes. Não há segredos listados no projeto. Nenhuma concessão foi criada ou alterada.

O plano propõe Firestore restrito ao novo banco por condição, criação/leitura de objetos somente no novo bucket, assinatura na própria conta runtime e acesso somente aos segredos do vínculo desta instalação. A leitura da imagem pelo agente gerenciado exigirá verificar dependência em `artefatos`, fora do projeto alvo, antes de qualquer alteração nesse escopo. [Evidências e plano](../../solicitacoes/2026-11-12-plano-implantacao-gestao-dados-sao-joao/relatorio.md).

## Concessões executadas — São João del-Rei, 12/11/2026

Principal: `serviceAccount:gestao-de-dados-api-runtime@pm-sao-joao-del-rei-mg.iam.gserviceaccount.com`. Estado consultado em 2026-11-12T09:59:10.373973-03:00.

| Recurso/escopo | Papel | Condição/finalidade |
| --- | --- | --- |
| Projeto `pm-sao-joao-del-rei-mg` | `roles/datastore.user` | `resource.name=="projects/pm-sao-joao-del-rei-mg/databases/gestao-de-dados"`; apenas o novo banco na concessão |
| Bucket `gestao-de-dados-pm-sao-joao-del-rei-mg` | `roles/storage.objectCreator` | Criar objetos; sem condição |
| Mesmo bucket | `roles/storage.objectViewer` | Ler objetos/metadados; sem condição |
| Própria runtime | `roles/iam.serviceAccountTokenCreator` | Assinar URLs/signBlob; sem condição |
| Secret `NEOGOV_AUTH_API_KEY` | `roles/secretmanager.secretAccessor` | Somente este segredo; ainda sem versões |
| Secret `NEOGOV_AUTH_ALLOWED_ISSUERS` | `roles/secretmanager.secretAccessor` | Somente este segredo; ainda sem versões |

Comparação das políticas antes/depois: todas as bindings antigas do projeto preservadas, adicionada exatamente uma binding condicional à runtime. No bucket foram preservadas as quatro bindings padrão e adicionadas duas para a runtime. Outras contas têm concessões Firestore amplas no projeto; elas continuam alcançando o novo banco conforme seus papéis. O bucket também mantém bindings padrão para papéis de projeto; prevenção de acesso público não remove esses acessos. Herança, Deny e acesso efetivo via SDK não foram testados. Não se afirma isolamento integral ou auditoria IAM completa.

Invocação/publicação: nenhum serviço Cloud Run criado ou acesso público liberado; nenhuma concessão em `artefatos` executada. Políticas anteriores e roteiro de revogação específica salvos na solicitação. [Relatório de execução e evidências](../../solicitacoes/2026-11-12-plano-implantacao-gestao-dados-sao-joao/execucao-aprovada/relatorio.md).

## Preenchimento dos segredos — São João del-Rei, 12/11/2026

Em 2026-11-12T10:05:48.603568-03:00, adicionadas e verificadas por metadados as versões `NEOGOV_AUTH_API_KEY:1` e `NEOGOV_AUTH_ALLOWED_ISSUERS:1`, ambas ENABLED, no projeto `pm-sao-joao-del-rei-mg`. Chave fornecida pelo usuário sem registro do valor; emissor exato indicado pelo usuário: `https://api.auth.neogov.com.br` (sem barra final). Nenhum payload lido na verificação. Este estado sucede os registros anteriores de segredos sem versões. IAM não alterado; vínculo tenant/sistema e validação funcional ainda não comprovados. Template local atualizado nesta solicitação para referências fixas `:1`, mantendo a imagem pendente; não houve deploy. [Relatório do preenchimento](../../solicitacoes/2026-11-12-preencher-segredos-gestao-dados-sao-joao/relatorio.md).

## Publicação HTTP e imagem — São João del-Rei, 12/11/2026

Em 2026-11-12T10:20:22.124691-03:00, confirmado `roles/artifactregistry.reader` para `serviceAccount:service-971507433447@serverless-robot-prod.iam.gserviceaccount.com` somente no repositório `artefatos/us-central1/gestao-de-dados-api`. A comparação das políticas registra somente esse membro novo; demais membros/papéis preservados. Runtime e permissões de dados/segredos existentes não foram ampliados nesta etapa.

O serviço `pm-sao-joao-del-rei-mg/us-central1/gestao-de-dados-api` tem `run.googleapis.com/invoker-iam-disabled=true`, ingress all e política sem allUsers. O acesso HTTP público foi testado; rotas protegidas recusaram sessões ausentes/inválidas (401). Documentação /docs e /docs-json está acessível sem sessão (200). Não se afirma teste de login válido, controle de todos os tenants, IAM herdado ou escrita real em dados.

Reversão de exposição: reabilitar o invoker IAM check, preservando a política atual; isso interrompe chamadas públicas. A leitura do repositório pode ser revogada somente após verificar consumidores. [Relatório do deploy](../../solicitacoes/2026-11-12-deploy-gestao-dados-sao-joao/relatorio.md).
