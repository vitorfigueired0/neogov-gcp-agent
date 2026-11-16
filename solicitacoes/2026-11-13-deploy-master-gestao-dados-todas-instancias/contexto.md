# Contexto

Data: 2026-11-13T12:38:57.766111-03:00

## Prompt recebido

> pode fazer a publicação em master da ultima versão em todas as instâncias?

## Objetivo e autorização

Implantar a imagem mais recente publicada pela branch master do Gestão de Dados em todas as instalações existentes identificadas nos projetos conhecidos. Inclui QA, apresentação e clientes com o serviço da aplicação. Pedido sucede diagnóstico da versão 2.1.0: imagem publicada em artefatos, workflow com deploy automático somente para develop.

Escopo: revalidar imagem master e versão; descobrir serviços existentes nos 29 projetos do mapeamento de 09/11/2026; guardar configuração sanitizada e tráfego anterior; atualizar imagem por digest, verificar revisões e respostas HTTP sem sessão; reverter tráfego em caso de falha relacionada à atualização. Não criar novas instalações em projetos sem o serviço; não alterar IAM, dados, segredos, DNS, configurações de autenticação, GitHub/pipeline ou defaults do CLI. Preservar alterações locais preexistentes.

Riscos apresentados antes da execução: novas revisões podem falhar, causar regressões/cold starts e cobrança temporária. Rollback de tráfego não reverte gravações de aplicação; segredos referenciados por latest e dependências externas podem limitar a recuperação. Nenhum teste de escrita ou login com dados reais previsto.

Conta gcloud existente confirmada: desenvolvimento@neogov.com.br; default dashboard-admin-481516, sem região/zona/impersonação configuradas. Defaults não serão alterados. Ambiente exato dos clientes é historicamente incompleto; autorização atual abrange todas as instâncias da aplicação, com identificação concreta antes das mutações.

## Correção posterior de escopo pelo usuário

> em qa nãoo precisa, apenas faça em todos os ambientes de prod
> pode roodar uma leitura ai eem todos os projetos gcp que possuem a cloud run gestao-de-dados-api

Esta correção substitui a inclusão inicial de QA: não fazer deploy em QA. Consultar todos os projetos acessíveis para descobrir os serviços de nome exato gestao-de-dados-api em todas as regiões, identificar produção e limitar a alteração a essas instalações. A leitura não autoriza modificar outros serviços. Nenhum deploy tinha sido executado antes desta correção.
