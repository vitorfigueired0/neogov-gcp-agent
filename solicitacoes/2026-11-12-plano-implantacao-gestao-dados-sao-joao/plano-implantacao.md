# Plano de implantação — Gestão de Dados / São João del-Rei

Data: 12/11/2026, America/Sao_Paulo. Status: apresentado antes da implantação; nenhum recurso GCP alterado.

## Objetivo, evidências e limites

Implantar somente API e infraestrutura no projeto `pm-sao-joao-del-rei-mg` (971507433447). Frontend fora do escopo; origem informada: `https://pmsaojoaodelreimg.gestaodedados.neogov.com.br`. O usuário criará o vínculo na neogov-auth e preencherá os segredos depois. Não copiar chaves ou emissores de outros clientes.

As 7 consultas de metadados tiveram sucesso: projeto ACTIVE, 8 serviços Cloud Run (nenhum `gestao-de-dados-api`), apenas o banco `modules`, 5 buckets sem nome dedicado à aplicação, conta runtime esperada ausente e Secret Manager vazio. As 6 APIs exigidas pelo README já estão habilitadas. Isso não comprova ausência de implementação equivalente com outros nomes.

Usar a autenticação existente `desenvolvimento@neogov.com.br`, sem impersonação configurada, sem login ou chaves. Preservar default `dashboard-admin-481516`; sempre informar o projeto alvo. Não houve leitura de documentos Firestore, objetos ou payloads de segredos.

## Recursos propostos

| Item | Configuração proposta |
| --- | --- |
| Ambiente/região | Produção, `us-central1`; ainda sujeitos à confirmação, alinhados ao roteiro e à localização dos recursos atuais |
| Cloud Run | `gestao-de-dados-api`, porta 8080, 1 vCPU, 1 GiB, mínimo 0, máximo 3, concorrência 80, timeout 300 s; dimensionamento inicial proposto, sujeito a validação de carga |
| Conta runtime | `gestao-de-dados-api-runtime@pm-sao-joao-del-rei-mg.iam.gserviceaccount.com` |
| Firestore | Novo banco `gestao-de-dados`, Native/Standard, `us-central1`; não reutilizar `modules` |
| Storage | Novo bucket `gestao-de-dados-pm-sao-joao-del-rei-mg`, STANDARD/us-central1; nome sujeito à disponibilidade global |
| Segredos | `NEOGOV_AUTH_API_KEY` e `NEOGOV_AUTH_ALLOWED_ISSUERS`, inicialmente sem versões/payloads |
| Imagem | Release de produção publicada pela `master`, fixada por digest no repositório central; digest ainda não selecionado |
| Central | `https://api.auth.neogov.com.br`, proposta baseada no README; vínculo/tenant criados pelo usuário |
| Domínio da API | `api.pmsaojoaodelreimg.gestaodedados.neogov.com.br`, proposto e ainda não confirmado |

A região define residência dos novos dados nos EUA; escolha de localização do banco exige decisão antes da criação. Mudar a localização posteriormente exige outro recurso e migração. Não se propõe migração de dados legados nesta solicitação.

## Sequência de execução

