# Implantação Gestão de Dados — produção

> Conservação documental — 13/11/2026: por pedido do usuário, foram mantidos o contexto, o relatório final e as entregas finais. Arquivos auxiliares, evidências separadas, scripts, verificações, diffs e backups locais foram removidos; referências a eles no histórico descrevem a execução original, não arquivos ainda disponíveis. Os resultados não foram reconsultados no GCP durante esta limpeza. Recuperação que dependa dos backups removidos exige outra cópia ou versão disponível no Git.

Atualizado em 2026-11-13T13:00:58.042875-03:00

## Resultado

Status: implantação e verificação final concluídas.

25/25 instalações com deploy e smoke tests verificados. 0 falhas registradas. QA excluído explicitamente pelo usuário.

Imagem fixada: us-central1-docker.pkg.dev/artefatos/gestao-de-dados-api/gestao-de-dados-api@sha256:519b603914c4ce73922e4328078293e781a67b82b1a9febfde343248be883185

Versão: 2.1.0. Digest linux/amd64: sha256:da79b04ddca7292fe334dd5bf928a32f05220e8d50eb7173945aaf6817940649

Commit informado nos metadados OCI: 3ffda7a6923c36b353acf586221fa5b68bc6facd. Corresponde ao checkout master inspecionado; metadados não equivalem a assinatura independente.

## Descoberta e escopo

Consultados 65 projetos acessíveis pela conta existente desenvolvimento@neogov.com.br, em todas as regiões. Encontrados 26 serviços de nome exato gestao-de-dados-api, todos us-central1. Selecionados 25 com autenticação de produção e frontend de cliente/apresentação. QA pm-neogov-qa-lgpdweb excluído. lgpdweb é apresentação de produção conhecida, com label histórica production-test, usada como primeira validação.

Nem todos os clientes têm label explícita de ambiente; classificação baseada no contexto do pedido, frontend e NEOGOV_AUTH_BASE_URL de produção. Universo limitado aos projetos visíveis à conta. Em 32 projetos a consulta foi bem-sucedida sem o serviço; em sete a API Cloud Run está desabilitada e não foi habilitada. Consulta com erro não prova ausência global.

## Execução e verificações

Baseline HTTP aprovado nos 25 alvos. Em cada deploy concluído: snapshot sanitizado, geração conferida para detectar alteração concorrente, atualização somente da imagem por digest sem tráfego, revisão Ready, digest de plataforma e configuração runtime sem imagem conferidos. Teste pela tag temporária; promoção de 100% do tráfego mantendo latest e remoção da tag.

Smoke tests: /docs-json=200; /auth/self, /complaints e /complaints/aggregates sem credenciais=401; OPTIONS /auth/self=204 com origem CORS e credentials corretos. Na nova versão também verificada a presença de personal_data_consent obrigatório no schema de cadastro. Testes repetidos pela URL padrão run.app após promoção. Sem cadastro, login válido, CRUD, upload ou leitura de dados de negócio. DNS/TLS de domínios personalizados não foram revalidados.

Verificação final independente: 2026-11-13T13:00:32.793100-03:00. Estados aprovados: 26/26, incluindo QA.

Tag master ainda corresponde à release fixada na conferência final: True.

QA com mesma geração, imagem, configuração e tráfego do snapshot: True. Revisão: gestao-de-dados-api-00025-d7k.

Logs severity>=ERROR das novas revisões desde o início de cada deploy, limite 20/projeto: 0 entradas. Falhas de leitura: nenhuma. Ausência de entradas é limitada ao intervalo e instante consultados.

## Estado por instalação

