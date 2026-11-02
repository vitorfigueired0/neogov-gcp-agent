# Componentes — neogov-auth

Coleta em 2026-10-29T23:25:30-03:00 (`America/Sao_Paulo`). Não foi fornecido README ou outra documentação da aplicação; por isso não há `README.md` neste ativo.

## Finalidade e arquitetura observada

O usuário informou que esta é a API de autenticação, em produção no projeto `neogov-auth-prd` e em desenvolvimento no projeto `neogov-auth-dev`. Essa classificação de ambientes é **informada pelo usuário**. A implementação observada em ambos os projetos é um serviço Cloud Run, com um banco Firestore Native local e integração Firebase/Identity Toolkit habilitada.

```mermaid
flowchart LR
  Cliente[Clientes / rota externa não verificada] --> CR[Cloud Run: neogov-auth-*]
  CR --> FS[Firestore Native: auth-db-*]
  CR --> FA[Firebase / Identity Toolkit]
  CR --> SM[Secret Manager]
  AR[Artifact Registry no projeto externo artefatos] --> CR
```

O diagrama descreve vínculos observados ou inferidos pela configuração; não comprova chamadas, autenticação funcional, rotas, domínio/TLS ou conteúdo armazenado.

| Componente | Estado da verificação | Evidência e limite |
| --- | --- | --- |
| Cloud Run e domínio | Observado | Um serviço em `us-central1` por projeto; ambos `Ready`, com 100% do tráfego na revisão mais recente e domínio mapeado. |
| Firestore | Observado | Bancos Native `auth-db-prd` e `auth-db-dev`; não foram lidos documentos. Índices e metadados de backup foram consultados. |
| Firebase / Identity Toolkit | Observado parcialmente | APIs habilitadas; configuração de provedores, domínios autorizados e tenants inacessível por limitação de quota project das ADC locais. |
| Secret Manager | Observado | Cinco referências de segredo por instalação; conteúdo não foi lido. Políticas diretas dos segredos não retornaram associações. |
| Imagem/publicação | Observado parcialmente | Imagens vêm de `us-central1-docker.pkg.dev/artefatos/neogov-auth/...`; o projeto `artefatos` não foi consultado. |
| E-mail transacional | Inferido | A referência `ZEPTOMAIL_API_TOKEN` sugere uma integração externa, sem comprovação de uso em execução. |

## Exposição e riscos observados

- Ambos os serviços têm `ingress=all` e `run.googleapis.com/invoker-iam-disabled=true`. A invocação não é controlada pelo IAM do Cloud Run. A política IAM do serviço sem `allUsers` não demonstra privacidade nesse cenário.
- A URL padrão do Cloud Run está desabilitada, mas os domínios Cloud Run foram confirmados: `api.auth.neogov.com.br` → `neogov-auth-prd` e `api.auth-develop.neogov.com.br` → `neogov-auth-dev`. Ambos estão `Ready`, `DomainRoutable` e `CertificateProvisioned`, com CNAME para `ghs.googlehosted.com.`. WAF/CDN e outros controles de borda não foram verificados.
- `minScale=0` permite escala a zero; há limite máximo de 100 instâncias. Isso é configuração de capacidade, não prova de desempenho nem disponibilidade fim a fim.
- A proteção contra exclusão do Firestore está desabilitada nos dois bancos. Produção possui quatro backups `READY` do `auth-db-prd`, de 03, 10, 17 e 24/10/2026, com expiração entre 09 e 30/01/2027; desenvolvimento não retornou backups. Não foi testada restauração.
- As versões atuais estão prontas, mas isso não constitui teste das rotas nem da autenticação. Em histórico de revisões do desenvolvimento foi observado um erro antigo de acesso a segredos em revisão já retirada; a revisão atual está `Ready`.

## Diferenças entre instalações

| Aspecto | Produção | Desenvolvimento |
| --- | --- | --- |
| Imagem | `.../neogov-auth:1.0.1` | `.../neogov-auth:develop` |
| CPU / memória | 4 vCPU / 2 GiB | 2 vCPU / 1 GiB |
| Revisão recebendo tráfego | `neogov-auth-prd-00008-rdp` | `neogov-auth-dev-00025-lhc` |
| Publicador externo | `roles/run.developer` | `roles/run.admin` |

## Pendências

1. Verificar WAF/CDN e autenticação de borda; domínio, rota Cloud Run e certificado já foram observados, mas não equivalem a teste funcional da API.
2. A configuração de Firebase Authentication (provedores, domínios autorizados e tenants) permanece inacessível porque a consulta exige um quota project nas ADC locais. Configurá-lo alteraria credenciais locais e requer autorização específica.
3. Cloud Functions e Cloud SQL continuam não verificáveis: as APIs correspondentes estão desabilitadas nos dois projetos e não foram ativadas.
4. Confirmar a origem da publicação e permissões no projeto externo `artefatos`, se esse projeto for incluído em uma solicitação futura.
