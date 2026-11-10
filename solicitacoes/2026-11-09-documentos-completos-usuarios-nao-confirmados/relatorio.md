# Relatório da exportação completa dos 47 documentos

Data de geração: 2026-11-09T15:53:16.631269-03:00.

Obtidos os **47 documentos** selecionados em **8 projetos**, no banco `modules`, coleção `user-data`. Todos têm o mesmo `updateTime` da coleta original e foram consultados usando os `readTime` originais, por volta de 15h22 de 09/11/2026 (America/Sao_Paulo).

## Entrega

- [Documento Word com todos os campos e metadados](dados-dos-47-documentos.docx).
- [JSON na representação nativa do Firestore](documentos-completos.json).
- [Verificação](verificacao.json) e [integridade SHA-256](manifesto-sha256.json).

| Projeto | Documentos |
| --- | ---: |
| `cachoeiradouradamglgpdweb` | 3 |
| `camarafrutallgpdweb` | 1 |
| `camaraituiutabalgpdweb-a1a06` | 1 |
| `frutallgpdweb-3dab8` | 2 |
| `lgpdwebsaaeituiutaba` | 2 |
| `neogov-default` | 10 |
| `pm-machado-lgpdweb` | 1 |
| `pm-neogov-qa-lgpdweb` | 27 |

## Conteúdo e limites

Incluídos todos os campos dos documentos, com mapas/listas completos, ID/caminho e metadados createTime/updateTime, além da classificação anterior do de/para. Campos de topo exportados: **373**. Ocorrências omitidas por possíveis segredos no resultado final: **0**. Foram verificados nomes de campos sensíveis, valores com padrões de credenciais e parâmetros de URL. A varredura é heurística; valores sem padrões reconhecíveis podem exigir revisão específica. Não houve truncamento.

O Word exibe os valores em JSON legível; tipos especiais têm marcadores $timestamp, $reference, $bytes_base64 e $geoPoint. O JSON anexo preserva a representação tipada do Firestore. Subcoleções não são parte dos campos do documento e não foram exportadas. Nenhuma nova leitura de Firebase Authentication foi feita; a classificação por Auth continua a da coleta anterior.

## Execução e verificação

Utilizada a autenticação existente do gcloud, sem login, alteração de identidade/configuração ou credenciais novas. Leituras GET diretas apenas dos 47 alvos; nenhum recurso GCP foi alterado. A primeira passada de sanitização omitiu indevidamente booleanos chamados cookies e datas passwordChangedAt. Uma leitura limitada conferiu os tipos; a regra foi ajustada e os 47 documentos foram relidos no mesmo snapshot, preservando esses valores. Foram 95 leituras GET de documentos (47 iniciais + 1 diagnóstico + 47 finais), além da obtenção de token em memória, sem persistência do token.

Verificados: cobertura exata dos 47 alvos, unicidade projeto/ID, updateTime igual ao histórico, preservação dos nomes dos campos de topo, JSON válido, integridade do pacote DOCX e de seus XMLs, reconstrução dos 47 JSONs a partir do texto do Word e igualdade com os dados de origem convertidos. Campos secretos simples e aninhados e preservação de booleanos/datas foram conferidos com dados sintéticos. A formatação visual no Microsoft Word/LibreOffice não foi inspecionada; a verificação realizada é estrutural e de conteúdo.

## Arquivos, impactos e reversão

Arquivos mantidos após a limpeza: `contexto.md`, `dados-dos-47-documentos.docx`, `documentos-completos.json`, `verificacao.json`, `manifesto-sha256.json` e este relatório. O JSON consolidado preserva integralmente o conteúdo das 47 evidências individuais removidas. Word e JSON mantêm os hashes originais.

As leituras podem gerar cobrança de Firestore; o valor monetário não foi apurado. Os arquivos contêm dados pessoais. Pasta principal com modo 700; arquivos de dados e entregáveis com modo 600. Acesso e cópias continuam sujeitos às permissões locais e ao compartilhamento feito pelo usuário.

Reversão: remover esta pasta e eventuais cópias entregues. Não há alterações remotas para desfazer; custos/quota consumidos e cópias compartilhadas não são revertidos pela remoção local.

Referências: [levantamento anterior](../2026-11-09-depara-usuarios-ativos-lgpdweb/relatorio.md), [esclarecimento dos 47](../2026-11-09-esclarecimento-usuarios-nao-confirmados/relatorio.md) e [Firestore GET/readTime](https://docs.cloud.google.com/firestore/docs/reference/rest/v1/projects.databases.documents/get).

## Limpeza dos arquivos auxiliares

Data: 2026-11-09T15:59:32.727305-03:00. Limpeza solicitada pelo usuário nas três pastas desta conversa, sem criar nova solicitação.

Removidos 54 arquivos: 47 evidências individuais já contidas em `documentos-completos.json`, scripts, cache Python, lista de alvos, resultado de coleta duplicado e diagnóstico de sanitização. Antes da exclusão, todas as evidências individuais foram comparadas com o JSON consolidado. Word e JSON finais foram conferidos pelos hashes originais, preservando seu conteúdo. A limpeza não acessou o GCP. Os arquivos de apoio apagados não têm recuperação garantida; os dados completos e os entregáveis foram preservados.
