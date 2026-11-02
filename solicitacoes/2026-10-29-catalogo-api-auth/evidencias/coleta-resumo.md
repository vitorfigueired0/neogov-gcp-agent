# Evidências da coleta

Data: 2026-10-29T23:25:30-03:00 (`America/Sao_Paulo`). Todos os comandos abaixo foram executados somente para leitura, com `--project` explícito quando aplicável. Valores de variáveis e conteúdos de segredos não foram exibidos nem salvos.

## Contexto CLI

- Conta CLI ativa observada: `desenvolvimento@neogov.com.br`.
- Projeto default observado: `dashboard-admin-481516`; não foi usado como alvo.
- Região, zona e impersonação default: não configuradas.

## Comandos sanitizados e resultado resumido

| Consulta | Projetos | Resultado |
| --- | --- | --- |
| `gcloud projects describe PROJECT_ID` | ambos | projetos `ACTIVE`; números `569943311841` e `757454966640`. |
| `gcloud run services list/describe ... --region=us-central1` | ambos | um serviço por projeto, `Ready`, 100% na revisão mais recente; configuração registrada no inventário. |
| `gcloud run services get-iam-policy` | ambos | nenhuma associação direta no nível do serviço retornada. |
| `gcloud projects get-iam-policy` | ambos | papéis da execução e publicação registrados em `permissoes.md`. |
| `gcloud run revisions list` | ambos | histórico observado; somente a revisão atual recebe tráfego. |
| `gcloud firestore databases list` | ambos | bancos Native `auth-db-prd` e `auth-db-dev` em `us-central1`. |
| `gcloud secrets list` | ambos | cinco segredos por projeto; somente nomes/referências e versões configuradas foram documentados. |
| `gcloud artifacts repositories list`, `gcloud storage buckets list`, `gcloud app describe` | ambos | nenhum repositório/bucket local retornado; não há App Engine. |
| `gcloud services list --enabled` | ambos | Cloud Run, Firestore, Firebase, Identity Toolkit, Secret Manager e Artifact Registry habilitados. |

## Limites e falhas controladas

- A sintaxe `--gen1/--gen2` para Cloud Functions não é aceita por esta versão do CLI; a ajuda confirmou `--v2`. A repetição com a sintaxe correta retornou `cloudfunctions.googleapis.com` desabilitada. Não foi ativada API.
- A consulta Cloud SQL retornou `sqladmin.googleapis.com` desabilitada. Não foi ativada API.
- A subárvore `gcloud firebase` instalada não oferece `projects describe`.
- A consulta de mapeamentos de domínio exigiria a trilha beta; não foi concluída.
- Consultas posteriores planejadas para backups/índices Firestore e políticas diretas dos segredos foram bloqueadas pelo controle de escopo da sessão e não foram executadas.
