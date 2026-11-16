# Execução aprovada — infraestrutura de Gestão de Dados

> Conservação documental — 13/11/2026: por pedido do usuário, foram mantidos o contexto, o relatório final e as entregas finais. Arquivos auxiliares, evidências separadas, scripts, verificações, diffs e backups locais foram removidos; referências a eles no histórico descrevem a execução original, não arquivos ainda disponíveis. Os resultados não foram reconsultados no GCP durante esta limpeza. Recuperação que dependa dos backups removidos exige outra cópia ou versão disponível no Git.

Data: 2026-11-12T09:59:10.478967-03:00 (America/Sao_Paulo). Projeto `pm-sao-joao-del-rei-mg` (971507433447), produção, us-central1.

**Resultado parcial da implantação: infraestrutura preparada e verificada; API Cloud Run ainda não publicada.** A preparação foi executada após a resposta `sim` ao plano e à confirmação de ambiente/região/domínio. O usuário configurará neogov-auth e preencherá os dois segredos posteriormente. O relatório anterior permanece preservado em [diagnóstico e planejamento](../relatorio.md).

## Recursos criados e configuração observada

| Componente | Estado |
| --- | --- |
| Conta runtime | `gestao-de-dados-api-runtime@pm-sao-joao-del-rei-mg.iam.gserviceaccount.com`; sem chaves USER_MANAGED |
| Firestore | Banco dedicado `gestao-de-dados`, Native/Standard/us-central1, proteção contra exclusão ENABLED, freeTier=false |
| Índices | Quatro índices de coleção `complaints` READY; campos, IDs e instante em ver-indices-5.json (auxiliar removido; resultado consolidado neste relatório) |
| Storage | `gs://gestao-de-dados-pm-sao-joao-del-rei-mg`, STANDARD/US-CENTRAL1, acesso uniforme e prevenção de acesso público enforced |
| CORS | GET/PUT somente para `https://pmsaojoaodelreimg.gestaodedados.neogov.com.br`; Content-Type/x-goog-if-generation-match, 300 s |
| Soft delete | 604800 s (7 dias), sujeito a cobrança por dados retidos |
| Segredos | `NEOGOV_AUTH_API_KEY` e `NEOGOV_AUTH_ALLOWED_ISSUERS`, replicação user-managed/us-central1, ambos sem versões/payloads |
| Recuperação Firestore | PITR desabilitado; listagem de agendas de backup vazia; política a definir antes de dados reais |
| Cloud Run / DNS / TLS | Não criados/configurados nesta fase; sem publicação ou teste funcional |

## IAM e verificação

Foram adicionadas seis concessões à runtime: datastore.user no projeto com condição exata ao banco `gestao-de-dados`; storage.objectCreator e storage.objectViewer no bucket novo; iam.serviceAccountTokenCreator na própria conta; secretmanager.secretAccessor em cada um dos dois segredos novos. A política de projeto passou da versão 1 à versão 3 para suportar a condição; nenhuma binding anterior foi removida ou substituída. As quatro bindings padrão do bucket também foram preservadas. Políticas anteriores e posteriores estão nos JSON `pre-*`/`ver-*`.

Há contas preexistentes com acesso amplo ao Firestore e papéis de projeto com acesso padrão ao bucket; a nova concessão restrita não remove esses acessos. Não se afirma isolamento total de administradores ou auditoria completa da herança. Condições/IAM foram verificadas por metadados e comparação de políticas; não foram exercitadas por impersonação, leitura de documentos ou geração de URLs.

A conta gcloud permaneceu `desenvolvimento@neogov.com.br`, default `dashboard-admin-481516`, sem mudança de impersonação/configuração. Não houve login, ADC, criação/exportação de credenciais ou leitura de payloads. CLI executado fora do sandbox somente para permitir o uso do cache de autenticação existente e do acesso de rede. Todos os comandos destinados ao GCP informaram explicitamente o projeto.

A listagem de serviços Run antes/depois tem o mesmo conteúdo de nomes/labels. Nenhuma operação de escrita foi direcionada ao banco `modules`, serviços/buckets antigos, outro projeto, DNS ou vínculo neogov-auth. Isso não constitui monitoramento de disponibilidade dos serviços antigos. Uma consulta inicial do CLI falhou por sintaxe de projeção do campo de labels; foi corrigida e repetida somente como leitura, sem efeitos remotos.

## Entrega e pendências

- [Env sem credenciais](env.yaml), preparado localmente e não aplicado ao Cloud Run.
- [Template Cloud Run](cloud-run.template.json), com marcadores explícitos para imagem por digest e versões numéricas. Não aplicar enquanto houver marcadores.
- [Como preencher os segredos](preencher-segredos.md), com links diretos ao console. O usuário deve criar o vínculo e adicionar os valores corretos nos dois segredos, sem enviá-los pelo chat.
- Confirmar release de produção publicada pela master, digest e acesso de leitura ao repositório central. Nenhuma leitura ou mudança em `artefatos` foi executada nesta etapa.
- Depois dos valores, selecionar versões ENABLED por metadados, publicar a API inicialmente com invocação restrita e homologar login, sessões inválidas, dados e mídia.
- Definir política de recuperação e revisar acessos amplos antes de dados reais. Decidir a solução de entrada para o hostname confirmado `api.pmsaojoaodelreimg.gestaodedados.neogov.com.br`; DNS/TLS e eventual balanceador ainda não foram autorizados com escopo concreto.

