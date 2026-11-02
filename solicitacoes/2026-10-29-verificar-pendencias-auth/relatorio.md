# Relatório — verificação de pendências da Auth API

## Resultado

Foram verificadas as pendências autorizadas, sem alterar recursos GCP, ativar APIs, ler dados de negócio ou revelar valores de segredos.

- Domínios e TLS confirmados: produção `api.auth.neogov.com.br` → `neogov-auth-prd`; desenvolvimento `api.auth-develop.neogov.com.br` → `neogov-auth-dev`. Ambos têm domínio roteável e certificado provisionado.
- Firestore: produção possui quatro backups `READY` do `auth-db-prd`; desenvolvimento não retornou backup. Há três índices compostos `READY` em produção e nenhum em desenvolvimento.
- Políticas diretas: os cinco segredos de cada projeto não possuem `bindings` locais retornados.
- Firebase Auth não pôde ser detalhado porque a chamada requer *quota project* nas ADC locais. A configuração não foi alterada.
- Cloud Functions e Cloud SQL continuam não verificáveis porque suas APIs estão desabilitadas; elas não foram ativadas.

## Arquivos afetados

- [Contexto](contexto.md)
- [Evidências](evidencias/coleta-resumo.md)
- [Cópias anteriores](backups/)
- [Resumo das diferenças](diff-resumo.md)
- [Catálogo atualizado — componentes](../../ativos/neogov-auth-api/componentes.md)
- [Catálogo atualizado — inventário](../../ativos/neogov-auth-api/inventario.md)
- [Catálogo atualizado — permissões](../../ativos/neogov-auth-api/permissoes.md)

## Reversão

As mudanças são exclusivamente documentais. Para reverter o catálogo, restaure os arquivos de `backups/` sobre os equivalentes em `ativos/neogov-auth-api/`. Não há reversão remota porque não houve mudança em GCP.
