# Relatório — associação de authUserId no LGPDweb QA

> Conservação documental — 13/11/2026: por pedido do usuário, foram mantidos o contexto, o relatório final e as entregas finais. Arquivos auxiliares, evidências separadas, scripts, verificações, diffs e backups locais foram removidos; referências a eles no histórico descrevem a execução original, não arquivos ainda disponíveis. Os resultados não foram reconsultados no GCP durante esta limpeza. Recuperação que dependa dos backups removidos exige outra cópia ou versão disponível no Git.

## Estado atual — remoção concluída

**17 documentos de QA removidos**, correspondentes aos **14 e-mails sem conta localizada no provider**, conforme autorização do usuário. Verificação concluída em 2026-11-11T17:51:13.339873-03:00. A coleção `pm-neogov-qa-lgpdweb/modules/user-data` passou de **43 para 26 documentos**. Os 26 restantes permaneceram iguais ao snapshot anterior, inclusive os 10 sem e-mail, ignorados conforme o pedido. Os cadastros do Auth permaneceram iguais.

Na execução houve backup integral dos documentos removidos e payload de restauração preparado, não executado. Ambos foram removidos na limpeza autorizada de 13/11/2026; os arquivos restantes não permitem restauração integral dos documentos excluídos. Uma subcoleção `course-progress`, sob um dos documentos removidos, foi preservada e verificada. Esse histórico continua armazenado com o documento pai ausente.

Os oito vínculos criados anteriormente e o exemplo preexistente foram preservados. Permanecem pendentes apenas seis duplicatas cujo ID difere do provider e a divergência de Francisco; os dez documentos sem e-mail continuam ignorados.

Listas atuais: [removidos](etapa4-removidos.csv), [pendências e ignorados](etapa4-pendencias-atuais.csv) e [sincronizados na etapa anterior](etapa3-sincronizados.csv). As seções anteriores são histórico; o detalhe desta remoção está na etapa 4, ao final.

## Histórico — estado após cadastro direto

**8 usuários cadastrados diretamente no Firestore do Auth e 8 documentos de QA associados por authUserId**, com releitura e comparação concluídas em 2026-11-11T17:03:30.435932-03:00. Não foram criadas ou alteradas contas no provider. O vínculo do exemplo já estava correto e foi preservado.

O escopo vigente ignora usuários exclusivos do Auth. Dos documentos de QA ainda sem vínculo, 17 correspondem a 14 e-mails não localizados no Firebase QA; 6 são duplicatas com ID diferente do UID real; 1 tem cadastro Auth divergente (Francisco). Os 10 documentos sem e-mail foram ignorados. As seções históricas abaixo registram diagnósticos anteriores, não pendências adicionais do escopo atual.

Listas finais: [sincronizados](etapa3-sincronizados.csv) e pendências/ignorados (auxiliar removido; resultado consolidado neste relatório). Os IDs, evidências e a reversão constam na etapa final deste relatório.

Data: 2026-11-11T15:47:15.584630-03:00

## Histórico — resultado da primeira etapa

Comparação concluída; nenhuma alteração remota executada. Foram encontrados 15 documentos em users no Auth dev, dos quais 4 estão associados ao sistema LGPDweb. Desses 4, 1 já está sincronizado corretamente e 3 não existem na coleção de destino pelos identificadores consultados. Não há correspondência elegível que exija preencher authUserId. A associação solicitada permanece pendente para os 3 usuários sem documento correspondente em QA.

## Escopo e identificação

- Origem: `neogov-auth-dev`, banco `auth-db-dev`, coleção `users`.
- Sistema confirmado: `systems/Dx41wrLCM4QNYmxaMyc3`, nome `lgpdweb`, ativo.
- Seleção: `tenant_access.system_ids ARRAY_CONTAINS Dx41wrLCM4QNYmxaMyc3`; também consultado `system_id EQUAL` para cobrir o campo direto. A união retornou 4 usuários e foi conferida contra varredura projetada dos 15 documentos da origem.
- Destino confirmado pelo exemplo: `pm-neogov-qa-lgpdweb`, banco `modules`, coleção `user-data` (43 documentos). O banco `gestao-de-dados` e a coleção `users-citizen` não são o destino indicado pelo exemplo.
- Identidade: `desenvolvimento@neogov.com.br`, autenticação existente do gcloud, sem impersonação configurada ou overrides CLOUDSDK_/GOOGLE_ encontrados. Projeto padrão observado: `dashboard-admin-481516`; todas as consultas usaram caminhos explícitos e nenhum default foi alterado.

## Critério de correspondência

O valor de authUserId deve ser o ID do documento da origem, não provider_uid. Compara-se provider_uid com o ID do documento de QA e confirma-se o e-mail; alternativamente, usa-se e-mail único após trim e comparação sem diferença de caixa. Emails duplicados no sistema de origem ou destino, divergência entre UID e e-mail, reutilização de authUserId e valores existentes conflitantes impedem qualquer associação automática. Não se filtrou por is_active: o pedido abrange todos os associados ao sistema; os quatro selecionados estavam ativos, assim como o tenant_access.

## Vínculo já correto

`modules/user-data/ac3YIwGPhraFkiKdqJRa4v290EB3`, e-mail `vitor.figueiredo@neogov.com.br`, possui `authUserId = 8E59kN4wHG8lus1P0p1M`. O documento de origem confirma o mesmo provider_uid, e-mail e participação no sistema LGPDweb. Releitura direcionada confirmou o vínculo.

## Usuários do Auth não sincronizados

Nenhum dos três abaixo foi localizado em `modules/user-data` de QA pelo provider_uid como ID do documento ou pelo e-mail normalizado. A releitura direta dos três IDs de destino retornou HTTP 404.

