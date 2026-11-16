# Diagnóstico da publicação Gestão de Dados 2.1.0

> Conservação documental — 13/11/2026: por pedido do usuário, foram mantidos o contexto, o relatório final e as entregas finais. Arquivos auxiliares, evidências separadas, scripts, verificações, diffs e backups locais foram removidos; referências a eles no histórico descrevem a execução original, não arquivos ainda disponíveis. Os resultados não foram reconsultados no GCP durante esta limpeza. Recuperação que dependa dos backups removidos exige outra cópia ou versão disponível no Git.

Data: 13/11/2026, fuso America/Sao_Paulo.

## Resultado e causa

O workflow inspecionado publica imagens de master e develop, mas contém apenas um job de deploy, deploy-dev, cuja condição exige refs/heads/develop. Assim, uma execução na master pode publicar 2.1.0/master/latest e terminar sem executar deploy-dev. Não existe job de deploy para master nesse arquivo.

Fonte: /home/vitor/projetos/NEOGOV/gestao-de-dados-api/.github/workflows/ci.yml, job publish linhas 48–56, regras de tags linhas 100–103 e job deploy-dev linhas 152–201. Cópia documental em workflow-ci.yml (auxiliar removido; resultado consolidado neste relatório). A árvore local consultada estava limpa, branch master, commit 3ffda7a6923c36b353acf586221fa5b68bc6facd (13/11/2026 12:09:11 -03), package.json 2.1.0. O histórico contém merge da release/2.1.0 às 12:00:15 -03.

A condição do job explica o comportamento relatado e é consistente com as evidências GCP. A execução e os logs correspondentes do GitHub Actions não foram consultados; portanto não foi afirmado ter observado diretamente o estado skipped do job no GitHub, nem comprovada a igualdade entre o checkout e o arquivo remoto daquela execução.

## Verificações atuais no GCP

- Imagem 2.1.0 existe no projeto artefatos, repositório us-central1/gestao-de-dados-api, publicada em 13/11/2026 às 12:12:48 -03. Tags 2.1.0, master e latest apontam ao índice OCI sha256:519b603914c4ce73922e4328078293e781a67b82b1a9febfde343248be883185.
- QA pm-neogov-qa-lgpdweb/us-central1: revisão gestao-de-dados-api-00025-d7k, Ready=True, tráfego 100%, pronta em 13/11/2026 às 11:50:01 -03. Imagem configurada sha256:c508b861cac6e5ecec08ad1955ec931d53a2985cb75d73d10721cdf5e8badd22, correspondente à tag develop na consulta atual. É diferente da imagem 2.1.0.
- Apresentação lgpdweb/us-central1: revisão gestao-de-dados-api-rel-1-0-0, Ready=True e tráfego 100%. Imagem sha256:72ab7958af9cf666d167d39f5ae68c5562fa3613c034a6e9688a545e16f8a439, correspondente à tag 1.0.0 na consulta atual.
- No projeto artefatos não foram encontrados gatilhos Cloud Build do Gestão de Dados em us-central1/global; builds desde 12/11/2026T00:00Z retornaram vazios nessas localizações, limite 20 por consulta. Isso não exclui mecanismos em outros projetos/regiões ou fora de Cloud Build.
- Publicar uma tag não atualiza sozinho uma revisão Cloud Run: a imagem é resolvida por digest no deploy. [Documentação oficial](https://docs.cloud.google.com/run/docs/deploying).

O README do catálogo, copiado no levantamento de 29/10, dizia que a publicação não fazia deploy. Ele é referência histórica: o workflow local atual já inclui deploy de develop, mas continua sem deploy da master. O catálogo não foi alterado nesta solicitação.

## Escopo, impactos e alterações

Somente consultas de leitura ao GCP, leitura do repositório local da aplicação e criação de documentação nesta pasta. Contexto de autenticação consultado e preservado; falha inicial por filesystem somente leitura foi resolvida com execução escalada usando a mesma autenticação. Não houve login, troca de identidade/configuração, leitura de payload de segredo, alteração de IAM, deploy, modificação de pipeline ou dados da aplicação.

Arquivos criados: contexto.md, evidencias.md, workflow-ci.yml e relatorio.md. Registros locais podem conter identificadores operacionais, mas não credenciais nem valores de segredos. Não foram criados temporários descartáveis por esta execução; não há temporários próprios a limpar.

## Pendências e encaminhamento

Para implantar 2.1.0, será necessário definir o projeto/ambiente de destino e autorizar o deploy dessa imagem por digest. Para automatizar releases de master, será necessário definir destinos e política de promoção/aprovação e implementar o job apropriado; esta solicitação de diagnóstico não autoriza essa alteração. Não basta remover a condição de develop, pois o job usa environment develop e as variáveis desse ambiente.

Não foi revalidada toda a frota de clientes, nem consultado diretamente o workflow remoto/run do GitHub. Não houve teste funcional da aplicação.

## Reversão

Nenhuma mudança GCP ou código da aplicação a reverter. Os quatro arquivos desta pasta podem ser removidos para desfazer o registro documental, com perda da trilha do diagnóstico. Os registros anteriores e o catálogo foram preservados.

Evidências (auxiliar removido; resultado consolidado neste relatório).

