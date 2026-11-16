# Contexto da solicitação

Data: 2026-11-12T09:40:59.080510-03:00 (America/Sao_Paulo).

## Prompt recebido

> quero que faça a implantação do gestao de dados no proojetoo pm-sao-joao-del-rei-mg
> caso ele n esteja catalogadoo pode catalogar, e antes de iniciar de fato me mostre qual o passo a passo que será executado

## Resumo técnico

- Objetivo: preparar a implantação de Gestão de Dados no projeto `pm-sao-joao-del-rei-mg`, mostrando o passo a passo antes da execução efetiva.
- Escopo inicial: referências locais, diagnóstico delimitado somente leitura no projeto alvo, catalogação documental se necessária e preparação do plano.
- Projeto alvo: `pm-sao-joao-del-rei-mg`; ambiente ainda não confirmado.
- Recursos, versão da aplicação, região, autenticação, dependências e estado atual: a confirmar.
- Restrições: preservar autenticação/configuração existentes do gcloud; não acessar payloads de segredos nem dados de negócio; não iniciar implantação antes da apresentação do plano; não alterar outros projetos.
- Autorização: catalogação documental permitida; implantação solicitada com apresentação prévia do passo a passo.
- Alterações locais previstas: contexto, evidências sanitizadas, plano, relatório e eventual atualização delimitada do catálogo com backup e diff.

## Esclarecimento posterior do usuário

Escopo confirmado: API e infraestrutura.

Resposta sobre domínios e autenticação, reproduzida:

> [https://pmsaojoaodelreimg.gestaodedados.neogov.com.br](https://pmsaojoaodelreimg.gestaodedados.neogov.com.br)
>
> acho que ainda n tem no auth, vou criar la e cadastroo depois, pode deixar ja gerado as secrets e env  q eu populo depois

Interpretação: origem do frontend informada; criar estruturas dos segredos sem payloads e preparar variáveis. O vínculo neogov-auth será criado pelo usuário posteriormente. Hostname da API proposto pelo agente, ainda não confirmado: `api.pmsaojoaodelreimg.gestaodedados.neogov.com.br`. Produção/us-central1 são propostas, não confirmações do usuário. Frontend fora do escopo de alterações.