| E-mail | ID do documento Auth | provider_uid | Motivo |
| --- | --- | --- | --- |
| ratewof508@hideam.com | `Id5aungEvVHGlx9oyV5i` | `9r88tdeWtaZIPPlqhCykZZvoExK2` | Não encontrado em user-data de QA |
| yojayer103@ncleap.com | `Y1JsKZt2KkcYLnvTirCb` | `vs8S4M6fV2Q5QTLAVJQoWTZrBcJ3` | Não encontrado em user-data de QA |
| meliboy953@findize.com | `sfq33mFQQXToqBerTQyF` | `K2WkzFd5ZCRTsUcsS1KOjxILGqD3` | Não encontrado em user-data de QA |

Lista exportada em auth-nao-sincronizados.csv (auxiliar removido; resultado consolidado neste relatório).

## Documentos de QA sem correspondência no grupo LGPDweb do Auth

Dos 43 documentos de QA, o exemplo é o único associado ao grupo selecionado. Os outros 42 se distribuem em 31 sem correspondência por UID/e-mail no Auth dev, 1 correspondente a conta existente sem participação no LGPDweb e 10 sem e-mail e sem correspondência por provider_uid. Essa ausência de correspondência não prova que sejam a mesma pessoa com outro e-mail/UID. Duplicatas históricas de e-mail em QA não foram mescladas.

| ID do documento QA | E-mail | Motivo | Candidatos no Auth |
| --- | --- | --- | --- |
| `2kEDuYkFxVe3jX5nKF5rkuLsPH23` | joao@neogov.com.br | Sem correspondência por provider_uid ou e-mail no Auth dev | — |
| `5kh90QB7CmYhIPBOUi0Gd2eo6O93` | alberto.souza@neogov.com.br | Sem correspondência por provider_uid ou e-mail no Auth dev | — |
| `6LE7t8mE20hWuf5xLanr1UqelaC2` | francisco.gama@neogov.com.br | Conta existente no Auth dev, sem associação ao sistema LGPDweb | hGHUYpXDvzWwZIHXRsDc |
| `8FP7iXi4g5V5tKBdZ9YGh8Mghmd2` | joao@neogov.com.br | Sem correspondência por provider_uid ou e-mail no Auth dev | — |
| `8tBJHyKjVFXvYvgLiRZQCnxMHau2` | thiago.honorio@neogov.com.br | Sem correspondência por provider_uid ou e-mail no Auth dev | — |
| `B5Q9VGOHbqWnWneB7jclzq1ioNY2` | wesley.costa@neogov.com.br | Sem correspondência por provider_uid ou e-mail no Auth dev | — |
| `D2cucMG7FWbu5tTafpHGO5qbfDp1` | gu@teste.com | Sem correspondência por provider_uid ou e-mail no Auth dev | — |
| `DCEtTzoO1rhoh5ILWJ9He8SOqJJ2` | Ausente | QA sem e-mail e sem provider_uid correspondente no Auth dev | — |
| `G8CZBV1CabUITTJg9ITb5EjTUen1` | gustavo@teste.com.br | Sem correspondência por provider_uid ou e-mail no Auth dev | — |
| `HLw68lFJaxSOrmTI0phke1dkCDG2` | adilsonteste@email.com | Sem correspondência por provider_uid ou e-mail no Auth dev | — |
| `HyBzU3n4J0hdFzzPLo867eAXR903` | Ausente | QA sem e-mail e sem provider_uid correspondente no Auth dev | — |
| `ImUr1LDGIuS0kUA0UxGELdby3gN2` | gustavo@neogov.com.br | Sem correspondência por provider_uid ou e-mail no Auth dev | — |
| `Iro02Fi7srfV3AbARQR5tLV7VCI3` | Ausente | QA sem e-mail e sem provider_uid correspondente no Auth dev | — |
| `MIapHuGZRIW3HV6fYItWrXPbMxE2` | gustavo@neogov.com.br | Sem correspondência por provider_uid ou e-mail no Auth dev | — |
| `PYxZqu5vTyX6pQLIKcNCSr2UIi63` | teste-anonimizacao-ana@neogov.com.br | Sem correspondência por provider_uid ou e-mail no Auth dev | — |
| `PbTYSwgcetMxHPyxpW3RWBjmXcg1` | daniel-feijao@live.com | Sem correspondência por provider_uid ou e-mail no Auth dev | — |
| `RCsdoC4IcGQai6c276qZHzyMxDh1` | lennynggustdavog@gmail.com | Sem correspondência por provider_uid ou e-mail no Auth dev | — |
| `RtM9At1hVNg34ehjN2Uybj7UZsL2` | Ausente | QA sem e-mail e sem provider_uid correspondente no Auth dev | — |
| `S3g3Gfo2ibZ4KVe2dkYPewmCZT73` | Ausente | QA sem e-mail e sem provider_uid correspondente no Auth dev | — |
| `Sn1dXnRjzNPFwUoE5qNdyffSLhy1` | gustavo@gus.com | Sem correspondência por provider_uid ou e-mail no Auth dev | — |
| `Wc9CsVy0j2Mvk7m0wdyDhW1EFI22` | vinicius.rezende@neogov.com.br | Sem correspondência por provider_uid ou e-mail no Auth dev | — |
| `WwFmzShZwJYNJfg2BObKqCW5T8s2` | wesley.costa@neogov.com.br | Sem correspondência por provider_uid ou e-mail no Auth dev | — |
| `YpUvLwAL89dzvjckf8xuo0qdLBy2` | Ausente | QA sem e-mail e sem provider_uid correspondente no Auth dev | — |
| `Z7YVSh7w4zUBqcLycxEfdk9oSVw2` | Ausente | QA sem e-mail e sem provider_uid correspondente no Auth dev | — |
| `Z7xuoIIGBlPVn2ZKKnyLPXadAcP2` | desenvolvimento@neogov.com.br | Sem correspondência por provider_uid ou e-mail no Auth dev | — |
| `ZynNBmGI5WavziesgxtNaqbl9YF3` | thiago.honorio@neogov.com.br | Sem correspondência por provider_uid ou e-mail no Auth dev | — |
| `a3M5nncraSPC6o8J1LLz1vj8mk02` | Ausente | QA sem e-mail e sem provider_uid correspondente no Auth dev | — |
| `aN66wj1n4VX2YzvlfjQUoIngzAt2` | gustavo@teste.com | Sem correspondência por provider_uid ou e-mail no Auth dev | — |
| `abiyojG9TXTYq4o2f64pbrLYdLQ2` | lucas.assis@neogov.com.br | Sem correspondência por provider_uid ou e-mail no Auth dev | — |
| `cdJb2Zq5qRfCUBbEJuDH8gxiW4K2` | gustavo.henrique@neogov.com.br | Sem correspondência por provider_uid ou e-mail no Auth dev | — |
| `dxeohRcHEeTbISzgVIGkxlk4zM63` | adilson@neogov.com.br | Sem correspondência por provider_uid ou e-mail no Auth dev | — |
| `gDUHBVYKT3fN7BxQuLAhSrlf5x62` | root@root.com | Sem correspondência por provider_uid ou e-mail no Auth dev | — |
| `hhqDINpICRP9sRHLpHwwROGVWeW2` | lucas.assis@neogov.com.br | Sem correspondência por provider_uid ou e-mail no Auth dev | — |
| `j9nKhPPTLCXZ7UctVYaSwdYixIB3` | test@dka.com | Sem correspondência por provider_uid ou e-mail no Auth dev | — |
| `kMiC8oks5HQpEjeRRE2Xop2rKdv2` | teste-anonimizacao-ana@neogov.com.br | Sem correspondência por provider_uid ou e-mail no Auth dev | — |
| `kqK6OH8wz7To2E2BVhUhx3C828Z2` | gustavossssss@neogov.com.br | Sem correspondência por provider_uid ou e-mail no Auth dev | — |
| `nedXZujz6BUeRVJ3imQ1KzW2kPE3` | joao.doreto@neogov.com.br | Sem correspondência por provider_uid ou e-mail no Auth dev | — |
| `o8zgHrfHTvcvxb7byS7A9CaYDwo1` | alberto.souza@neogov.com.br | Sem correspondência por provider_uid ou e-mail no Auth dev | — |
| `rTfpsBWYHbbrMOaUSXRdiv63tXM2` | Ausente | QA sem e-mail e sem provider_uid correspondente no Auth dev | — |
| `rXP3qs4AvZfk7hOPcKQjR4Bt66I3` | adilson@neogov.com.br | Sem correspondência por provider_uid ou e-mail no Auth dev | — |
| `se4ZdLZ1Jkf9zjm9vyrQULGAOGA2` | desenvolvimento@neogov.com.br | Sem correspondência por provider_uid ou e-mail no Auth dev | — |
| `servico-relatorios` | Ausente | QA sem e-mail e sem provider_uid correspondente no Auth dev | — |

