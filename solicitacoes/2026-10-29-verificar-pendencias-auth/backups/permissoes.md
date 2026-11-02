# Permissões — neogov-auth

Coleta em 2026-10-29T23:25:30-03:00. A matriz contém concessões observadas diretamente na política IAM de cada projeto; não avalia políticas herdadas, *deny policies*, condições fora do resultado, permissões efetivas ou políticas diretas de segredo.

| Projeto | Principal | Recurso/escopo | Papel observado | Finalidade provável | Condição |
| --- | --- | --- | --- | --- | --- |
| `neogov-auth-prd` | `neogov-auth-runtime@...` | projeto | `roles/datastore.user` | acesso ao Firestore pela execução | nenhuma observada |
| `neogov-auth-prd` | `neogov-auth-runtime@...` | projeto | `roles/firebaseauth.editor` | operações Firebase Auth pela execução | nenhuma observada |
| `neogov-auth-prd` | `neogov-auth-runtime@...` | projeto | `roles/secretmanager.secretAccessor` | acesso aos segredos referenciados | nenhuma observada |
| `neogov-auth-prd` | `github-publicador@artefatos.iam.gserviceaccount.com` | projeto | `roles/run.developer` | publicação/gestão Cloud Run; principal de outro projeto | nenhuma observada |
| `neogov-auth-dev` | `neogov-auth-runtime@...` | projeto | `roles/datastore.user` | acesso ao Firestore pela execução | nenhuma observada |
| `neogov-auth-dev` | `neogov-auth-runtime@...` | projeto | `roles/firebaseauth.editor` | operações Firebase Auth pela execução | nenhuma observada |
| `neogov-auth-dev` | `neogov-auth-runtime@...` | projeto | `roles/secretmanager.secretAccessor` | acesso aos segredos referenciados | nenhuma observada |
| `neogov-auth-dev` | `github-publicador@artefatos.iam.gserviceaccount.com` | projeto | `roles/run.admin` | publicação/gestão Cloud Run; principal de outro projeto | nenhuma observada |

Também foram observadas contas de serviço `firebase-adminsdk-fbsvc@...` com `roles/firebase.sdkAdminServiceAgent`, `roles/firebaseauth.admin` e `roles/iam.serviceAccountTokenCreator`, aparentando ser contas gerenciadas pelo Firebase. Não foi inferido uso direto pela aplicação.

## Execução, invocação e publicação

- **Execução:** a conta `neogov-auth-runtime@...` está configurada no template de cada serviço.
- **Invocação:** a política IAM direta de cada serviço não retornou `bindings`. Porém `run.googleapis.com/invoker-iam-disabled=true` está configurado, portanto a invocação não requer IAM Cloud Run. Isso não confirma que qualquer domínio, proxy ou aplicação aceite toda requisição.
- **Publicação:** `github-publicador@artefatos.iam.gserviceaccount.com` possui `run.developer` em produção e `run.admin` em desenvolvimento. O recurso/controle do projeto `artefatos` não foi consultado.

As políticas específicas dos cinco segredos de cada projeto não foram coletadas; logo, não há conclusão sobre concessões locais adicionais ou negações.
