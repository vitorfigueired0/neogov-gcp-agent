# Deploy de Gestão de Dados — São João del-Rei

> Conservação documental — 13/11/2026: por pedido do usuário, foram mantidos o contexto, o relatório final e as entregas finais. Arquivos auxiliares, evidências separadas, scripts, verificações, diffs e backups locais foram removidos; referências a eles no histórico descrevem a execução original, não arquivos ainda disponíveis. Os resultados não foram reconsultados no GCP durante esta limpeza. Recuperação que dependa dos backups removidos exige outra cópia ou versão disponível no Git.

Data: 2026-11-12T10:20:22.124691-03:00, America/Sao_Paulo. Projeto `pm-sao-joao-del-rei-mg` (971507433447), produção/us-central1.

**API implantada, Ready e respondendo na URL padrão. Domínio personalizado ainda depende de DNS externo e emissão de certificado.**

URL acessível: [https://gestao-de-dados-api-971507433447.us-central1.run.app](https://gestao-de-dados-api-971507433447.us-central1.run.app/docs). Domínio final: `https://api.pmsaojoaodelreimg.gestaodedados.neogov.com.br` (não declarado pronto).

## Publicação e recursos afetados

Criado o serviço Cloud Run `gestao-de-dados-api`, inicialmente com invocação IAM restrita. Foi verificado HTTP 403 sem credenciais antes da abertura. Depois foi desabilitada a checagem IAM de invocação, permitindo chamadas do navegador; a política do serviço continua sem allUsers. A autenticação de negócio permanece na aplicação/neogov-auth. Documentação /docs e /docs-json fica pública.

Revisão atual: `gestao-de-dados-api-00002-l6h`, Ready=True, tráfego 100%. Imagem selecionada pelas tags master/latest/2.0.0 e fixada em `us-central1-docker.pkg.dev/artefatos/gestao-de-dados-api/gestao-de-dados-api@sha256:d7f64a47030cbccad5cc5a7b4ae16ae95158651fe1548f8a364c5d6a3ea3c505`. A revisão resolve o manifesto de plataforma `sha256:5d9ed6fca626a3b9544aed13286442246b17b5af34af0f1cb15ea5ba2cfdbf0a`; a prova do índice OCI (auxiliar removido; resultado consolidado neste relatório) confirma que é o membro linux/amd64 da imagem selecionada. O repositório não retornou proveniência de build/assinatura; não foi alegada verificação de commit ou pipeline que não ocorreu.

Configuração: 1 vCPU, 1 GiB, porta 8080, concorrência 80, timeout HTTP 300 s, min 0/max 3, runtime dedicada, banco gestao-de-dados, bucket dedicado, origem frontend informada e versões 1 dos dois segredos. Cookie Secure/SameSite=lax. Manifesto final (auxiliar removido; resultado consolidado neste relatório) sem payloads. Min zero pode gerar cold starts e max três limita capacidade sem garantir teto financeiro.

Adicionado reader somente para o agente gerenciado `service-971507433447@serverless-robot-prod.iam.gserviceaccount.com` no repositório `artefatos/us-central1/gestao-de-dados-api`. Políticas anteriores e posteriores preservadas. Não foi ampliado o acesso da runtime a dados ou segredos. Não foram alterados serviços/bancos/buckets antigos, frontend, central neogov-auth ou dados de negócio.

## Verificações e ajuste observado

Na revisão final: /docs-json e /docs responderam 200; GET /auth/self e /complaints, sem sessão e com cookie deliberadamente inválido, responderam 401/INVALID_SESSION; preflight OPTIONS respondeu 204, Access-Control-Allow-Origin igual à origem informada e credentials=true. Evidência: HTTP final (auxiliar removido; resultado consolidado neste relatório). A URL canônica por número do projeto também respondeu 200 em /docs-json. Os quatro índices foram revalidados READY antes do deploy.

Houve um 503/AUTH_PROVIDER_UNAVAILABLE no primeiro teste com sessão inválida, após aproximadamente 5 s. Testes subsequentes retornaram 401 em menos de 1 s sem trocar a chave. Foi elevado NEOGOV_AUTH_TIMEOUT_MS de 5000 para 20000 como mitigação de timeout transitório; causa da lentidão da central não comprovada. Isso pode fazer falhas demorarem até 20 s. Diagnóstico e limites (auxiliar removido; resultado consolidado neste relatório). A consulta de erros da revisão final após os testes retornou vazia, limitada ao intervalo/volume solicitado; não é garantia de ausência de erros futuros. A primeira prova usou /auth/me, que retornou 404; o contrato OpenAPI indicou /auth/self, usado na verificação final.

Não foram executados login válido, escrita/consulta de dados de negócio, geração de URLs assinadas ou upload. Não há credenciais de usuário real fornecidas para homologação; não foram criadas contas de teste nem acessados payloads dos segredos. Testes negativos não provam todos os fluxos funcionais ou todas as regras de autorização. Backup/PITR continuam como pendência de política de recuperação da preparação anterior.

## Domínio e pendência externa

Criado mapeamento somente para `api.pmsaojoaodelreimg.gestaodedados.neogov.com.br` → gestao-de-dados-api. DomainRoutable=True, mas Ready e CertificateProvisioned permanecem Unknown/CertificatePending na leitura mais recente (auxiliar removido; resultado consolidado neste relatório). Foi devolvido o registro:

| Tipo | Nome na zona neogov.com.br | Destino |
| --- | --- | --- |
| CNAME | api.pmsaojoaodelreimg.gestaodedados | ghs.googlehosted.com. |

Os nameservers são ns1/ns2.pajehost.com.br; não há acesso demonstrado ao painel externo nesta sessão. A última consulta de CNAME continua vazia. A publicação foi solicitada ao usuário; não foi presumida nem executada pelo agente. Instruções exatas (auxiliar removido; resultado consolidado neste relatório). O certificado depende de DNS e pode levar tempo para emitir. A URL run.app está disponível para diagnóstico; não foi alterado o frontend para usá-la, pois o cookie lax precisa ser avaliado no site final.

Mapeamento direto segue o padrão histórico das instalações e está em Preview, com limitações de suporte/latência/TLS documentadas pelo Google e comunicadas antes da criação. Não foi criado balanceador/IP adicional. A documentação online lista um dry-run ausente no gcloud 560.0.0 instalado; a tentativa falhou no parser, sem operação remota. O help local comprovou a ausência, foi preservado e nenhuma ferramenta foi atualizada. Uma consulta de propriedade também rejeitou a opção de filtro sem efeito remoto; a criação bem-sucedida comprovou a capacidade de mapear o hostname com a identidade existente.

## Custos e reversão

Cloud Run, armazenamento/operações, logs, segredos e tráfego podem gerar cobrança. Não houve cálculo monetário ou mudança de billing. O índice de imagem não foi reconstruído/publicado; apenas lido e importado pela plataforma.

Para retirar a exposição da nova instalação, reabilitar o invoker IAM check no serviço e verificar HTTP 403 sem credenciais; isso interrompe chamadas públicas e não apaga dados. Para desfazer apenas a mitigação de timeout, restaurar NEOGOV_AUTH_TIMEOUT_MS=5000, ciente do retorno do risco observado. O reader adicionado no repositório pode ser retirado somente após avaliar as revisões/consumidores. O mapeamento pode ser removido após avaliar o acesso; não alterar registros DNS preexistentes de outros consumidores. Nenhuma reversão foi executada. Não apagar banco, bucket ou segredos automaticamente; rollback de revisão não desfaz IAM, DNS ou dados.

## Artefatos e integridade

[Contexto](contexto.md), plano concreto (auxiliar removido; resultado consolidado neste relatório), comandos e respostas sanitizadas nos JSON desta pasta. Conta e default gcloud preservados (`desenvolvimento@neogov.com.br`, dashboard-admin-481516), sem login, ADC, impersonação nova ou chaves. A leitura do manifesto OCI usou token da mesma sessão somente em memória, sem exibição/gravação. Nenhuma mensagem foi enviada a terceiros; somente perguntas ao usuário nesta conversa.

[Catálogo atualizado](../../ativos/gestao-de-dados-api/inventario.md): componentes, inventário Markdown/JSON, permissões e custos; histórico anterior preservado, backups dos cinco arquivos em backup-catalogo e diff (auxiliar removido; resultado consolidado neste relatório). Para reversão documental, comparar e restaurar só os arquivos afetados, preservando mudanças posteriores. Os números globais anteriores mantêm sua data histórica.

Verificações documentais em verificacoes.txt. Não foram criados temporários descartáveis nem arquivos de payload; apenas artefatos documentais dentro da solicitação. Alterações preexistentes do workspace preservadas.

Fontes oficiais: [deploy](https://docs.cloud.google.com/run/docs/deploying), [invocação pública e reversão](https://docs.cloud.google.com/run/docs/authenticating/public) e [domínios/certificados e limitações](https://docs.cloud.google.com/run/docs/mapping-custom-domains).
