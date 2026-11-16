# Contexto da implantação

Data: 2026-11-12T10:08:30.579242-03:00 (America/Sao_Paulo).

Prompt recebido:

> pode implantar, quero o ambiente rodando

Objetivo: concluir a publicação da API Gestão de Dados e verificar execução no projeto pm-sao-joao-del-rei-mg (produção, us-central1). Frontend fora do escopo. Infraestrutura já criada e segredos versão 1 ENABLED conforme solicitações anteriores; revalidar fatos antes do deploy. Não registrar payloads de segredos. Hostname confirmado: api.pmsaojoaodelreimg.gestaodedados.neogov.com.br; origem frontend: https://pmsaojoaodelreimg.gestaodedados.neogov.com.br. Preservar autenticação/configuração existentes do gcloud. Dependência necessária de imagem: artefatos/us-central1/gestao-de-dados-api; consultar somente o repositório e imagem da aplicação. Confirmar IAM de leitura do agente gerenciado; expor escopo/impactos antes de eventual binding mínimo no repositório. Não operar outros serviços de aplicação nem criar infraestrutura de balanceamento sem definir seu escopo.

Plano: consultas direcionadas; escolher digest de produção; publicar inicialmente com invocação restrita; verificar revisão/boot; liberar HTTP necessário ao frontend; configurar entrada no domínio dentro do escopo confirmado; testar contratos HTTP e observar logs sanitizados. Não modificar dados de negócio ou executar login com credenciais não fornecidas. Qualificar limites do teste funcional. Reversão: retirar exposição da nova instalação; preservar dados, arquivos e versões de segredos. Sem revisão anterior validada nesta instalação.
