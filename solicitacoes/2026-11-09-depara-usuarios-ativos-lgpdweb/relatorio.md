# Relatório — ID do documento × UID do Firebase Authentication

Coleta: 2026-11-09T15:22:01.749408-03:00 a 2026-11-09T15:22:18.536172-03:00 (America/Sao_Paulo).

## Resultado

Foram consultados com sucesso os **29 projetos** fornecidos pelo usuário, no banco Firestore **modules**, coleção **user-data**, e as contas correspondentes no Firebase Authentication do mesmo projeto.

- Documentos exportados: **426**.
- ID do documento igual ao UID do Auth: **373**.
- ID do documento diferente do UID do Auth: **6**, todos em **pm-neogov-qa-lgpdweb**.
- Comparação não confirmada: **47** — 29 documentos sem e-mail e 18 com e-mail não localizado no Auth do mesmo projeto.
- Contas desativadas confirmadas: **2**, em **cisalp-lgpdweb**, com IDs iguais aos UIDs. Esse total se sobrepõe às comparações iguais.
- Falhas pendentes de consulta: **0**.

Os números contam documentos do Firestore, não necessariamente pessoas únicas. Em QA, 9 e-mails estão repetidos em mais de um documento.

## Entregáveis

- [Todos os CSVs em ZIP](usuarios-depara-lgpdweb.zip).
- [Resumo por projeto](resumo-projetos.csv).
- [Verificação dos arquivos](verificacao.json) e [manifesto SHA-256](manifesto-sha256.json).

CSVs em UTF-8 com BOM, separador ponto e vírgula, uma linha por documento, incluindo contas ativas e desativadas.

| Projeto / CSV | Documentos | Iguais | Diferentes | Não confirmados | Desativados |
| --- | ---: | ---: | ---: | ---: | ---: |
| [pm-itaguai-rj-lgpdweb](csv/pm-itaguai-rj-lgpdweb.csv) | 10 | 10 | 0 | 0 | 0 |
| [pm-neogov-qa-lgpdweb](csv/pm-neogov-qa-lgpdweb.csv) | 43 | 10 | 6 | 27 | 0 |
| [lgpdweb](csv/lgpdweb.csv) | 11 | 11 | 0 | 0 | 0 |
| [camaraconceicaoalagoaslgpdweb](csv/camaraconceicaoalagoaslgpdweb.csv) | 12 | 12 | 0 | 0 | 0 |
| [pm-tupaciguara-mg-lgpdweb](csv/pm-tupaciguara-mg-lgpdweb.csv) | 11 | 11 | 0 | 0 | 0 |
| [pm-pedrinopolis-lgpdweb](csv/pm-pedrinopolis-lgpdweb.csv) | 13 | 13 | 0 | 0 | 0 |
| [frutallgpdweb-3dab8](csv/frutallgpdweb-3dab8.csv) | 15 | 13 | 0 | 2 | 0 |
| [cm-campo-florido-lgpdweb](csv/cm-campo-florido-lgpdweb.csv) | 15 | 15 | 0 | 0 | 0 |
| [prefeiturateresopolislgpdweb](csv/prefeiturateresopolislgpdweb.csv) | 12 | 12 | 0 | 0 | 0 |
| [pmsgalgpdweb-32cf8](csv/pmsgalgpdweb-32cf8.csv) | 13 | 13 | 0 | 0 | 0 |
| [pmdeltamglgpdweb](csv/pmdeltamglgpdweb.csv) | 13 | 13 | 0 | 0 | 0 |
| [prefeituraituiutabalgpdweb](csv/prefeituraituiutabalgpdweb.csv) | 14 | 14 | 0 | 0 | 0 |
| [novapontelgpdweb](csv/novapontelgpdweb.csv) | 13 | 13 | 0 | 0 | 0 |
| [cm-estrela-do-sul-lgpdweb](csv/cm-estrela-do-sul-lgpdweb.csv) | 12 | 12 | 0 | 0 | 0 |
| [pm-estreladosul-mg-lgpdweb](csv/pm-estreladosul-mg-lgpdweb.csv) | 14 | 14 | 0 | 0 | 0 |
| [cm-araguari-lgpdweb](csv/cm-araguari-lgpdweb.csv) | 14 | 14 | 0 | 0 | 0 |
| [pm-machado-lgpdweb](csv/pm-machado-lgpdweb.csv) | 14 | 13 | 0 | 1 | 0 |
| [lgpdwebsaaeituiutaba](csv/lgpdwebsaaeituiutaba.csv) | 15 | 13 | 0 | 2 | 0 |
| [camarafrutallgpdweb](csv/camarafrutallgpdweb.csv) | 14 | 13 | 0 | 1 | 0 |
| [saosimaolgpdweb-1a6e5](csv/saosimaolgpdweb-1a6e5.csv) | 13 | 13 | 0 | 0 | 0 |
| [camarateresopolislgpdweb](csv/camarateresopolislgpdweb.csv) | 13 | 13 | 0 | 0 | 0 |
| [pm-sao-joao-del-rei-mg](csv/pm-sao-joao-del-rei-mg.csv) | 11 | 11 | 0 | 0 | 0 |
| [pm-montecarmelo-mg-lgpdweb](csv/pm-montecarmelo-mg-lgpdweb.csv) | 13 | 13 | 0 | 0 | 0 |
| [cides-lgpdweb](csv/cides-lgpdweb.csv) | 11 | 11 | 0 | 0 | 0 |
| [cisalp-lgpdweb](csv/cisalp-lgpdweb.csv) | 13 | 13 | 0 | 0 | 2 |
| [neogov-default](csv/neogov-default.csv) | 32 | 22 | 0 | 10 | 0 |
| [cachoeiradouradamglgpdweb](csv/cachoeiradouradamglgpdweb.csv) | 17 | 14 | 0 | 3 | 0 |
| [camaraituiutabalgpdweb-a1a06](csv/camaraituiutabalgpdweb-a1a06.csv) | 14 | 13 | 0 | 1 | 0 |
| [pm-coromandel-mg-lgpdweb](csv/pm-coromandel-mg-lgpdweb.csv) | 11 | 11 | 0 | 0 | 0 |