Lista exportada em qa-sem-correspondencia.csv (auxiliar removido; resultado consolidado neste relatório).

## Execução, evidências e verificações

- Consultados os bancos existentes nos dois projetos e os metadados das coleções para localizar o exemplo. Nas amostras iniciais foram retidos somente nomes de campos e valores permitidos de identificação; valores de senhas/segredos não foram exibidos nem salvos.
- Consultas seguintes limitaram os campos retornados por projeção. Nenhuma API foi ativada; não foram consultados valores de Secret Manager nem efetuado login.
- diagnostico.py (auxiliar removido; resultado consolidado neste relatório): consulta paginada de origem/destino e comparação; não contém operações de escrita remota. Reexecutar produz novas leituras e sobrescreve evidências desta solicitação; para nova solicitação, copiar para nova pasta exclusiva.
- evidencias-origem.json (auxiliar removido; resultado consolidado neste relatório): sistema confirmado, quatro usuários selecionados e três role bindings do LGPDweb. Todos os role bindings observados referem-se ao usuário do exemplo (dois inativos e um ativo); a seleção de usuários usa associação ao sistema, não apenas os papéis.
- evidencias-destino-antes.json (auxiliar removido; resultado consolidado neste relatório): 43 documentos com projeção de email, name e authUserId, além de metadados.
- plano.json (auxiliar removido; resultado consolidado neste relatório): resultado individual; 1 já sincronizado, 3 ausentes, 0 atualizações propostas.
- verificacao.json (auxiliar removido; resultado consolidado neste relatório): conferência independente dos 15 usuários, classificação dos 42 documentos de QA e releituras direcionadas (1 vínculo correto e 3 HTTP 404).
- Contexto do CLI inicialmente bloqueado por restrição do sandbox à pasta de configuração; consultas posteriores executadas com escalonamento permitido, mantendo a identidade e configuração existentes.
- Escritas remotas: **0**. Não houve indisponibilidade causada por mudança, criação de contas ou alteração de permissões. As leituras podem gerar cobrança normal de Firestore; não foi estimado custo monetário.
- Artefatos locais de dados com permissão 0600 e pasta da solicitação 0700. Não foram criados diretórios temporários; não há cache Python gerado nesta solicitação.

## Pendências e reversão

Para associar os três usuários ausentes, é necessário identificar documentos equivalentes já existentes com outra identificação ou definir o cadastro em QA. Criar documentos ou incluir outros usuários no sistema LGPDweb muda o escopo e requer definição/autorização específica; nenhuma dessas ações foi feita. Não se inferem perfis/permissões a partir dos cadastros existentes.

