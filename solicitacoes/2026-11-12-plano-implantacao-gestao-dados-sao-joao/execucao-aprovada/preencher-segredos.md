# Preenchimento posterior da neogov-auth

Projeto: `pm-sao-joao-del-rei-mg`. Os dois recursos foram criados sem valores. Não envie chaves pelo chat nem as grave nesta pasta.

1. Cadastre na neogov-auth o vínculo do tenant São João del-Rei com Gestão de Dados. Frontend: `https://pmsaojoaodelreimg.gestaodedados.neogov.com.br`. API planejada: `https://api.pmsaojoaodelreimg.gestaodedados.neogov.com.br` (DNS/TLS ainda não configurados).
2. No [segredo NEOGOV_AUTH_API_KEY](https://console.cloud.google.com/security/secret-manager/secret/NEOGOV_AUTH_API_KEY/versions?project=pm-sao-joao-del-rei-mg), use **Adicionar nova versão** e informe a chave BFF gerada para este vínculo.
3. No [segredo NEOGOV_AUTH_ALLOWED_ISSUERS](https://console.cloud.google.com/security/secret-manager/secret/NEOGOV_AUTH_ALLOWED_ISSUERS/versions?project=pm-sao-joao-del-rei-mg), adicione uma versão com os valores exatos de `iss` aceitos, separados por vírgula, sem curingas. Não copiar emissores de outro cliente.
4. Confirme que as versões estão ENABLED. Para prosseguir, basta informar que preencheu; não informe os valores. A próxima execução consultará metadados e fixará os números das versões.

`env.yaml` contém variáveis não secretas; não coloque as chaves nesse arquivo. `cloud-run.template.json` contém marcadores explícitos para a imagem e versões. Não aplicar o template antes de resolver todos os marcadores e verificar o acesso à imagem central. O template não contém chave JSON nem define ADC.

A URL da central foi preparada como `https://api.auth.neogov.com.br`, conforme o roteiro de produção; confirme compatibilidade com o vínculo criado. Produção/us-central1 e o hostname da API foram confirmados pelo usuário. Política de backup/retensão, liberação pública e a solução DNS/TLS ainda precisam ser fechadas antes do uso real. Nenhum serviço Cloud Run desta instalação foi criado nesta fase.
