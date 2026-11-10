# Contexto

Data: 2026-11-09T15:40:50.640773-03:00

## Prompt recebido

> me gere um documento com todos os dados desses documentos por favor,

## Escopo

Exportar os campos completos e metadados dos 47 documentos de modules/user-data classificados como NAO_CONFIRMADO no de/para anterior, distribuídos em 8 projetos. Referência: [coleta anterior](../2026-11-09-depara-usuarios-ativos-lgpdweb/relatorio.md). Usar os readTime originais (menos de uma hora no início) para manter o mesmo snapshot. Somente leitura remota; documento Word e JSON locais. Não incluir subcoleções ou dados adicionais de Firebase Auth. Sanitizar segredos antes de salvar. Preservar autenticação e configuração do gcloud existentes.

## Impactos, verificação e reversão

As 47 leituras podem gerar cobrança; o documento consolidará dados pessoais sob permissões locais. Verificar cobertura exata dos alvos, campos, contagens, XML e integridade do DOCX, sanitização e integridade dos arquivos. Reversão: remover a pasta e as cópias locais; não reverte custos de leitura ou cópias compartilhadas. Sem alterações em recursos GCP.

Catálogo ativos/ consultado; não contém esquema dessa coleção.
