# Contexto da solicitação

- Data da abertura: 2026-10-29T23:19:52-03:00 (America/Sao_Paulo)
- Tipo: catalogação documental de ativo GCP; somente consultas de metadados e políticas.

## Prompt recebido

> [$gcp-catalogar-ativos](/home/vitor/projetos/playground/gcp-agent/.codex/skills/gcp-catalogar-ativos/SKILL.md) quero que faça o catalogo da api de auth, ela rooda eem prod no projeto neogov-auth-prd e em dev no projeto neogov-auth-dev

## Resumo técnico

- Objetivo: catalogar a API de autenticação (identificador provisório: `neogov-auth`) em um consolidado local sob `ativos/`.
- Escopo autorizado: consultas de configuração, metadados e políticas nos projetos `neogov-auth-prd` (produção, conforme informado) e `neogov-auth-dev` (desenvolvimento, conforme informado).
- Fora de escopo: alteração de recursos GCP, leitura de dados de negócio, conteúdo de segredos, credenciais e projetos/dependências externos.
- Recursos específicos, regiões, nomes de serviços, domínios, custos e documentação-fonte: ainda não confirmados no início da coleta.
- Referência local prévia: o catálogo `ativos/gestao-de-dados-api/` cita `neogov-auth` como dependência externa e URLs de autenticação, mas não constitui prova do estado atual nem amplia o escopo.