## Custos e reversão

Billing habilitado foi verificado; não houve consulta financeira ou estimativa monetária. Banco nomeado informa freeTier=false. Banco/índices, operações, Storage/soft delete e futuras versões de segredos e execução podem cobrar conforme uso. Não atribuir serviços antigos ou recursos centrais a esta API. Nenhuma carga ou escrita de negócio foi executada nesta preparação.

O roteiro de reversão (auxiliar removido; resultado consolidado neste relatório) contém comandos específicos para revogar somente as seis concessões adicionadas; **não foi executado**. Antes de reverter, consultar o estado atual e preservar mudanças posteriores. Não aplicar políticas antigas inteiras sobre as atuais. Revogar IAM não apaga dados nem encerra todos os custos de armazenamento. Remoção do banco/bucket/segredos/conta exigirá nova avaliação de dependências e conteúdo; banco tem proteção contra exclusão e objetos podem ficar retidos pelo soft delete.

## Documentação e integridade

O catálogo [Gestão de Dados](../../../ativos/gestao-de-dados-api/inventario.md) foi complementado em `componentes.md`, `inventario.md`, `inventario.json`, `permissoes.md` e `custos.md`; README e registros históricos preservados. Backups anteriores à atualização em `backup-catalogo/` e diff (auxiliar removido; resultado consolidado neste relatório). Restauração documental deve comparar e restaurar apenas esses arquivos, preservando alterações posteriores.

Contexto da continuação em [contexto.md](contexto.md). Scripts documentais, sequência exata de comandos, respostas e verificações estão nesta pasta. A verificação local (auxiliar removido; resultado consolidado neste relatório) confere os metadados, comparação de IAM, índices, consistência do catálogo, JSON, links e ausência de padrões comuns de segredos. Nenhum temporário descartável foi criado nesta execução; somente artefatos de auditoria foram salvos. Alterações preexistentes no workspace foram preservadas.

Fontes técnicas: [condição IAM por banco](https://docs.cloud.google.com/firestore/native/docs/manage-databases#configure_per-database_access_permissions), [criação de banco](https://docs.cloud.google.com/sdk/gcloud/reference/firestore/databases/create), [segredos sem versões](https://docs.cloud.google.com/sdk/gcloud/reference/secrets/create) e [comportamento de segredos no Cloud Run](https://docs.cloud.google.com/run/docs/configuring/services/secrets).

## Reversão de IAM consolidada

Comandos documentais, não executados. Consultar políticas e consumidores atuais antes de remover somente as concessões adicionadas; preservar mudanças posteriores e não remover dados automaticamente.

```bash
gcloud projects remove-iam-policy-binding pm-sao-joao-del-rei-mg --member=serviceAccount:gestao-de-dados-api-runtime@pm-sao-joao-del-rei-mg.iam.gserviceaccount.com --role=roles/datastore.user '--condition=expression=resource.name=="projects/pm-sao-joao-del-rei-mg/databases/gestao-de-dados",title=gestao-de-dados-only,description=Acesso runtime somente ao banco gestao-de-dados' --project=pm-sao-joao-del-rei-mg

gcloud iam service-accounts remove-iam-policy-binding gestao-de-dados-api-runtime@pm-sao-joao-del-rei-mg.iam.gserviceaccount.com --member=serviceAccount:gestao-de-dados-api-runtime@pm-sao-joao-del-rei-mg.iam.gserviceaccount.com --role=roles/iam.serviceAccountTokenCreator --condition=None --project=pm-sao-joao-del-rei-mg

gcloud storage buckets remove-iam-policy-binding gs://gestao-de-dados-pm-sao-joao-del-rei-mg --member=serviceAccount:gestao-de-dados-api-runtime@pm-sao-joao-del-rei-mg.iam.gserviceaccount.com --role=roles/storage.objectCreator --project=pm-sao-joao-del-rei-mg

gcloud storage buckets remove-iam-policy-binding gs://gestao-de-dados-pm-sao-joao-del-rei-mg --member=serviceAccount:gestao-de-dados-api-runtime@pm-sao-joao-del-rei-mg.iam.gserviceaccount.com --role=roles/storage.objectViewer --project=pm-sao-joao-del-rei-mg

gcloud secrets remove-iam-policy-binding NEOGOV_AUTH_API_KEY --member=serviceAccount:gestao-de-dados-api-runtime@pm-sao-joao-del-rei-mg.iam.gserviceaccount.com --role=roles/secretmanager.secretAccessor --condition=None --project=pm-sao-joao-del-rei-mg

gcloud secrets remove-iam-policy-binding NEOGOV_AUTH_ALLOWED_ISSUERS --member=serviceAccount:gestao-de-dados-api-runtime@pm-sao-joao-del-rei-mg.iam.gserviceaccount.com --role=roles/secretmanager.secretAccessor --condition=None --project=pm-sao-joao-del-rei-mg
```
