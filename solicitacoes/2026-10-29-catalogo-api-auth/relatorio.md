# Relatório — catálogo da API de Auth

> Conservação documental — 13/11/2026: por pedido do usuário, foram mantidos o contexto, o relatório final e as entregas finais. Arquivos auxiliares, evidências separadas, scripts, verificações, diffs e backups locais foram removidos; referências a eles no histórico descrevem a execução original, não arquivos ainda disponíveis. Os resultados não foram reconsultados no GCP durante esta limpeza. Recuperação que dependa dos backups removidos exige outra cópia ou versão disponível no Git.

## Resultado

Catálogo criado para `neogov-auth` em `ativos/neogov-auth-api/`, com instalações de produção e desenvolvimento documentadas. Foram feitas somente leituras de metadados, políticas e estados. Nenhum recurso GCP, configuração, API, segredo ou credencial foi alterado.

Os dois projetos estão `ACTIVE`; cada um contém um serviço Cloud Run em `us-central1`, `Ready`, com 100% do tráfego na revisão mais recente. Foram identificados Firestore Native, referências de Secret Manager, Firebase/Identity Toolkit habilitados e uma dependência de imagem no projeto externo `artefatos`.

## Arquivos afetados

- [Contexto](contexto.md)
- Evidências (auxiliar removido; resultado consolidado neste relatório)
- [Componentes](../../ativos/neogov-auth-api/componentes.md)
- [Inventário Markdown](../../ativos/neogov-auth-api/inventario.md)
- [Inventário JSON](../../ativos/neogov-auth-api/inventario.json)
- [Permissões](../../ativos/neogov-auth-api/permissoes.md)
- [Custos](../../ativos/neogov-auth-api/custos.md)

Não existia catálogo prévio deste ativo, portanto não houve arquivo a preservar ou backup a criar. Nenhum README da aplicação foi fornecido; não foi criado um README fictício.

## Verificações realizadas

- JSON validado e coerência conferida entre as instalações do inventário e as tabelas Markdown.
- Nenhum valor de segredo foi lido ou persistido; somente nomes e versões de referências foram registrados.
- Os resultados diretos e limitações estão em `evidencias/coleta-resumo.md`.

## Pendências e limites

- Rota pública, domínio/TLS, WAF/CDN e a configuração de Firebase Auth não foram confirmados.
- Backups/índices Firestore e políticas diretas dos segredos permanecem não verificados, pois a coleta detalhada foi bloqueada pelo controle de escopo da sessão.
- Cloud Functions e Cloud SQL não foram inventariados porque suas APIs estão desabilitadas; elas não foram ativadas.
- Custos não foram apurados, pois não foram solicitados.

## Reversão

As mudanças são exclusivamente locais e documentais. Para desfazê-las, remova `ativos/neogov-auth-api/` e esta pasta de solicitação. Não há reversão de recursos GCP porque não houve alteração remota.
