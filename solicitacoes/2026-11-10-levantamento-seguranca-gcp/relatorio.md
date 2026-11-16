# Segurança GCP — pontos de atenção

> Conservação documental — 13/11/2026: por pedido do usuário, foram mantidos o contexto, o relatório final e as entregas finais. Arquivos auxiliares, evidências separadas, scripts, verificações, diffs e backups locais foram removidos; referências a eles no histórico descrevem a execução original, não arquivos ainda disponíveis. Os resultados não foram reconsultados no GCP durante esta limpeza. Recuperação que dependa dos backups removidos exige outra cópia ou versão disponível no Git.

**Data da avaliação:** 10/11/2026.  
**Abrangência:** configurações de segurança de 65 projetos GCP.

**Prioridade imediata:** regras Firebase permitem operações sem autenticação em **19 recursos existentes de 13 projetos: 11 bancos Firestore e 8 buckets**. O alcance varia entre acesso global e caminhos específicos. Os achados indicam permissões nas configurações e não comprovam exploração ou vazamento.

## 1. Crítico — Firestore com leitura e escrita globais sem autenticação

| Projeto | Banco | Configuração observada |
| --- | --- | --- |
| `neogov-default` | `inventario-dados` | Leitura e escrita sem autenticação até 2085-03-30 |
| `estreladosullgpdrive` | `(default)` | Leitura e escrita sem autenticação |
| `lgpdrive-8f2a8` | `(default)` | Leitura e escrita sem autenticação até 2028-06-14 |
| `chequei` | `(default)` | Leitura e escrita sem autenticação |

**Ação recomendada:** substituir a liberação global por autorização por usuário, função e recurso; validar previamente os fluxos legítimos. As datas futuras de regras de teste mantêm o acesso permitido hoje. O risco inclui leitura, alteração e exclusão de documentos.

## 2. Crítico — denúncias e cadastros com acesso sem autenticação

No banco `modules` de **seis projetos**, as coleções `complaints` e `users-citizen` permitem leitura e criação sem autenticação:

- `pm-itaguai-rj-lgpdweb`
- `pm-sao-joao-del-rei-mg`
- `pm-coromandel-mg-lgpdweb`
- `cm-estrela-do-sul-lgpdweb`
- `novapontelgpdweb`
- `neogov-default`

A regra de atualização de `complaints` também admite requisição não autenticada quando o documento resultante contém `comments`; não limita a alteração somente a esse campo. Isso pode permitir adulteração de outros campos.

Em `neogov-default`, o banco **`gestao-de-dados`** permite leitura/criação pública de `users`, `complaints` e comentários. A atualização de perfil compara apenas o e-mail anterior e posterior, sem exigir identidade do solicitante.

**Ação recomendada:** manter o recebimento público de denúncias somente onde necessário, com campos e operações limitados; proteger leitura, identidade e atualizações. O risco de exposição de dados pessoais exige prioridade na revisão dessas coleções.

## 3. Crítico — Firebase Storage com regras abertas

Sete buckets permitem leitura e escrita, incluindo alteração/exclusão, sem autenticação:

| Projeto | Bucket | Configuração observada |
| --- | --- | --- |
| `novapontelgpdweb` | `novapontelgpdweb.firebasestorage.app` | Leitura e escrita sem autenticação |
| `prefeituraituiutabalgpdrive` | `prefeituraituiutabalgpdrive.firebasestorage.app` | Leitura e escrita sem autenticação |
| `cm-cachoeira-dourada-lgpdrive` | `cm-cachoeira-dourada-lgpdrive.firebasestorage.app` | Leitura e escrita sem autenticação |
| `camaraituiutabalgpdweb` | `camaraituiutabalgpdweb.firebasestorage.app` | Leitura e escrita sem autenticação |
| `camarasaogoncalodoabaete` | `camarasaogoncalodoabaete.firebasestorage.app` | Leitura e escrita sem autenticação |
| `neogov-default` | `neogov-default.firebasestorage.app` | Leitura e escrita sem autenticação |
| `chequei` | `chequei.appspot.com` | Leitura e escrita sem autenticação |

Além disso, em `neogov-default`, o bucket **`gestao-de-dados`** permite `write: if true` em `/complaints/{userId}/{fileName}`. A restrição de `update/delete` em outra declaração não cancela essa permissão ampla.

