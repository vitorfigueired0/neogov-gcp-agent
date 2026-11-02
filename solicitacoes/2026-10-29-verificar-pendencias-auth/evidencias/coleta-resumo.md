# Evidências — verificação de pendências

Coleta em 2026-10-29T23:32:55-03:00 (`America/Sao_Paulo`). Somente consultas de leitura; nenhum valor de segredo, documento Firestore ou credencial foi salvo.

| Consulta sanitizada | Resultado |
| --- | --- |
| `gcloud beta run domain-mappings list/describe --region=us-central1` | `api.auth.neogov.com.br` roteia para `neogov-auth-prd`; `api.auth-develop.neogov.com.br` roteia para `neogov-auth-dev`. Ambos `Ready`, `DomainRoutable` e `CertificateProvisioned`; CNAME para `ghs.googlehosted.com.`. |
| `gcloud firestore backups list --location=us-central1` | Produção: 4 backups `READY` de `auth-db-prd`, snapshots em 03, 10, 17 e 24/10/2026; desenvolvimento: nenhum backup retornado. |
| `gcloud firestore indexes composite list --database=...` | Produção: 3 índices compostos `READY` para `users`; desenvolvimento: nenhum índice composto retornado. |
| `gcloud secrets get-iam-policy SECRET_ID` | Para os 5 segredos de cada projeto, resposta sem `bindings` locais (somente `etag`). |
| `gcloud functions list` e `gcloud sql instances list` | APIs Cloud Functions e Cloud SQL desabilitadas nos dois projetos; não foram ativadas. |
| `identitytoolkit.googleapis.com/v2/projects/PROJECT_ID/config` e `/tenants` | `PERMISSION_DENIED`: as ADC locais usadas pela chamada exigem quota project. Nenhuma mudança foi feita na configuração de credenciais. |

## Diagnóstico da sintaxe

- `gcloud firestore backups list` aceita `--location`, não `--database`; a documentação de ajuda do CLI confirmou a sintaxe antes da repetição.
- `gcloud beta run domain-mappings describe` exige `--domain=DOMINIO`; a consulta repetida com essa flag confirmou a rota Cloud Run.
