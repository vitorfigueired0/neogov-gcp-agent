# Contexto

Data: 2026-11-11T15:43:07.515079-03:00

## Prompt recebido

> preciso que faça uma adequação:
> busque todos os usuários salvos no projeto da api auth (neogov-auth-dev) que estejam no sistema lgdpweb (system_id condizente)
> depois, quero que pegue o id do documento desses usuários e assoocie eles na collection do proojeto lgdpweb qa, coomo o usuário ac3YIwGPhraFkiKdqJRa4v290EB3 ja está, com o campo **authUserId**
>
> e queroo que me traga os que não fooram sincronizados por não existir ou algo assim

## Resumo técnico

Objetivo: associar documentos de usuários do Auth de desenvolvimento aos usuários existentes do LGPDweb QA pelo campo authUserId e listar não sincronizados e seus motivos.
Origem: neogov-auth-dev; referência histórica do banco auth-db-dev.
Destino: pm-neogov-qa-lgpdweb, ambiente QA confirmado no catálogo; banco e coleção específicos serão confirmados por consulta.
Exemplo informado: ac3YIwGPhraFkiKdqJRa4v290EB3.
A confirmar: system_id do LGPDweb, coleção de usuários, chave de correspondência e conflitos.
Restrições: usar identidade existente do gcloud; não criar usuários; não modificar origem, identidade ou configuração do CLI; preservar campos fora de authUserId; não associar correspondências ambíguas; manter backups e evidências sanitizadas.
Impactos expostos previamente: leituras/escritas cobradas pelo Firestore; possível associação incorreta; registros locais com identificadores/e-mails e acesso restrito. Verificação por releitura e reversão por backup dos campos afetados.

## Continuação autorizada — 2026-11-11T16:38:32.597977-03:00

> durante esse chat, não crie mais solicitaçõoes, vamos trabalhar me cima apenas dessa atual
>
> soobre os usuários que existem noo projetoo de auth e não no lgpdweb, poode ignorar
> agora para os que existem no lgpdweb e não noo auth, quero que faça a criação deles, apenas os que possuem email, segue a doc da api de auth:
> [https://api.auth-develop.neogov.com.br/docs](https://api.auth-develop.neogov.com.br/docs)
>
> para criar, use o token:
> [SEGREDO OMITIDO]
>
> após a criação, faça a associação dos IDS

Escopo atualizado: criar pela API Auth dev os usuários de QA com e-mail e ainda ausentes no Auth, depois associar os IDs retornados em modules/user-data. Ignorar os três usuários exclusivos do Auth. Preservar a mesma pasta por instrução expressa do usuário. Token fornecido para uso apenas na API; autenticação GCP continua pelo CLI existente. A definir pela documentação: payload, tenant/system, duplicatas, senha e efeitos de notificação.

## Continuação — cadastro direto no Firestore — 2026-11-11T16:43:10.984165-03:00

O usuário forneceu uma API key ([SEGREDO OMITIDO]), escolheu associar duplicatas apenas ao documento cujo ID coincidir com provider_uid e recusou seguir com senhas iniciais, indicando outro caminho. A API key não foi utilizada.

> criar pela api n faz sentido ja que eles ja existem no proovider
> pode gcriar apenas na collection seguindo o padrão do que ja existe

Escopo vigente: criar somente os documentos users ausentes no Auth dev, com UIDs conferidos no provider existente, no tenant de QA e sistema LGPDweb. Associar os IDs de documento Auth em user-data de QA. Não chamar API de criação nem modificar contas Firebase, senhas, chaves ou roles. Mantém-se a política expressa para duplicatas. Impactos e reversão expostos antes das escritas.

## Continuação — remoção de QA sem identidade no provider — 2026-11-11T17:47:45.432703-03:00

> esses q o email nã foi encoontrado no provider, pode remover
> ignore oos sem email

Escopo autorizado: excluir os 17 documentos de modules/user-data, pm-neogov-qa-lgpdweb, correspondentes aos 14 e-mails da lista de ausentes no Firebase QA (etapa3-plano.json). Ignorar os 10 documentos sem e-mail. Antes da exclusão: reconfirmar ausência por e-mail e UID, salvar backup dos documentos sem segredos, verificar concorrência e expor impactos. Exclusão limitada aos documentos de cadastro, sem limpeza recursiva ou propagação para outras coleções. Verificação por ausência/HTTP 404 e igualdade dos outros documentos. Reversão por recriação a partir do backup, sem recuperar os metadados originais createTime/updateTime ou efeitos posteriores.