1. **Fechar os alvos e precondições.** Confirmar produção/us-central1, hostname da API e release; verificar billing habilitado e permissões necessárias com a identidade existente. Revalidar nomes imediatamente antes de criar. Se aparecerem recursos novos, revisar o plano para reaproveitar com segurança. Não habilitar APIs já disponíveis.
2. **Criar a conta runtime dedicada.** Sem chave JSON. Conferir a conta retornada e políticas antes das concessões. A separação permite limitar a identidade ao banco/bucket desta instalação.
3. **Criar banco e índices.** Banco Native/Standard `gestao-de-dados`; conceder `roles/datastore.user` à runtime com condição restrita a esse banco. Criar somente os quatro índices compostos `complaints` do README: `reportedBy ASC + timestamp DESC + __name__ DESC`; adicionar `status ASC`, `reasonCode ASC`, ou ambos antes de `timestamp`, conforme os quatro índices. Aguardar todos READY. Antes da liberação, definir proteção contra exclusão e política de backup/retensão; nenhuma agenda ou PITR será ativada silenciosamente. Regras de clientes e permissões herdadas precisam de revisão antes de dados reais.
4. **Criar o bucket dedicado e configurar upload.** Acesso uniforme, prevenção de acesso público enforced; soft delete de 7 dias proposto. CORS só para a origem informada: GET/PUT, headers `Content-Type` e `x-goog-if-generation-match`, max-age 300 s. Runtime recebe objectCreator/objectViewer nesse bucket e TokenCreator somente na própria conta para signBlob. Não alterar CORS dos buckets existentes.
5. **Criar os dois recursos Secret Manager sem conteúdo.** Conceder secretAccessor à runtime somente nesses segredos. Verificar existência e ausência de versões por metadados. Não inserir valores falsos, gerar chaves BFF por conta própria nem acessar outras instalações. O usuário adicionará os valores verdadeiros pelo Secret Manager após cadastrar o vínculo na central.
6. **Preparar configuração e publicação.** `env-planejado.yaml` contém apenas variáveis não secretas propostas. Preparar o manifesto final com a imagem aprovada por digest e referências dos dois segredos. O digest e a origem master precisam ser comprovados; não implantar digest histórico do catálogo automaticamente. A dependência central é `artefatos/us-central1/gestao-de-dados-api`: verificação ou concessão fora do projeto alvo requer escopo confirmado. Se faltar, propor exclusivamente reader no repositório para `service-971507433447@serverless-robot-prod.iam.gserviceaccount.com`; não conceder reader na organização ou projeto inteiro. Até o usuário preencher os segredos, encerrar esta fase com infraestrutura preparada e implantação funcional pendente.
7. **Após o preenchimento pelo usuário, implantar a API.** Consultar apenas metadados para selecionar versões numéricas ENABLED, sem ler payloads. Vincular as versões fixas ao Cloud Run, implantar inicialmente com invocação IAM restrita e aguardar Ready. A aplicação exige chave e emissores válidos para iniciar; um segredo sem versão não permite instância funcional. Validar imagem, conta, configuração, índices e logs antes da exposição.
8. **Configurar entrada, DNS e TLS.** Confirmar domínio, responsável DNS e solução antes da ação dependente. Para produção, avaliar entrada existente ou balanceador HTTPS, recomendação atual do Google; balanceador adiciona recursos/custos ainda não incluídos na autorização de criação. O padrão histórico do catálogo usa mapeamento direto Cloud Run, mas o Google o classifica como Preview e não o recomenda para produção. Não adotar uma opção silenciosamente. Preparar registros exatos; alterar DNS somente no escopo e na zona confirmados. Liberar invocação HTTP necessária ao navegador após validação; autenticação de negócio permanece na neogov-auth. CORS não autentica clientes.
9. **Homologar e registrar.** Conferir revisão Ready, digest, versões de segredos, índices READY, DNS/TLS, cookie e CORS. Com o vínculo ativo, testar login, sessão inválida, logout e operações de dados/upload com dados de teste combinados e limpeza registrada. Não afirmar fluxo funcional só por Ready. Não modificar o frontend; entregar a URL final ao responsável. Atualizar catálogo, evidências e relatório com o que efetivamente ocorreu.

## Impactos negativos e reversão

- Novos recursos podem cobrar por execução, armazenamento, índices, operações, logs, versões/acessos de segredos, tráfego e dados retidos. Máximo de instâncias não garante teto financeiro. Não foi calculado preço nem consultado faturamento nesta fase.
- Mínimo zero implica cold starts; máximo 3 limita capacidade. Validar antes de uso real. IAM incorreto pode ampliar acesso a `modules` ou recursos existentes; conceder escopos específicos e preservar bindings atuais.
- Expor HTTP torna a API acessível pela internet; autenticação de negócio, cookies e tratamento de Swagger precisam de validação. Não preencher segredos com valores fictícios.
- Banco/bucket em nova região exigiriam migração. Escritas reais e alterações DNS podem afetar usuários; nenhum dado legado será movido nesta proposta.
- Reversão da preparação: revogar somente bindings criados nesta execução e interromper exposição/publicação. Exclusão de recursos novos exige nova avaliação de dados, custos retidos e autorização; não apagar bancos/buckets automaticamente. Sem deploy anterior nesta instalação, não existe revisão anterior validada para rollback. Depois da primeira revisão validada, atualizações podem retornar tráfego a ela, mas isso não desfaz escritas, IAM, DNS ou segredos.
- Reversão documental: restaurar exclusivamente os 5 arquivos em `backup-catalogo/`, após comparar para preservar mudanças posteriores. Contexto/evidências devem permanecer como histórico.

## Fontes

- [README local preservado](../../ativos/gestao-de-dados-api/README.md), documentação histórica, não comprovação da release atual.
- [Deploy de imagens no Cloud Run](https://docs.cloud.google.com/run/docs/deploying).
- [Segredos no Cloud Run: resolução no startup e versões fixas](https://docs.cloud.google.com/run/docs/configuring/services/secrets).
- [Opções de domínio e limitações do mapeamento direto](https://docs.cloud.google.com/run/docs/mapping-custom-domains).
- [IAM Firestore e condições](https://docs.cloud.google.com/firestore/native/docs/security/iam).
- Consultas JSON nesta pasta, com comando, instante, código de saída e limites.