| Projeto | Revisão anterior | Nova revisão | Estado |
| --- | --- | --- | --- |
| cachoeiradouradamglgpdweb | gestao-de-dados-api-00001-x7z | gestao-de-dados-api-00002-bud | verified |
| camaraconceicaoalagoaslgpdweb | gestao-de-dados-api-00001-x66 | gestao-de-dados-api-00002-vup | verified |
| camarafrutallgpdweb | gestao-de-dados-api-00001-c2v | gestao-de-dados-api-00002-qac | verified |
| camaraituiutabalgpdweb-a1a06 | gestao-de-dados-api-00001-q7w | gestao-de-dados-api-00002-qin | verified |
| camarateresopolislgpdweb | gestao-de-dados-api-00001-jrn | gestao-de-dados-api-00002-nif | verified |
| cides-lgpdweb | gestao-de-dados-api-00001-wqr | gestao-de-dados-api-00002-mag | verified |
| cisalp-lgpdweb | gestao-de-dados-api-00001-gvr | gestao-de-dados-api-00002-vep | verified |
| cm-araguari-lgpdweb | gestao-de-dados-api-00001-947 | gestao-de-dados-api-00002-faq | verified |
| cm-campo-florido-lgpdweb | gestao-de-dados-api-00001-xws | gestao-de-dados-api-00002-gim | verified |
| frutallgpdweb-3dab8 | gestao-de-dados-api-00001-tpq | gestao-de-dados-api-00002-yeh | verified |
| lgpdweb | gestao-de-dados-api-rel-1-0-0 | gestao-de-dados-api-00005-teq | verified |
| lgpdwebsaaeituiutaba | gestao-de-dados-api-00001-7w9 | gestao-de-dados-api-00002-xoy | verified |
| pm-coromandel-mg-lgpdweb | gestao-de-dados-api-00001-b2c | gestao-de-dados-api-00002-cad | verified |
| pm-estreladosul-mg-lgpdweb | gestao-de-dados-api-00001-k45 | gestao-de-dados-api-00002-gez | verified |
| pm-itaguai-rj-lgpdweb | gestao-de-dados-api-00001-ck8 | gestao-de-dados-api-00002-zoh | verified |
| pm-machado-lgpdweb | gestao-de-dados-api-00001-sst | gestao-de-dados-api-00002-daz | verified |
| pm-montecarmelo-mg-lgpdweb | gestao-de-dados-api-00001-nxh | gestao-de-dados-api-00002-baz | verified |
| pm-pedrinopolis-lgpdweb | gestao-de-dados-api-00001-vk7 | gestao-de-dados-api-00002-kuw | verified |
| pm-sao-joao-del-rei-mg | gestao-de-dados-api-00002-l6h | gestao-de-dados-api-00004-zoc | verified |
| pm-tupaciguara-mg-lgpdweb | gestao-de-dados-api-00001-vzz | gestao-de-dados-api-00002-yuz | verified |
| pmdeltamglgpdweb | gestao-de-dados-api-00001-t4d | gestao-de-dados-api-00002-pep | verified |
| pmsgalgpdweb-32cf8 | gestao-de-dados-api-00001-nbf | gestao-de-dados-api-00002-sed | verified |
| prefeituraituiutabalgpdweb | gestao-de-dados-api-00001-kln | gestao-de-dados-api-00002-suy | verified |
| prefeiturateresopolislgpdweb | gestao-de-dados-api-00001-5wt | gestao-de-dados-api-00002-jem | verified |
| saosimaolgpdweb-1a6e5 | gestao-de-dados-api-00001-wc7 | gestao-de-dados-api-00002-vih | verified |

## Impactos e limites

A versão 2.1.0 exige personal_data_consent=true no cadastro; consumidores sem esse campo podem receber 400. Agregados passam a exigir ID token Google e AGGREGATES_TOKEN_AUDIENCE/AGGREGATES_ALLOWED_CALLERS. Valores existentes foram preservados; onde ausentes a rota recusa chamadas (401). Essa integração não foi reconfigurada. Compatibilidade do frontend e fluxos autenticados completos não foram homologados.

Novas revisões e testes podem gerar custos de execução/logs, cold starts e regressões. Runtime, referências de segredos, dados, escala e limites existentes foram preservados. Nenhum IAM, banco, bucket, segredo, DNS, domínio, frontend, GitHub ou pipeline foi alterado. Labels históricas release/commit preservadas; digest e revisão servida determinam a versão observada.