**Ação recomendada:** limitar operações por identidade e caminho, validar tamanho/tipo de arquivo e separar conteúdos destinados à divulgação pública. Ver interpretação em [regras inseguras do Firebase](https://firebase.google.com/docs/rules/insecure-rules).

## 4. Demais pontos de atenção

| Prioridade | Evidência e escopo | Ação recomendada |
| --- | --- | --- |
| Alta | **239 chaves de contas de serviço habilitadas e na validade**, em 125 contas de 54 projetos; **228 têm mais de 90 dias**. Destas 239, **173** pertencem a contas com concessões locais Owner/Editor; **74** a contas com Owner. | Identificar consumidores, substituir por identidade gerenciada/Workload Identity e desativar chaves dispensáveis com migração controlada. A idade é critério de priorização, não prova de vazamento. |
| Alta | **182 concessões Owner/Editor a contas de serviço em 59 projetos**. Uma única conta pessoal concentra o papel Owner nos 65 projetos. | Aplicar menor privilégio e revisar acesso administrativo centralizado. Incluir MFA e proteção das contas administrativas nessa revisão. |
| Alta | **24 bancos Firestore e 32 buckets Firebase**, em 28 projetos, permitem leitura/escrita globais a qualquer usuário autenticado no respectivo Firebase. | Restringir por proprietário, função e organização. Estar autenticado não comprova autorização para acessar todos os dados. |
| Revisar exposição | **212 serviços Cloud Run em 56 projetos** com ingresso `all` e invocação pública ou amplamente autenticada; **151** desabilitam a checagem IAM. Incluem APIs, processamento de arquivos e serviços de gatilhos. Dois serviços de autenticação têm URL padrão desabilitada; a exposição por rotas alternativas requer validação. | Confirmar quais devem ser públicos, testar autorização na aplicação e restringir gatilhos e funções administrativas. Exposição HTTP pública pode ser intencional e não comprova falha na aplicação. |
| Revisar exposição | **4 funções HTTP de `chequei`** com `allUsers` invocador: `list_pdfs`, `driveshare`, `file-api`, `fetch_table_names_and_texts`. | Validar a necessidade de acesso público e exigir autenticação e autorização nas operações restritas. |
| Revisar exposição | **5 buckets com concessão IAM de leitura a `allUsers`**: `cdn-banner` (`neogov-default`); `entidades-png` (`lgpdrive-8f2a8`); `neogov`, `neogov-public-images` e `public-files-media` (`chequei`). | Confirmar que contêm exclusivamente arquivos públicos. O papel Composer usado em `entidades-png` também inclui leitura de objetos. A finalidade pública dos arquivos e a acessibilidade externa precisam ser confirmadas. |
| Média | **SSH 22 e RDP 3389 abertos a `0.0.0.0/0` em 43 projetos**, além de ICMP. **Não há VMs no inventário avaliado.** | Remover ou restringir regras desnecessárias antes de criar VMs; usar IAP/VPN ou faixas administrativas. É risco de configuração, sem VM exposta comprovada hoje. |
| Alta para recuperação / média para rede | `treinamento-db` em **`treinamento-neogov-prod` e `treinamento-neogov-dev`**: backup automático desabilitado, IP público e TLS não obrigatório. Sem redes autorizadas configuradas; **não há liberação `0.0.0.0/0` identificada**. | Habilitar proteção de recuperação adequada e TLS obrigatório; avaliar IP privado/Cloud SQL Connector. IP público sozinho não comprova acesso irrestrito ao banco. |
| Média | As **18 instâncias Cloud SQL** permitem conexões diretas sem TLS (`ALLOW_UNENCRYPTED_AND_ENCRYPTED`). As outras 16 têm somente IP privado. | Exigir TLS conforme o cliente utilizado. Validar se os clientes atuais já utilizam TLS ou conectores. |
| Média | **248 funções de primeira geração** com `SECURE_OPTIONAL`: configuração permite HTTP sem redirecionar para HTTPS; IAM permanece um controle separado. | Exigir HTTPS nos consumidores e na configuração. Confirmar a exigência de HTTPS nos fluxos de integração. |
| Revisar controles | **145 buckets com ACLs habilitadas**. Em `lgpdwebsaaeituiutaba`, os controles App Check de Storage, Firestore e Identity Toolkit estão `UNENFORCED`. | Avaliar acesso uniforme e ACLs de objetos; planejar App Check nos clientes aplicáveis. App Check complementa as regras e não substitui autorização. |

As listas completas de projetos, recursos, contas, chaves e condições estão nos anexos. Referências: [invocação pública no Cloud Run](https://docs.cloud.google.com/run/docs/authenticating/public), [gestão de chaves](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys), [papel Composer](https://docs.cloud.google.com/iam/docs/roles-permissions/composer), [regras de firewall](https://docs.cloud.google.com/firewall/docs/firewalls), [TLS no Cloud SQL](https://docs.cloud.google.com/sql/docs/mysql/authorize-ssl) e [HTTP em funções](https://docs.cloud.google.com/functions/docs/reference/rest/v1/projects.locations.functions).

## 5. Abrangência e limitações técnicas

O inventário abrange **427 serviços Cloud Run, 350 funções, 508 buckets, 18 instâncias Cloud SQL, 282 datasets BigQuery e 137 repositórios Artifact Registry**. Não constam VMs, clusters GKE, forwarding rules ou backend services nos resultados dos serviços avaliados.

Não foram identificadas concessões públicas nas políticas IAM de projeto, nos datasets BigQuery ou nos repositórios avaliados. As três instâncias Realtime Database identificadas têm regras de negação total ou liberações temporais expiradas.

Pontos que exigem avaliação complementar:

- **Inventário de chaves incompleto por API IAM desabilitada:** `neogov-auth-prd`, `neogov-auth-dev`, `lgpdweb-h4-cleanup-qa-202611`, `teste-daa68`, `pm-neogov-lgpdrive`, `uberlandia-prefeitura` e `exemplo-c20ee`.
- **Firewall e Artifact Registry de `modulocookies`:** avaliação limitada por bloqueio de faturamento.
- APIs desabilitadas representam lacunas de cobertura e não comprovam ausência de recursos. A cobertura por projeto está detalhada no anexo.
- Autenticação e autorização das aplicações, exploração das permissões, conteúdo dos dados, vulnerabilidades das imagens, TLS/domínios, ACLs individuais de objetos/tabelas, IAM herdado, políticas Deny, grupos e MFA exigem validação específica. A configuração App Check foi confirmada somente em `lgpdwebsaaeituiutaba`.

As recomendações devem ser aplicadas com testes de dependências e plano de reversão, especialmente ao restringir regras Firebase, revogar chaves e alterar permissões de execução. Os achados refletem as configurações na data da avaliação.

## 6. Anexos técnicos

- [Recursos que precisam de atenção](recursos-atencao.csv)
- [Regras Firebase que precisam de revisão](regras-firebase-atencao.csv)
- [Metadados das chaves de contas de serviço](chaves-contas-servico.csv)
- [Permissões IAM amplas e condições](iam-amplo.csv)
- [Cobertura por projeto](cobertura-projetos.csv)
