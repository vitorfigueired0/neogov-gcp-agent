# Criação da estrutura de custos — histórico

Data da execução: **29/10/2026**, fuso `America/Sao_Paulo`.

## Pedido e resultado

O usuário escolheu o projeto principal `lgpdweb` para centralizar as consultas financeiras da Gestão de Dados. Foi criado **`lgpdweb.finops_billing` em US**, sem expiração automática de tabelas ou partições e sem acesso público direto. O único recurso GCP criado foi o dataset; a API, seu IAM, bancos, buckets e segredos não foram alterados.

A ausência inicial foi confirmada por HTTP 404, a criação retornou HTTP 200 e os GETs posteriores confirmaram o dataset em US e zero tabelas. Evidências e instantes estão no [resumo histórico](evidencias/resumo.json). A exportação detalhada estava desativada segundo o usuário nesta etapa; sua ativação foi posteriormente informada na [solicitação seguinte](../2026-10-29-validacao-exportacao-billing/relatorio.md).

A ACL direta ficou restrita à conta criadora. As permissões herdadas do projeto dão acesso BigQuery à conta `cookies-api` e à conta Compute padrão; esse achado permanece relevante para a confidencialidade dos futuros dados financeiros. Nenhum papel foi modificado. A exportação contém a conta Billing inteira, enquanto as consultas filtram os recursos inventariados.

## Entrega e pendências

Foram preparadas as [consultas detalhadas dos últimos 30 dias](ativacao-e-consultas.md), com créditos, moeda e separação entre recursos associados, compartilhados e não atribuídos. **Não houve SELECT de dados, dry-run ou apuração monetária.** A fonte ainda não existia ao encerrar a execução.

O catálogo do ativo foi atualizado somente em `custos.md` e no objeto `cost_reporting` de `inventario.json`; os dados técnicos das 23 instalações foram preservados. O dataset proposto anteriormente em `artefatos` não foi criado.

## Reversão e conservação

Uma futura exclusão do dataset exige conferir primeiro exportação ativa, conteúdo e consumidores. Não excluir dados para reverter apenas documentação. Custos incorridos e histórico financeiro apagado podem não ser recuperáveis. Nenhuma exclusão GCP foi feita.

Por solicitação do usuário, o registro local foi sanitizado: ficaram contexto, este relatório, guia, duas consultas detalhadas e evidências consolidadas. Scripts operacionais, backups, diffs, políticas completas, cópias do inventário, consultas padrão e respostas HTTP redundantes foram removidos. Os arquivos brutos e backups locais não estão mais disponíveis para restauração; os resultados acima são históricos, sem nova verificação GCP durante a limpeza.