Diferença observada em lgpdweb: o Cloud Run materializou autoscaling.knative.dev/maxScale=100 na revisão, antes implícito. O limite explícito do serviço permaneceu 3; o máximo efetivo continua 3. Não foi passada flag de escala. Evidência em diferenca-default-escala-lgpdweb.json e [documentação do padrão e interação dos limites](https://docs.cloud.google.com/run/docs/configuring/max-instances).

## Reversão

Revisões e distribuição anterior em antes.json; comandos individuais em reversao.md (auxiliar removido; resultado consolidado neste relatório). Em falha, o executor consulta o estado antes de restaurar o tráfego e registra a reversão. Revisões antigas não são removidas. Retornar tráfego não desfaz dados gravados, resolução de segredos latest ou dependências externas; também não restaura sozinho o template de imagem do serviço.

## Arquivos e evidências

[Contexto e autorização](contexto.md), plano e alvos (auxiliar removido; resultado consolidado neste relatório), [leitura dos 65 projetos](leitura-projetos.md), descoberta (auxiliar removido; resultado consolidado neste relatório), release (auxiliar removido; resultado consolidado neste relatório), estado anterior sanitizado (auxiliar removido; resultado consolidado neste relatório), reversão (auxiliar removido; resultado consolidado neste relatório).

Por projeto: baseline, preflight, candidato, depois, resultado e comandos em arquivos próprios. Auditoria-PROJETO, logs-PROJETO e verificacao-final.json documentam a auditoria final quando executada. Scripts operacionais auxiliares foram removidos na limpeza; antes de qualquer nova execução, conferir o estado e a autorização.

Somente esta pasta foi alterada documentalmente. Catálogo e alterações preexistentes preservados. Sem armazenamento de tokens, chaves, senhas ou payloads de segredos. Leitura de manifesto OCI usou token CLI apenas em memória. Nenhum temporário descartável criado; bytecode Python desabilitado nos scripts com imports locais.

Documentação oficial: [deploy por digest](https://docs.cloud.google.com/run/docs/deploying), [teste por tag, promoção e reversão](https://docs.cloud.google.com/run/docs/rollouts-rollbacks-traffic-migration), [update-traffic](https://docs.cloud.google.com/sdk/gcloud/reference/run/services/update-traffic).

## Comandos de reversão consolidados


Executar somente para reverter a operação autorizada, após conferir o estado atual. Comandos não executados nesta preparação.

```bash
gcloud run services update-traffic gestao-de-dados-api --project=cachoeiradouradamglgpdweb --region=us-central1 --to-revisions=gestao-de-dados-api-00001-x7z=100
```

```bash
gcloud run services update-traffic gestao-de-dados-api --project=camaraconceicaoalagoaslgpdweb --region=us-central1 --to-revisions=gestao-de-dados-api-00001-x66=100
```

```bash
gcloud run services update-traffic gestao-de-dados-api --project=camarafrutallgpdweb --region=us-central1 --to-revisions=gestao-de-dados-api-00001-c2v=100
```

```bash
gcloud run services update-traffic gestao-de-dados-api --project=camaraituiutabalgpdweb-a1a06 --region=us-central1 --to-revisions=gestao-de-dados-api-00001-q7w=100
```

```bash
gcloud run services update-traffic gestao-de-dados-api --project=camarateresopolislgpdweb --region=us-central1 --to-revisions=gestao-de-dados-api-00001-jrn=100
```

```bash
gcloud run services update-traffic gestao-de-dados-api --project=cides-lgpdweb --region=us-central1 --to-revisions=gestao-de-dados-api-00001-wqr=100
```

```bash
gcloud run services update-traffic gestao-de-dados-api --project=cisalp-lgpdweb --region=us-central1 --to-revisions=gestao-de-dados-api-00001-gvr=100
```

```bash
gcloud run services update-traffic gestao-de-dados-api --project=cm-araguari-lgpdweb --region=us-central1 --to-revisions=gestao-de-dados-api-00001-947=100
```

```bash
gcloud run services update-traffic gestao-de-dados-api --project=cm-campo-florido-lgpdweb --region=us-central1 --to-revisions=gestao-de-dados-api-00001-xws=100
```

```bash
gcloud run services update-traffic gestao-de-dados-api --project=frutallgpdweb-3dab8 --region=us-central1 --to-revisions=gestao-de-dados-api-00001-tpq=100
```

```bash
gcloud run services update-traffic gestao-de-dados-api --project=lgpdweb --region=us-central1 --to-revisions=gestao-de-dados-api-rel-1-0-0=100
```

```bash
gcloud run services update-traffic gestao-de-dados-api --project=lgpdwebsaaeituiutaba --region=us-central1 --to-revisions=gestao-de-dados-api-00001-7w9=100
```

```bash
gcloud run services update-traffic gestao-de-dados-api --project=pm-coromandel-mg-lgpdweb --region=us-central1 --to-revisions=gestao-de-dados-api-00001-b2c=100
```

```bash
gcloud run services update-traffic gestao-de-dados-api --project=pm-estreladosul-mg-lgpdweb --region=us-central1 --to-revisions=gestao-de-dados-api-00001-k45=100
```

```bash
gcloud run services update-traffic gestao-de-dados-api --project=pm-itaguai-rj-lgpdweb --region=us-central1 --to-revisions=gestao-de-dados-api-00001-ck8=100
```

```bash
gcloud run services update-traffic gestao-de-dados-api --project=pm-machado-lgpdweb --region=us-central1 --to-revisions=gestao-de-dados-api-00001-sst=100
```

```bash
gcloud run services update-traffic gestao-de-dados-api --project=pm-montecarmelo-mg-lgpdweb --region=us-central1 --to-revisions=gestao-de-dados-api-00001-nxh=100
```

```bash
gcloud run services update-traffic gestao-de-dados-api --project=pm-pedrinopolis-lgpdweb --region=us-central1 --to-revisions=gestao-de-dados-api-00001-vk7=100
```

```bash
gcloud run services update-traffic gestao-de-dados-api --project=pm-sao-joao-del-rei-mg --region=us-central1 --to-revisions=gestao-de-dados-api-00002-l6h=100
```

```bash
gcloud run services update-traffic gestao-de-dados-api --project=pm-tupaciguara-mg-lgpdweb --region=us-central1 --to-revisions=gestao-de-dados-api-00001-vzz=100
```

```bash
gcloud run services update-traffic gestao-de-dados-api --project=pmdeltamglgpdweb --region=us-central1 --to-revisions=gestao-de-dados-api-00001-t4d=100
```

```bash
gcloud run services update-traffic gestao-de-dados-api --project=pmsgalgpdweb-32cf8 --region=us-central1 --to-revisions=gestao-de-dados-api-00001-nbf=100
```

```bash
gcloud run services update-traffic gestao-de-dados-api --project=prefeituraituiutabalgpdweb --region=us-central1 --to-revisions=gestao-de-dados-api-00001-kln=100
```

```bash
gcloud run services update-traffic gestao-de-dados-api --project=prefeiturateresopolislgpdweb --region=us-central1 --to-revisions=gestao-de-dados-api-00001-5wt=100
```

```bash
gcloud run services update-traffic gestao-de-dados-api --project=saosimaolgpdweb-1a6e5 --region=us-central1 --to-revisions=gestao-de-dados-api-00001-wc7=100
```