Não há rollback remoto: nenhum recurso GCP foi modificado e não foi necessário backup de campos. Os arquivos locais são o único estado criado; sua exclusão elimina a trilha desta solicitação e não altera o GCP. Os snapshots contêm apenas campos projetados e não servem como backup integral de documentos.

## Referência técnica

A projeção de campos das consultas segue a [documentação oficial de StructuredQuery](https://docs.cloud.google.com/firestore/docs/reference/rest/v1/StructuredQuery). Ela reduz os campos retornados; as consultas continuam sujeitas à cobrança de leitura.

## Continuação — criação de usuários ausentes no Auth

O resultado das seções anteriores registra a primeira etapa. O usuário alterou o escopo nesta continuação: ignorar os três usuários exclusivos do Auth, criar pela API os usuários de QA com e-mail que ainda não existem no Auth e depois preencher authUserId. Por instrução expressa, todos os registros continuam nesta pasta. A versão anterior do relatório está preservada em relatorio-etapa-1.md (auxiliar removido; resultado consolidado neste relatório).

### Diagnóstico atualizado

- 43 documentos em modules/user-data; 33 com e-mail e 10 sem e-mail, ignorados conforme o pedido.
- 24 e-mails distintos em QA; 2 já têm cadastro no tenant QA do Auth (Vitor e Francisco).
- 22 e-mails distintos ainda precisam de cadastro no tenant QA, correspondendo a 31 documentos. Nove e-mails estão duplicados em QA.
- Tenant confirmado por project_id: yHcGlIG4ZeBcy7V5DQSC, LGPDWeb QA, pm-neogov-qa-lgpdweb, ativo, com o sistema LGPDweb ativo. Não usar o tenant administrativo do emissor do token como destino.
- Francisco já existe no Auth (hGHUYpXDvzWwZIHXRsDc), mas tem somente o sistema Gestão de Dados. Não foi duplicado nem incluído em outro sistema; isso permanece como caso separado da criação de ausentes.

### API e impedimentos

Foi lida a [documentação indicada pelo usuário](https://api.auth-develop.neogov.com.br/docs), obtendo o contrato Swagger em /docs/swagger-ui-init.js. /openapi.json retornou 404. O snapshot público está em api-openapi.json (auxiliar removido; resultado consolidado neste relatório).

POST /users exige Bearer e x-api-key. No contrato de plataforma exige tenant_id, email, password, accesses.system_ids e username opcional. Nenhuma role é concedida pelo cadastro. Uma única consulta GET /users?limit=1 usando apenas o token fornecido retornou HTTP 401, mensagem Invalid credentials. Não é possível distinguir pela mensagem se há também outro problema com o token; a especificação confirma que ele sozinho não supre as credenciais documentadas. A referência autorizada da API key de plataforma foi solicitada, sem solicitar seu valor no chat e sem tentar outra identidade ou criar/rotacionar chaves.

Também foram solicitadas decisões sobre os nove e-mails duplicados de QA e as senhas iniciais obrigatórias. A proposta é gerar uma senha forte e individual em memória, sem guardar valores, e associar duplicatas somente ao documento cujo ID coincida com provider_uid, mantendo os demais pendentes, salvo orientação expressa diferente.

### Plano preparado e impactos

Criar uma conta por e-mail ausente, somente no tenant QA e no sistema LGPDweb, pela API indicada, sem atribuir roles. Verificar cada resposta e reler o usuário no Firestore; só então preencher authUserId nos documentos de QA autorizados. Antes de cada gravação, reler o destino, confirmar o e-mail e o campo anterior, salvar backup do campo e usar precondição updateTime e máscara exclusiva de authUserId. Em falhas de criação, consultar o estado antes de qualquer nova tentativa, evitando duplicação.

Os efeitos possíveis incluem contas novas no provedor de identidade do tenant, custos de API/Firestore e novos vínculos de acesso ao sistema. E-mails duplicados podem levar dois documentos e seus dados/permissões à mesma identidade; essa decisão permanece pendente. O contrato não documenta envio de mensagem no cadastro, portanto esse efeito não foi confirmado. Nenhuma rota de recuperação de senha foi executada. Descartar as senhas propostas implica que os usuários precisarão de recuperação de senha para acessá-las.

A reversão futura de authUserId deve restaurar somente o campo alterado, com backup e verificação de concorrência. A API documenta inativação de usuários, sem exclusão física; inativar uma conta criada não apaga cadastros nem auditoria, e não desfaz eventual comunicação enviada. Rollback remoto não foi executado e dependerá de autorização caso necessário.

### Artefatos e estado

- etapa2-plano.json (auxiliar removido; resultado consolidado neste relatório): 22 payloads de cadastro sem segredos, documentos relacionados e casos pendentes.
- etapa2-cadastros-propostos.csv (auxiliar removido; resultado consolidado neste relatório): lista de e-mails, nomes e IDs de QA a cadastrar/associar.
- etapa2-qa-antes.json (auxiliar removido; resultado consolidado neste relatório), etapa2-auth-antes.json (auxiliar removido; resultado consolidado neste relatório), etapa2-tenants.json (auxiliar removido; resultado consolidado neste relatório): snapshots projetados da nova leitura.
- etapa2-verificacao-api.json (auxiliar removido; resultado consolidado neste relatório) e verificar-api.py (auxiliar removido; resultado consolidado neste relatório): evidência e procedimento da consulta GET; token recebido por entrada oculta, mantido em memória, sem valor em arquivo.

Estado: preparação concluída; criação e associação ainda não executadas, aguardando a credencial adicional e as decisões solicitadas. Escritas remotas nesta continuação: 0. Nenhum diretório temporário/cache foi criado. Os arquivos contêm apenas dados necessários ao pedido e têm acesso local restrito.

## Etapa 3 — criação direta na coleção users

O usuário substituiu expressamente a criação pela API por cadastro direto no Firestore, pois as identidades já existem no provider. Também confirmou que duplicatas de QA devem ser associadas somente quando o ID do documento coincide com provider_uid. A API key fornecida não foi usada ou armazenada, e nenhuma senha foi criada. O relatório imediatamente anterior foi preservado em relatorio-etapa-2.md (auxiliar removido; resultado consolidado neste relatório).

### Diagnóstico e escopo efetivo

O tenant `yHcGlIG4ZeBcy7V5DQSC` confirma o projeto `pm-neogov-qa-lgpdweb` e o domínio Firebase `pm-neogov-qa-lgpdweb.firebaseapp.com`. O sistema LGPDweb é `Dx41wrLCM4QNYmxaMyc3`. Por consulta OAuth com a identidade existente do gcloud, foram buscados os 24 e-mails distintos e, em consulta separada, os 33 IDs de documentos de QA com e-mail. As duas consultas confirmaram as mesmas 10 identidades no Firebase QA: 8 ainda ausentes no Auth, Vitor já sincronizado e Francisco com cadastro divergente. As demais contas não foram presumidas a partir de documentos históricos.

As criações ocorreram somente em `projects/neogov-auth-dev/databases/auth-db-dev/documents/users`. Os vínculos foram preenchidos somente em `projects/pm-neogov-qa-lgpdweb/databases/modules/documents/user-data`. A identidade GCP permaneceu `desenvolvimento@neogov.com.br`, sem login ou troca de configuração.

### Campos e execução

Cada novo documento tem ID aleatório de 20 caracteres, seguindo o padrão Firestore existente, e contém `email`, `username`, `provider_uid`, `is_active=true`, `created_at`, `updated_at` e `tenant_access`. O mapa de acesso contém `id` do tenant QA, `is_active=true`, somente o ID do sistema LGPDweb em `system_ids`, `granted_at` e `updated_at`. As quatro datas usam timestamp do servidor, assim como o tipo observado no exemplo. Não foram copiados acessos a outros sistemas, criadas roles ou modificadas contas/senhas do Firebase. A escrita direta não chama a auditoria da API de negócio.

Antes da gravação foram relidos o tenant, os usuários Auth, os oito documentos QA e as oito identidades Firebase. O commit Auth criou os oito documentos com precondição `exists=false`; após releitura dos oito, o commit QA escreveu somente `authUserId` com máscara de campo e precondição `updateTime`. O backup registra presença/ausência e valor anterior de cada campo. São dois commits em bancos distintos, sem atomicidade entre bancos; ambos concluíram e foram verificados.

### Usuários criados e associados

| E-mail | ID do documento Auth / authUserId | ID QA = provider_uid |
| --- | --- | --- |
| adilson@neogov.com.br | `ycZalfKwPOf4rPR7zg9Y` | `dxeohRcHEeTbISzgVIGkxlk4zM63` |
| alberto.souza@neogov.com.br | `sHdb0auoLOJ5BpVLxHI7` | `5kh90QB7CmYhIPBOUi0Gd2eo6O93` |
| desenvolvimento@neogov.com.br | `Ic7l5LhO8hhxe2S4RN5P` | `Z7xuoIIGBlPVn2ZKKnyLPXadAcP2` |
| gustavo.henrique@neogov.com.br | `gczPoTRG1Z2Q6wXGOTpD` | `cdJb2Zq5qRfCUBbEJuDH8gxiW4K2` |
| gustavo@neogov.com.br | `af2eYsZnE35O9qqzMd7w` | `ImUr1LDGIuS0kUA0UxGELdby3gN2` |
| lucas.assis@neogov.com.br | `OcjBMeme8Yr4nzjXjFps` | `hhqDINpICRP9sRHLpHwwROGVWeW2` |
| vinicius.rezende@neogov.com.br | `YGMZXGfsx8lw2ptuMZZh` | `Wc9CsVy0j2Mvk7m0wdyDhW1EFI22` |
| wesley.costa@neogov.com.br | `TjDUbcZvYeANnFHnleJh` | `WwFmzShZwJYNJfg2BObKqCW5T8s2` |

### Pendências e documentos ignorados

| Categoria | E-mails distintos | Documentos QA |
| --- | ---: | ---: |
| Não localizados no provider por e-mail/UID | 14 | 17 |
| Duplicatas cujo ID difere do UID real | 6 | 6 |
| Cadastro existente divergente: Francisco | 1 | 1 |
| Sem e-mail, ignorados | — | 10 |

Francisco (`francisco.gama@neogov.com.br`) já possui o documento Auth `hGHUYpXDvzWwZIHXRsDc`, com `provider_uid=KtzzwIiTTtWd1eiaiEmWJRZGLca2` e acesso somente ao sistema Gestão de Dados. O provider de QA retorna o UID `6LE7t8mE20hWuf5xLanr1UqelaC2`, que coincide com seu documento em QA. Não foi criado cadastro duplicado, alterado esse UID ou ampliado o acesso do cadastro existente. Esse caso requer definição e autorização de correção específica.

| E-mail | Documento QA | Motivo |
| --- | --- | --- |
| francisco.gama@neogov.com.br | `6LE7t8mE20hWuf5xLanr1UqelaC2` | Já existe no Auth com provider_uid divergente e sem associação ao LGPDweb |
| adilson@neogov.com.br | `rXP3qs4AvZfk7hOPcKQjR4Bt66I3` | Duplicata: ID de QA difere do UID real no provider |
| alberto.souza@neogov.com.br | `o8zgHrfHTvcvxb7byS7A9CaYDwo1` | Duplicata: ID de QA difere do UID real no provider |
| desenvolvimento@neogov.com.br | `se4ZdLZ1Jkf9zjm9vyrQULGAOGA2` | Duplicata: ID de QA difere do UID real no provider |
| gustavo@neogov.com.br | `MIapHuGZRIW3HV6fYItWrXPbMxE2` | Duplicata: ID de QA difere do UID real no provider |
| lucas.assis@neogov.com.br | `abiyojG9TXTYq4o2f64pbrLYdLQ2` | Duplicata: ID de QA difere do UID real no provider |
| wesley.costa@neogov.com.br | `B5Q9VGOHbqWnWneB7jclzq1ioNY2` | Duplicata: ID de QA difere do UID real no provider |
| adilsonteste@email.com | `HLw68lFJaxSOrmTI0phke1dkCDG2` | Conta não localizada no Firebase QA por e-mail nem pelo ID do documento QA |
| daniel-feijao@live.com | `PbTYSwgcetMxHPyxpW3RWBjmXcg1` | Conta não localizada no Firebase QA por e-mail nem pelo ID do documento QA |
| gu@teste.com | `D2cucMG7FWbu5tTafpHGO5qbfDp1` | Conta não localizada no Firebase QA por e-mail nem pelo ID do documento QA |
| gustavo@gus.com | `Sn1dXnRjzNPFwUoE5qNdyffSLhy1` | Conta não localizada no Firebase QA por e-mail nem pelo ID do documento QA |
| gustavo@teste.com | `aN66wj1n4VX2YzvlfjQUoIngzAt2` | Conta não localizada no Firebase QA por e-mail nem pelo ID do documento QA |
| gustavo@teste.com.br | `G8CZBV1CabUITTJg9ITb5EjTUen1` | Conta não localizada no Firebase QA por e-mail nem pelo ID do documento QA |
| gustavossssss@neogov.com.br | `kqK6OH8wz7To2E2BVhUhx3C828Z2` | Conta não localizada no Firebase QA por e-mail nem pelo ID do documento QA |
| joao.doreto@neogov.com.br | `nedXZujz6BUeRVJ3imQ1KzW2kPE3` | Conta não localizada no Firebase QA por e-mail nem pelo ID do documento QA |
| joao@neogov.com.br | `2kEDuYkFxVe3jX5nKF5rkuLsPH23` | Conta não localizada no Firebase QA por e-mail nem pelo ID do documento QA |
| joao@neogov.com.br | `8FP7iXi4g5V5tKBdZ9YGh8Mghmd2` | Conta não localizada no Firebase QA por e-mail nem pelo ID do documento QA |
| lennynggustdavog@gmail.com | `RCsdoC4IcGQai6c276qZHzyMxDh1` | Conta não localizada no Firebase QA por e-mail nem pelo ID do documento QA |
| root@root.com | `gDUHBVYKT3fN7BxQuLAhSrlf5x62` | Conta não localizada no Firebase QA por e-mail nem pelo ID do documento QA |
| test@dka.com | `j9nKhPPTLCXZ7UctVYaSwdYixIB3` | Conta não localizada no Firebase QA por e-mail nem pelo ID do documento QA |
| teste-anonimizacao-ana@neogov.com.br | `PYxZqu5vTyX6pQLIKcNCSr2UIi63` | Conta não localizada no Firebase QA por e-mail nem pelo ID do documento QA |
| teste-anonimizacao-ana@neogov.com.br | `kMiC8oks5HQpEjeRRE2Xop2rKdv2` | Conta não localizada no Firebase QA por e-mail nem pelo ID do documento QA |
| thiago.honorio@neogov.com.br | `8tBJHyKjVFXvYvgLiRZQCnxMHau2` | Conta não localizada no Firebase QA por e-mail nem pelo ID do documento QA |
| thiago.honorio@neogov.com.br | `ZynNBmGI5WavziesgxtNaqbl9YF3` | Conta não localizada no Firebase QA por e-mail nem pelo ID do documento QA |
| Ausente | `DCEtTzoO1rhoh5ILWJ9He8SOqJJ2` | Ignorado: documento sem e-mail |
| Ausente | `HyBzU3n4J0hdFzzPLo867eAXR903` | Ignorado: documento sem e-mail |
| Ausente | `Iro02Fi7srfV3AbARQR5tLV7VCI3` | Ignorado: documento sem e-mail |
| Ausente | `RtM9At1hVNg34ehjN2Uybj7UZsL2` | Ignorado: documento sem e-mail |
| Ausente | `S3g3Gfo2ibZ4KVe2dkYPewmCZT73` | Ignorado: documento sem e-mail |
| Ausente | `YpUvLwAL89dzvjckf8xuo0qdLBy2` | Ignorado: documento sem e-mail |
| Ausente | `Z7YVSh7w4zUBqcLycxEfdk9oSVw2` | Ignorado: documento sem e-mail |
| Ausente | `a3M5nncraSPC6o8J1LLz1vj8mk02` | Ignorado: documento sem e-mail |
| Ausente | `rTfpsBWYHbbrMOaUSXRdiv63tXM2` | Ignorado: documento sem e-mail |
| Ausente | `servico-relatorios` | Ignorado: documento sem e-mail |

### Verificação

- Auth: passou de 15 para 23 documentos; os 15 documentos preexistentes permaneceram iguais no snapshot projetado, incluindo updateTime.
- QA: permaneceu com 43 documentos; os 8 authUserId correspondem aos IDs Auth criados. Nome e e-mail desses oito foram preservados; os outros 35 documentos permaneceram iguais no snapshot projetado, incluindo updateTime.
- As oito identidades do provider mantiveram UID, e-mail e status. Nenhuma chamada de modificação ao provider foi realizada.
- Os oito novos documentos apresentam UID, tenant, sistema, campos e tipos esperados. Não há senhas, tokens ou API keys nos artefatos.
- A primeira tentativa de iniciar a execução não foi criada porque a revisão automática de aprovação excedeu o prazo. A ausência de marcador/recibos foi confirmada antes da única repetição permitida, que executou os dois commits.
- A revisão automática também expirou antes de iniciar uma consulta de verificação. A consulta foi repetida uma vez, separando as leituras remotas da comparação local; as leituras e a comparação concluíram com sucesso. Não houve repetição de commits concluídos.

### Evidências finais

- cadastro-direto.py (auxiliar removido; resultado consolidado neste relatório): preparação e gravações delimitadas; uma execução iniciada bloqueia repetição automática.
- etapa3-plano.json (auxiliar removido; resultado consolidado neste relatório): oito novos IDs, campos, vínculos e 34 documentos pendentes/ignorados.
- etapa3-provider.json (auxiliar removido; resultado consolidado neste relatório), etapa3-provider-por-uid.json (auxiliar removido; resultado consolidado neste relatório), etapa3-provider-depois.json (auxiliar removido; resultado consolidado neste relatório): consultas projetadas do provider, sem hashes/senhas/tokens.
- etapa3-modelo-user.json (auxiliar removido; resultado consolidado neste relatório) e etapa3-tenant.json (auxiliar removido; resultado consolidado neste relatório): modelo de campos e configuração não secreta.
- etapa3-auth-antes.json (auxiliar removido; resultado consolidado neste relatório), etapa3-auth-depois.json (auxiliar removido; resultado consolidado neste relatório), etapa3-qa-antes.json (auxiliar removido; resultado consolidado neste relatório) e etapa3-qa-depois.json (auxiliar removido; resultado consolidado neste relatório): snapshots projetados antes/depois.
- etapa3-backup-authUserId.json (auxiliar removido; resultado consolidado neste relatório): presença e valores anteriores dos oito campos.
- etapa3-recibo-auth.json (auxiliar removido; resultado consolidado neste relatório), etapa3-recibo-qa.json (auxiliar removido; resultado consolidado neste relatório) e etapa3-execucao-iniciada.json (auxiliar removido; resultado consolidado neste relatório): commits e marcador de execução.
- verificar-cadastro.py (auxiliar removido; resultado consolidado neste relatório) e etapa3-verificacao.json (auxiliar removido; resultado consolidado neste relatório): verificações independentes dos snapshots finais.
- [etapa3-sincronizados.csv](etapa3-sincronizados.csv) e etapa3-pendencias.csv (auxiliar removido; resultado consolidado neste relatório): listas finais de resultados.
- Arquivos com acesso local 0600, pasta 0700; nenhum temporário ou cache Python criado. O token mantido na memória da ferramenta para o teste anterior foi descartado.

### Reversão e limites

O arquivo etapa3-rollback-nao-executado.json (auxiliar removido; resultado consolidado neste relatório) contém os payloads exatos, sem credenciais. Não foi executado. Após autorização e conferência de uso posterior: primeiro restaurar os oito campos de QA com o backup (remover authUserId quando antes ausente); depois remover somente os oito documentos Auth criados nesta etapa. Cada operação exige o updateTime da verificação final, portanto alterações posteriores interrompem a reversão e exigem revisão. Não remover documentos cuja origem ou uso posterior estejam incertos.

A reversão usa dois commits, sem transação entre bancos, e não desfaz sessões, dependências ou eventuais efeitos de uso posterior. Como não houve alteração no provider, não é necessário restaurar contas ou senhas Firebase. Os snapshots projetados não são backup integral dos documentos QA. Leituras e 16 escritas de documentos geram cobrança normal; não foi feito cálculo monetário.

As consultas de UID por OAuth seguem a [documentação oficial de accounts.lookup](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v1/projects.accounts/lookup). As precondições de criação/atualização seguem a [documentação oficial do Firestore](https://docs.cloud.google.com/firestore/docs/reference/rest/v1/Precondition).

## Etapa 4 — remoção autorizada dos cadastros sem identidade no provider

Prompt: “esses q o email nã foi encoontrado no provider, pode remover / ignore oos sem email”. O escopo corresponde aos 17 documentos da lista anterior de ausentes no provider, em `projects/pm-neogov-qa-lgpdweb/databases/modules/documents/user-data`. As seis duplicatas com identidade confirmada, o caso divergente de Francisco e os dez documentos sem e-mail não pertencem à lista de remoção. Por determinação do usuário, esta etapa continua na mesma pasta de solicitação. Relatório anterior preservado em relatorio-etapa-3.md (auxiliar removido; resultado consolidado neste relatório).

### Diagnóstico, impactos e proteção

Antes da exclusão, novas consultas ao Firebase QA confirmaram zero correspondências para os 14 e-mails e os 17 IDs. Foram lidos os documentos completos, conferidos seus e-mails e ausência de authUserId e gravado backup integral com permissão 0600, após checagem de campos e formatos conhecidos de segredo. Não foi necessário omitir campos dos documentos. O backup contém dados pessoais e configurações dos cadastros e deve manter acesso restrito.

A consulta das subcoleções encontrou `course-progress` sob `user-data/8FP7iXi4g5V5tKBdZ9YGh8Mghmd2`. O usuário foi informado antes da gravação de que o histórico permaneceria com o pai ausente. A exclusão foi limitada aos documentos de cadastro, sem exclusão recursiva ou propagação a documentos referenciados. Outros vínculos históricos podem permanecer fora de user-data; não houve varredura ou remoção dessas dependências.

Os impactos expostos foram perda dos dados/configurações dos cadastros e possíveis referências sem cadastro. A solução atende ao pedido eliminando os cadastros QA cujo e-mail/UID não tem identidade confirmada no provider. As leituras de conferência e 17 exclusões geram cobrança normal do Firestore; não foi calculado valor monetário.

### Execução e verificação

Imediatamente antes de excluir, os e-mails e IDs foram consultados novamente no provider e todos os documentos foram relidos e comparados integralmente com o backup. Um único commit Firestore excluiu os 17 documentos, cada qual com precondição updateTime. O marcador de início impede repetição automática da operação. O commit foi aceito e uma nova consulta independente comprovou:

- Coleção QA: 43 documentos antes, 26 depois, exatamente os 17 IDs autorizados ausentes.
- Os 17 GETs direcionados retornaram HTTP 404.
- Os outros 26 documentos permaneceram iguais no snapshot projetado de e-mail, nome e authUserId, incluindo updateTime; os 10 sem e-mail foram preservados.
- Todos os 23 documentos do Auth permaneceram iguais no snapshot projetado de identificação/acesso, incluindo updateTime.
- A subcoleção course-progress permaneceu igual na projeção de IDs e updateTime: 2 documento(s).

### Documentos removidos

| E-mail | ID QA removido |
| --- | --- |
| adilsonteste@email.com | `HLw68lFJaxSOrmTI0phke1dkCDG2` |
| daniel-feijao@live.com | `PbTYSwgcetMxHPyxpW3RWBjmXcg1` |
| gu@teste.com | `D2cucMG7FWbu5tTafpHGO5qbfDp1` |
| gustavo@gus.com | `Sn1dXnRjzNPFwUoE5qNdyffSLhy1` |
| gustavo@teste.com | `aN66wj1n4VX2YzvlfjQUoIngzAt2` |
| gustavo@teste.com.br | `G8CZBV1CabUITTJg9ITb5EjTUen1` |
| gustavossssss@neogov.com.br | `kqK6OH8wz7To2E2BVhUhx3C828Z2` |
| joao.doreto@neogov.com.br | `nedXZujz6BUeRVJ3imQ1KzW2kPE3` |
| joao@neogov.com.br | `2kEDuYkFxVe3jX5nKF5rkuLsPH23` |
| joao@neogov.com.br | `8FP7iXi4g5V5tKBdZ9YGh8Mghmd2` |
| lennynggustdavog@gmail.com | `RCsdoC4IcGQai6c276qZHzyMxDh1` |
| root@root.com | `gDUHBVYKT3fN7BxQuLAhSrlf5x62` |
| test@dka.com | `j9nKhPPTLCXZ7UctVYaSwdYixIB3` |
| teste-anonimizacao-ana@neogov.com.br | `PYxZqu5vTyX6pQLIKcNCSr2UIi63` |
| teste-anonimizacao-ana@neogov.com.br | `kMiC8oks5HQpEjeRRE2Xop2rKdv2` |
| thiago.honorio@neogov.com.br | `8tBJHyKjVFXvYvgLiRZQCnxMHau2` |
| thiago.honorio@neogov.com.br | `ZynNBmGI5WavziesgxtNaqbl9YF3` |

### Evidências

- remover-sem-provider.py (auxiliar removido; resultado consolidado neste relatório): preparação, commit de exclusão delimitado e consultas de verificação.
- etapa4-plano.json (auxiliar removido; resultado consolidado neste relatório): caminhos exatos, e-mails, updateTime e subcoleções encontradas.
- etapa4-backup-integral-qa.json (auxiliar removido; resultado consolidado neste relatório): documentos completos necessários à restauração.
- etapa4-provider-antes.json (auxiliar removido; resultado consolidado neste relatório): ausência de correspondência por e-mail/UID.
- etapa4-qa-antes.json (auxiliar removido; resultado consolidado neste relatório), etapa4-qa-depois.json (auxiliar removido; resultado consolidado neste relatório), etapa4-auth-antes.json (auxiliar removido; resultado consolidado neste relatório) e etapa4-auth-depois.json (auxiliar removido; resultado consolidado neste relatório): snapshots projetados.
- etapa4-subcolecoes-antes.json (auxiliar removido; resultado consolidado neste relatório) e etapa4-subcolecoes-depois.json (auxiliar removido; resultado consolidado neste relatório): IDs/metadados do histórico preservado.
- etapa4-recibo-exclusao.json (auxiliar removido; resultado consolidado neste relatório), etapa4-execucao-iniciada.json (auxiliar removido; resultado consolidado neste relatório) e etapa4-verificacao.json (auxiliar removido; resultado consolidado neste relatório): recibo e evidências de conclusão.
- [etapa4-removidos.csv](etapa4-removidos.csv) e [etapa4-pendencias-atuais.csv](etapa4-pendencias-atuais.csv): resultados atuais.
- Nenhuma credencial foi gravada. Arquivos 0600, pasta 0700. Não foram criados temporários ou caches Python.

### Restauração e limites

O arquivo etapa4-restauracao-nao-executada.json (auxiliar removido; resultado consolidado neste relatório) contém os 17 payloads de recriação por commit, com os campos completos do backup e precondição exists=false. A restauração não foi executada. Confirmar autorização e situação atual antes de usá-lo; se algum ID já existir, interromper e revisar em vez de sobrescrever.

A recriação preserva campos de negócio e IDs, mas gera novos metadados Firestore createTime/updateTime. Não desfaz efeitos de uso posteriores à exclusão, nem remove referências históricas. A subcoleção preservada volta a ter seu pai se o mesmo ID for recriado. Nenhuma conta, senha ou configuração do provider foi alterada nesta etapa.
