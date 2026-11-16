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

## São João del-Rei — preparação em 12/11/2026

A consulta de metadados não encontrou a instalação de Gestão de Dados no projeto `pm-sao-joao-del-rei-mg` pelos identificadores documentados. Não foram feitas consultas financeiras nem atribuídos os custos dos serviços existentes à aplicação. Ausência da instalação não significa custo zero no projeto.

A futura instalação poderá cobrar por Cloud Run, banco nomeado Firestore, índices, Storage/operações/soft delete, Secret Manager, logs e transferência; retenção de backups/PITR e balanceador, se escolhidos, têm custos adicionais. Não há estimativa monetária confirmada. Recursos centrais e existentes não devem ser rateados sem critério. [Evidências e plano](../../solicitacoes/2026-11-12-plano-implantacao-gestao-dados-sao-joao/relatorio.md).

## Recursos preparados — São João del-Rei, 12/11/2026

Faturamento habilitado verificado por metadados. Banco nomeado `gestao-de-dados` informa `freeTier=false`; não tratar como banco gratuito. Recursos associados: novo banco e quatro índices, bucket de mídias STANDARD/US-CENTRAL1 com soft delete de 7 dias e dois recursos de segredo ainda sem versões. Não há Cloud Run da instalação executando, balanceador criado, backup agendado ou PITR ativado nesta fase.

Armazenamento, operações, índices, retenção e versões/acessos de segredos podem gerar cobrança conforme uso; não foi calculado valor nem feita consulta financeira. CLI e catálogos não comprovam ausência absoluta de tráfego/custos. Revogar permissões não remove cobrança por dados retidos. Recursos já existentes e dependências centrais não foram atribuídos à aplicação. [Relatório de execução e evidências](../../solicitacoes/2026-11-12-plano-implantacao-gestao-dados-sao-joao/execucao-aprovada/relatorio.md).

Em 2026-11-12T10:05:48.603568-03:00, os dois segredos de São João del-Rei passaram a ter uma versão ENABLED cada. Armazenamento de versões e futuros acessos podem cobrar conforme uso; nenhuma análise financeira executada. Desabilitar versões não equivale a destruir seu conteúdo nem apagar toda cobrança. [Relatório do preenchimento](../../solicitacoes/2026-11-12-preencher-segredos-gestao-dados-sao-joao/relatorio.md).

Em 2026-11-12T10:20:22.124691-03:00, São João del-Rei passou a ter API Cloud Run publicada em us-central1: 1 vCPU/1 GiB, min 0/max 3, concorrência 80 e timeout HTTP 300 s. Execução, requisições, logs e tráfego são componentes faturáveis conforme uso; min zero admite cold starts, max três não é teto financeiro. O timeout da central de 20 s pode ampliar o tempo de requisições lentas. Não houve análise monetária, migração de dados ou criação de balanceador/IP nesta etapa. Imagem permanece no repositório compartilhado artefatos, sem rateio de custos. [Relatório do deploy](../../solicitacoes/2026-11-12-deploy-gestao-dados-sao-joao/relatorio.md).
