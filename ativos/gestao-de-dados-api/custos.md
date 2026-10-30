# Custos da API e dependências

Atualização: 2026-10-29T22:55:26.463931-03:00. Período de análise: **últimos 30 dias**.

## Estrutura criada no projeto principal

Dataset **`lgpdweb.finops_billing`**, multirregião **`US`**, criado e verificado. Projeto escolhido explicitamente pelo usuário para centralizar as consultas. A proposta histórica em `artefatos` foi substituída; nenhum dataset foi criado lá.

O usuário informou que **ativou a exportação detalhada**. Na consulta de metadados posterior, o dataset permanece **sem tabelas**; a primeira carga ainda não foi observada. A ativação foi realizada pelo usuário no console, sem mudança de configuração pelo agente. Ainda **não há valores monetários apurados**; ausência de dados não significa gasto zero.

## Acesso e impacto

A ACL direta tem OWNER `desenvolvimento.neogov@gmail.com`, endereço canônico retornado para a conta configurada no CLI como `desenvolvimento@neogov.com.br`. A identidade foi conferida usando a mesma sessão, sem troca de credenciais. Não há acesso público nem expiração automática de tabelas/partições configurados.

O IAM do projeto concede permissões BigQuery a `cookies-api@lgpdweb.iam.gserviceaccount.com` e à conta Compute padrão. Essas permissões se aplicam ao novo dataset. A exportação detalhada inclui a conta Billing inteira, abrangendo outros projetos; **os futuros dados financeiros também poderão ser acessados por essas contas**. Nenhum papel existente foi alterado.

Armazenamento da exportação e execução de consultas podem gerar cobrança BigQuery. As contas runtime da Gestão de Dados não receberam novas concessões. Nenhum recurso de execução, banco, bucket ou segredo da API foi alterado nesta etapa.

## Consultas e próximos passos

As consultas preparadas relacionam Cloud Run, Firestore, buckets e segredos dos 23 projetos inventariados, incluindo créditos e moeda. Repositório central, logging compartilhado e custos sem atribuição permanecem separados. Não foi aplicado rateio nem atribuído todo o projeto à API.

[Guia de ativação no console e uso das consultas](../../solicitacoes/2026-10-29-custos-gestao-dados-lgpdweb/ativacao-e-consultas.md).

[Consulta detalhada para o console — últimos 30 dias](../../solicitacoes/2026-10-29-custos-gestao-dados-lgpdweb/consultas/custos_detalhados_30_dias_console.sql).

[Consulta parametrizada para validação/dry-run](../../solicitacoes/2026-10-29-custos-gestao-dados-lgpdweb/consultas/custos_detalhados_30_dias.sql).

[Relatório desta criação](../../solicitacoes/2026-10-29-custos-gestao-dados-lgpdweb/relatorio.md).

As fontes SQL apontam para a tabela esperada do export detalhado; confirmar nome e esquema quando surgir. SQL e dry-run ainda não foram executados por falta da fonte. As demais informações técnicas do inventário preservam a data de sua coleta anterior.

[Verificação após ativação informada pelo usuário](../../solicitacoes/2026-10-29-validacao-exportacao-billing/relatorio.md). A tabela detalhada ainda não apareceu; não criar uma tabela substituta manualmente. Dry-run não realizado por ausência da fonte.
