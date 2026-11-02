# Inventário — neogov-auth

Coleta de metadados em 2026-10-29T23:25:30-03:00 (`America/Sao_Paulo`). Escopo: `neogov-auth-prd` e `neogov-auth-dev`; sem leitura de dados de negócio ou valores de segredos.

## Instalações

| Ambiente | Projeto | Serviço / região | Estado e tráfego | Revisão | Imagem | Configuração observada |
| --- | --- | --- | --- | --- | --- | --- |
| Produção (informado) | `neogov-auth-prd` (nº `569943311841`) | Cloud Run `neogov-auth-prd` / `us-central1` | `Ready`; 100% | `neogov-auth-prd-00008-rdp` | `us-central1-docker.pkg.dev/artefatos/neogov-auth/neogov-auth:1.0.1` | 4 vCPU, 2 GiB, concorrência 80, timeout 300 s, escala 0–100; domínio `api.auth.neogov.com.br` pronto e certificado |
| Desenvolvimento (informado) | `neogov-auth-dev` (nº `757454966640`) | Cloud Run `neogov-auth-dev` / `us-central1` | `Ready`; 100% | `neogov-auth-dev-00025-lhc` | `us-central1-docker.pkg.dev/artefatos/neogov-auth/neogov-auth:develop` | 2 vCPU, 1 GiB, concorrência 80, timeout 300 s, escala 0–100; domínio `api.auth-develop.neogov.com.br` pronto e certificado |

Nos dois serviços: porta HTTP 8080, `ingress=all`, invocação IAM desabilitada, URL padrão desabilitada e URL de status não retornada. Esses fatos não identificam a rota pública alternativa.

## Dados e segredos

| Projeto | Firestore | Localização / modo | Proteção e retenção observadas | Referências de segredo (sem valores) |
| --- | --- | --- | --- | --- |
| `neogov-auth-prd` | `auth-db-prd` | `us-central1`, Native, concorrência pessimista | proteção contra exclusão desabilitada; retenção de versões: 3600 s; 4 backups `READY` | `API_KEY_HMAC_SECRET:1`, `GCP_PROJECT_ID:latest`, `PLATFORM_API_KEY_HMAC_SECRET:1`, `PLATFORM_JWT_SECRET:latest`, `ZEPTOMAIL_API_TOKEN:latest` |
| `neogov-auth-dev` | `auth-db-dev` | `us-central1`, Native, concorrência pessimista | proteção contra exclusão desabilitada; retenção de versões: 3600 s; nenhum backup retornado | `API_KEY_HMAC_SECRET:latest`, `GCP_PROJECT_ID:latest`, `PLATFORM_API_KEY_HMAC_SECRET:latest`, `PLATFORM_JWT_SECRET:latest`, `ZEPTOMAIL_API_TOKEN:latest` |

As variáveis não secretas observadas foram somente registradas por nome: `AUTH_PROVIDER_TIMEOUT_MS`, `FIRESTORE_DATABASE_ID` e `PLATFORM_JWT_ISSUER`; valores foram propositalmente omitidos.

## Publicação, rede e ausências

| Item | Resultado | Limite |
| --- | --- | --- |
| Artifact Registry nos projetos da aplicação | Nenhum repositório retornado | A imagem aponta para o projeto externo `artefatos`, fora do escopo. |
| Cloud Storage nos projetos da aplicação | Nenhum bucket retornado | Não exclui recursos acessados em outros projetos. |
| App Engine | Consulta bem-sucedida: não há aplicação App Engine | — |
| Cloud Functions | Não verificável: API `cloudfunctions.googleapis.com` está desabilitada; não foi ativada | Desabilitar API não prova ausência histórica de recursos. |
| Cloud SQL | Não verificável: API `sqladmin.googleapis.com` está desabilitada; não foi ativada | — |
| Domínio/TLS/mapeamento Cloud Run | Observado | Produção: `api.auth.neogov.com.br` → `neogov-auth-prd`; desenvolvimento: `api.auth-develop.neogov.com.br` → `neogov-auth-dev`. Ambos roteáveis, prontos e com certificado provisionado. |
| Firebase Auth | Inacessível | A API respondeu `PERMISSION_DENIED`: as ADC locais não têm quota project. Provedores/tenants/domínios não foram retornados. |
| Índices Firestore | Observado | Produção tem 3 índices compostos `READY` no grupo `users`; desenvolvimento não retornou índices compostos. |
| Políticas diretas de segredos | Observado | Os cinco segredos de cada projeto não retornaram `bindings` locais; concessão de projeto previamente observada continua sendo a fonte documentada. |

## Proveniência

As consultas sanitizadas e o resumo dos resultados estão em [evidencias/coleta-resumo.md](../../solicitacoes/2026-10-29-catalogo-api-auth/evidencias/coleta-resumo.md) e [na verificação complementar](../../solicitacoes/2026-10-29-verificar-pendencias-auth/evidencias/coleta-resumo.md). Não foi fornecido documento-fonte da aplicação.
