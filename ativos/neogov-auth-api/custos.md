# Custos — neogov-auth

Não foi solicitada apuração financeira; não houve consulta de faturamento, exportação ou rateio. A ausência de valores neste documento não significa custo zero.

| Componente | Instalações associadas | Possível fator de custo | Situação |
| --- | --- | --- | --- |
| Cloud Run | um serviço em cada projeto | CPU/memória, solicitações, tempo de instância e rede | Configuração inventariada; sem valor monetário. Produção: até 100 instâncias de 4 vCPU/2 GiB; desenvolvimento: até 100 de 2 vCPU/1 GiB; mínimo 0 em ambos. |
| Firestore Native | `auth-db-prd`, `auth-db-dev` | armazenamento, leituras, gravações, exclusões e PITR, se configurado | Produção tem quatro backups `READY`; desenvolvimento não retornou backups. Uso e custo não apurados. |
| Secret Manager | cinco segredos referenciados por instalação | versões, acessos e replicação | Metadados de segredo listados; sem leitura de conteúdo ou custos. |
| Firebase/Identity Toolkit | recursos de autenticação habilitados | operação de autenticação e produtos associados | Sem apuração/rateio. |
| Artifact Registry | imagem em `artefatos` | armazenamento e transferência em projeto externo | Compartilhado/externo; não atribuído à aplicação. |

Para uma análise posterior, é necessário definir período, conta de faturamento, critério de rateio para recursos compartilhados e autorização explícita para consultar custos.
