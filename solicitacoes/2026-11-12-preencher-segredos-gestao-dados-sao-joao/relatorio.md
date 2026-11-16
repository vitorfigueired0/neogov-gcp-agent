# Preenchimento de segredos — Gestão de Dados / São João del-Rei

> Conservação documental — 13/11/2026: por pedido do usuário, foram mantidos o contexto, o relatório final e as entregas finais. Arquivos auxiliares, evidências separadas, scripts, verificações, diffs e backups locais foram removidos; referências a eles no histórico descrevem a execução original, não arquivos ainda disponíveis. Os resultados não foram reconsultados no GCP durante esta limpeza. Recuperação que dependa dos backups removidos exige outra cópia ou versão disponível no Git.

Data: 2026-11-12T10:05:48.603568-03:00 (America/Sao_Paulo). Projeto `pm-sao-joao-del-rei-mg`.

## Resultado

Criadas as versões `NEOGOV_AUTH_API_KEY:1` e `NEOGOV_AUTH_ALLOWED_ISSUERS:1`; ambas ENABLED, verificadas com consultas independentes de metadados. A chave foi fornecida pelo usuário e transmitida por entrada oculta ao script e por stdin ao gcloud; não foi incluída em argumentos, scripts, arquivos de payload ou registros. O emissor foi definido por indicação explícita do usuário como `https://api.auth.neogov.com.br`, sem barra final; a URL de produção consta no catálogo local.

A verificação não leu os valores de volta nem validou um token. Não se afirma que o vínculo tenant/sistema já existe ou que a chave foi aceita pela central. Foi usada a autenticação existente `desenvolvimento@neogov.com.br`, preservando default `dashboard-admin-481516`; nenhuma identidade/configuração foi trocada. Logging HTTP foi desativado apenas no processo de escrita para evitar payloads em logs.

## Arquivos e recursos afetados

- Secret Manager: somente adição de uma versão aos dois recursos existentes. Estado anterior sem versões nas evidências `pre-key.json` e `pre-issuers.json`; criação em `adicionar-key.json` e `adicionar-issuers.json`; verificação em `verificar-key.json` e `verificar-issuers.json`.
- [Contexto sanitizado](contexto.md) e script `preencher.py`, sem valores embutidos.
- Template local do Cloud Run (auxiliar removido; resultado consolidado neste relatório) com as duas referências fixadas na versão 1; imagem continua como marcador pendente. O template anterior permanece preservado na solicitação de preparação.
- Catálogo [Gestão de Dados](../../ativos/gestao-de-dados-api/inventario.md): complementados componentes, inventário Markdown/JSON, permissões e custos somente quanto às versões. Backups dos cinco arquivos em `backup-catalogo/`; diff (auxiliar removido; resultado consolidado neste relatório).

Nenhuma alteração IAM, deploy, mudança de domínio/DNS ou chamada funcional à central foi feita. A aplicação continua pendente de seleção da imagem, deploy e configuração da entrada.

## Impacto, verificação e reversão

Versões ativas e futuros acessos Secret Manager são sujeitos à cobrança. Nenhuma estimativa monetária realizada. A adição não substitui nem destrói versões anteriores; neste caso as consultas iniciais retornaram vazias.

Reversão proposta, não executada: consultar consumidores e desabilitar somente a versão 1 de cada segredo no projeto alvo. Isso pode impedir inicialização/acesso de aplicações que venham a referenciá-las; desabilitar não apaga o payload nem equivale a sua destruição. Não destruir segredos ou versões automaticamente. Para desfazer somente os documentos, comparar e restaurar os cinco backups preservando alterações posteriores.

Verificações locais em `verificacoes.txt`: JSON, referências numéricas, preservação do histórico, links, integridade do diff e padrões de segredos. Não houve diretório ou arquivo temporário de payload; somente registros documentais foram gerados. Não foram expostos valores secretos nas saídas.