## Critério de comparação

1. Lidos todos os documentos diretos de `modules/user-data`, com paginação completa e `readTime` fixo por projeto. Campos retornados limitados a `email`, além dos metadados automáticos do documento.
2. Consultado Firebase Authentication pelo e-mail do documento, no mesmo projeto. Para correspondência, removidos espaços nas extremidades e ignoradas maiúsculas/minúsculas do e-mail; os e-mails originais foram preservados.
3. O identificador comparado é `localId` da API do Firebase Authentication, isto é, o UID da conta. Não foi usado campo `uuid`/`uid` do documento.
4. O ID do documento e o UID do Auth foram comparados literalmente, sem remover espaços ou alterar letras.
5. `id_igual_uid`: `SIM` ou `NAO` quando a correspondência por e-mail é única; `NAO_CONFIRMADO` quando faltam evidências para identificar o mesmo usuário. `resultado` explica o motivo.
6. `estado_firebase_auth` e `desativado_firebase_auth` mostram o estado da conta correspondente. `disabled=true` significa desativada; `false` ou ausência do booleano na resposta significa não desativada. “ATIVO” aqui não comprova uso recente, e-mail verificado, permissões ou acesso funcional à aplicação.
7. Também foi feita consulta auxiliar usando o ID do documento como UID. As colunas `uid_localizado_pelo_id_documento`, `email_auth_localizado_pelo_id_documento` e `estado_auth_localizado_pelo_id_documento` mostram essa evidência. Em 16 dos 29 documentos sem e-mail há UID existente com o mesmo ID; a comparação principal permanece não confirmada porque o documento não fornece e-mail para corroborar a identidade.
8. E-mails repetidos no Firestore são indicados por `documentos_com_mesmo_email` e `observacao`. Mais de um documento pode corresponder à mesma conta Auth; cada ID é comparado separadamente.

Para localizar divergências confirmadas, filtre `id_igual_uid=NAO`. Para contas desativadas confirmadas por e-mail, filtre `desativado_firebase_auth=SIM`. Para revisar pendências, filtre `id_igual_uid=NAO_CONFIRMADO` e consulte também as colunas auxiliares.

## Execução, arquivos afetados e verificações

Identidade existente do gcloud: `desenvolvimento@neogov.com.br`. Projeto padrão encontrado: `dashboard-admin-481516`; preservado. Sem novos logins, chaves, mudanças de IAM, ativação de APIs, alteração de configurações do CLI ou escrita remota.

