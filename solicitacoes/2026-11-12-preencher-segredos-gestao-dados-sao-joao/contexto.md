# Contexto

Data: 2026-11-12T10:03:24.019066-03:00 (America/Sao_Paulo).

## Prompt recebido, com segredo omitido

> prencha a api key com [SEGREDO OMITIDO] e o alloowed issuers é a url da api de auth de prod

## Objetivo e escopo

Adicionar novas versões a NEOGOV_AUTH_API_KEY e NEOGOV_AUTH_ALLOWED_ISSUERS em pm-sao-joao-del-rei-mg, usando a chave fornecida somente em memória e a URL https://api.auth.neogov.com.br como emissor exato. A URL consta no catálogo de autenticação de produção e no env preparado; o valor de iss foi determinado explicitamente pelo usuário, sem validação de JWT nesta etapa. Usar identidade/configuração gcloud existente e projeto explícito. Verificar ENABLED por metadados sem ler payloads. Não iniciar deploy, mudar IAM ou rotacionar chaves por iniciativa própria nesta etapa. Chave omitida de contexto, comandos e evidências. Reversão: desabilitar apenas as versões novas depois de conferir consumidores; isso não remove o payload armazenado. Custos: armazenamento/acesso de versões Secret Manager conforme uso.
