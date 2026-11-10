# Esclarecimento dos 47 documentos não confirmados

Os 47 existem na coleção `modules/user-data`. “Não confirmado” significa que não foi possível corroborar a identidade por e-mail; não significa automaticamente que não há conta Auth.

| Situação observada na coleta anterior | Documentos |
| --- | ---: |
| Documento sem e-mail, mas ID encontrado como UID no Firebase Auth do mesmo projeto | 16 |
| Documento sem e-mail e ID não encontrado como UID no Firebase Auth do mesmo projeto | 13 |
| Documento com e-mail, mas nem e-mail nem ID encontrados no Firebase Auth do mesmo projeto | 18 |
| Total | 47 |

Portanto, 16 têm UID existente no Auth e 31 não foram localizados pelos identificadores disponíveis nessa coleta. Os 13 sem e-mail só puderam ser procurados pelo ID do documento; não é possível excluir conta com outro UID/e-mail. Os 18 com e-mail não foram localizados por nenhum dos dois identificadores. Não houve nova consulta ao estado atual do GCP.

Verificação: releitura dos 29 CSVs, cruzando `id_igual_uid=NAO_CONFIRMADO`, `resultado` e `uid_localizado_pelo_id_documento`; contagens 16 + 13 + 18 = 47 conferidas com asserção local.

Arquivos afetados: somente `contexto.md` e este `relatorio.md` nesta nova pasta. Reversão: remover esses dois arquivos e a pasta; nenhum recurso remoto foi alterado e não houve custo adicional de leitura no GCP.

Fonte: [relatório e links para CSVs da coleta original](../2026-11-09-depara-usuarios-ativos-lgpdweb/relatorio.md).