A tentativa inicial de Auth retornou `403 PERMISSION_DENIED` / `SERVICE_DISABLED` para o consumidor compartilhado do Cloud SDK `projects/32555940559`. A leitura funcionou após explicitar `X-Goog-User-Project` com o próprio projeto consultado, atribuindo a quota da chamada ao alvo sem alterar a identidade ou a configuração. Os diagnósticos de autenticação estão preservados em `evidencias.json`, na seção `diagnostico_autenticacao`. O resultado preliminar incompleto de QA foi substituído pela coleta bem-sucedida e removido na limpeza posterior solicitada pelo usuário.

Arquivos mantidos após a limpeza: `contexto.md`, CSVs por projeto em `csv/`, `resumo-projetos.csv`, evidências consolidadas em `evidencias.json`, `manifesto-sha256.json`, `verificacao.json`, `usuarios-depara-lgpdweb.zip` e este relatório. As evidências dos 29 projetos foram consolidadas sem alteração de conteúdo.

A verificação local conferiu os 29 CSVs contra as evidências de cada coleta: cobertura dos projetos, unicidade dos IDs de documento, colunas, quantidades, igualdade literal, correspondência por e-mail, estados das contas, motivos das pendências e hashes SHA-256. Cenários sintéticos de igualdade, divergência, conta desativada, ausência de e-mail/conta, ambiguidade e proteção contra fórmulas de planilha também foram conferidos. O ZIP teve sua integridade e igualdade com os CSVs de origem verificadas.

## Limites, impactos e reversão

A lista parte dos documentos existentes em `user-data`. Contas que existem somente no Firebase Authentication, sem documento nessa coleção, não fazem parte deste levantamento. Subcoleções, outras coleções, bancos e tenants do Identity Platform não foram varridos. E-mail alterado ou ausente pode impedir a correspondência; ausência por e-mail não prova que a conta não exista sob outro e-mail, UID ou tenant. Não foram efetuadas correções nem exclusões.

Firestore foi consultado com snapshot por projeto, mas as leituras de Auth ocorreram depois e não formam transação única entre serviços ou projetos. Os resultados retratam o intervalo registrado, sujeitos a mudanças posteriores.

As leituras do Firestore podem gerar cobrança, e as chamadas consomem quotas dos projetos consultados. Não foi apurado custo monetário. Os arquivos contêm e-mails e identificadores pessoais; a pasta principal e a pasta `csv/` foram criadas com modo 700, e os CSVs/evidências com modo 600. O acesso continua sujeito às permissões locais e a quem receber cópias. Não foram gravados tokens, hashes de senha, chaves, senhas ou documentos completos.

Não há mudanças remotas para reverter. Para desfazer a exportação local, remover esta pasta e eventuais cópias entregues; isso elimina o registro e os arquivos locais, não reverte custos/quota consumidos nem remove cópias já compartilhadas.

## Referências técnicas

- [Firestore — listar documentos, máscara de campos, paginação e readTime](https://docs.cloud.google.com/firestore/docs/reference/rest/v1/projects.databases.documents/list).
- [Firebase Authentication / Identity Platform — lookup por e-mail e UID](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v1/projects.accounts/lookup).
- [UserInfo — localId e disabled](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v1/UserInfo).
- [Autenticação REST e projeto consumidor de quota](https://docs.cloud.google.com/docs/authentication/rest).

## Limpeza dos arquivos auxiliares

Data: 2026-11-09T15:59:32.727305-03:00. Pedido recebido: “agora sem criar nenhuma solicitação noova, limpe o excesso das 3 ultims que geramos aqui”.

Revisadas as três pastas desta conversa. Nesta pasta foram removidos 102 arquivos auxiliares: scripts, cache Python, diagnósticos separados, resultados intermediários, listagem redundante de projetos e versão preliminar de QA. As 29 evidências por projeto e os dois diagnósticos de autenticação foram reunidos em `evidencias.json` antes de remover as cópias individuais. Os CSVs permanecem idênticos aos hashes originais. O ZIP foi atualizado para incluir este relatório revisado.

A pasta de esclarecimento foi mantida integralmente, pois já contém somente contexto e relatório. Na pasta dos documentos completos foram removidas cópias individuais e arquivos de apoio, mantendo Word e JSON finais. Nenhuma nova pasta de solicitação foi criada. A limpeza foi exclusivamente local, sem operações GCP. A remoção dos arquivos auxiliares não tem recuperação garantida; entregáveis e evidências consolidadas foram preservados.
