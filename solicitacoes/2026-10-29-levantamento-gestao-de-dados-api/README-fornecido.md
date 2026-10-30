# Gestão de Dados — API

API NestJS 11 (Express) e TypeScript para o sistema Gestão de Dados da NEOGOV.
As regras de organização, dependências e erros estão em [ARCHITECTURE.md](ARCHITECTURE.md).
Mudanças são planejadas em [openspec/](openspec/).

 O [passo a passo de implantação](#implantação-no-gcp)
reúne os componentes, acessos e configurações necessários. A
[pipeline](#pipeline-de-publicação-e-deploy) publica as imagens no projeto central
`artefatos`; cada cliente tem sua própria API e seus dados no ambiente de produção.


## Desenvolvimento local

Use Node 24 (recomendado, como Docker e CI), npm e, para acessar dados reais, Google Cloud CLI.
O mínimo local declarado é Node 22. Com nvm:

```bash
nvm install
nvm use
npm ci
```

Em um novo checkout, crie `.env` a partir do exemplo:

```bash
cp .env.example .env
```

Se você já tem `.env`, mantenha suas configurações e confira as variáveis abaixo.
`GOOGLE_CLOUD_PROJECT`, `STORAGE_BUCKET`, `NEOGOV_AUTH_BASE_URL`, `NEOGOV_AUTH_API_KEY` e `NEOGOV_AUTH_ALLOWED_ISSUERS` são obrigatórios; o exemplo usa um projeto fictício para iniciar
sem acesso remoto. Substitua pelo projeto autorizado ao desenvolver operações de dados.

```bash
npm run start:dev
```

Na porta padrão 3000:

- `http://localhost:3000/docs`: Swagger UI.
- `http://localhost:3000/docs-json`: documento OpenAPI gerado.


## Variáveis de ambiente

A configuração é carregada com `@nestjs/config` e validada uma única vez antes de iniciar HTTP.
Configuração inválida impede a inicialização e informa somente os nomes das variáveis inválidas.
Variáveis do processo têm precedência sobre `.env`.

| Variável | Padrão / uso |
| --- | --- |
| `NODE_ENV` | `development`; aceita `development`, `test` e `production` |
| `PORT` | `3000`; inteiro de 1 a 65535. Cloud Run/Docker usam 8080 |
| `FRONTEND_ORIGIN` | `http://localhost:4200`; uma origem HTTP(S), sem caminho, barra final, query ou credenciais. CORS permite credentials para essa origem |
| `GOOGLE_CLOUD_PROJECT` | Obrigatório; projeto usado pelos providers Firestore e Storage |
| `FIRESTORE_DATABASE_ID` | `(default)`; também aceita banco nomeado |
| `STORAGE_BUCKET` | Obrigatório; nome de bucket sem URL ou caminho de objeto; selecionado pelo service de arquivos |
| `GOOGLE_APPLICATION_CREDENTIALS` | Opcional; caminho externo de credencial ADC, interpretado pelo SDK |
| `FIRESTORE_EMULATOR_HOST` | Opcional; `host:porta` sem protocolo, interpretado pelo SDK Firestore |
| `NEOGOV_AUTH_BASE_URL` | Obrigatória; URL HTTP(S) da API central de autenticação |
| `NEOGOV_AUTH_API_KEY` | Obrigatória; segredo BFF do vínculo tenant/sistema, somente no backend |
| `NEOGOV_AUTH_ALLOWED_ISSUERS` | Obrigatória; lista de emissores exatos separados por vírgulas, sem padrão ou curingas |
| `NEOGOV_AUTH_TIMEOUT_MS` | `5000`; timeout positivo em milissegundos das chamadas centrais |
| `AUTH_COOKIE_SECURE` | `false` localmente; controla Secure e deve ser `true` em produção ou com SameSite=none |
| `AUTH_COOKIE_SAME_SITE` | `lax`; aceita `lax`, `strict` ou `none`. None exige Secure e HTTPS |

Configure a URL, a chave BFF e os emissores exatos da neogov-auth para o vínculo
tenant/sistema. Mantenha a chave somente no backend, via Secret Manager em produção.
O autocadastro exige `SELF_SERVICE` habilitado no vínculo.

A sessão usa cookie HttpOnly `access_token`, validado na central a cada requisição
autenticada. O `iss` deve corresponder exatamente a `NEOGOV_AUTH_ALLOWED_ISSUERS`;
emissor inválido retorna 401 e central indisponível retorna 503, sem liberar acesso.


## Firestore e Cloud Storage

O `CloudModule` fornece os SDKs oficiais: repositories usam Firestore e services de
arquivos usam Storage. Consulte o [schema dos dados](docs/firestore-schema.md).

Localmente, use ADC com impersonação de uma conta de serviço para acessar os dados
e gerar URLs assinadas:

```bash
gcloud auth application-default login \
  --impersonate-service-account=CONTA_DE_SERVICO@PROJETO.iam.gserviceaccount.com
```

Seu usuário precisa de `roles/iam.serviceAccountTokenCreator` na conta impersonada,
com a API IAM Service Account Credentials habilitada. A conta deve ter acesso ao
Firestore e aos objetos do bucket. Reinicie a API após alterar o ADC.
No Cloud Run, os SDKs usam a conta de execução; os acessos necessários estão no
[passo a passo de implantação](#implantação-no-gcp).

Para usar o Firestore Emulator, inicie-o separadamente e configure
`FIRESTORE_EMULATOR_HOST=127.0.0.1:8080` e um projeto local no `.env`.
Isso não emula o Cloud Storage.

## Contratos HTTP e novos módulos

A função `configureApp` centraliza CORS, shutdown, Swagger e o `ValidationPipe` do Nest
com `transform`, `whitelist` e `forbidNonWhitelisted`. DTOs de entrada usam decorators
de `class-validator`; campos desconhecidos e valores inválidos retornam 400.
Veja a [documentação oficial do ValidationPipe](https://docs.nestjs.com/techniques/validation).

Crie os módulos de negócio em `src/modules/<dominio>/`, com controller → service.
O service usa repositories para banco, clients para APIs e services próprios para
outros recursos. Crie entidades, DTOs e mappers conforme `ARCHITECTURE.md`.
Services, repositories e clients usam erros de aplicação de
`src/common/errors/application.error.ts`. O filtro global é o único lugar que converte
categorias em 400/401/404/409/422/503; erros inesperados retornam 500 com mensagem genérica.

```json
{
  "status_code": 404,
  "code": "RESOURCE_NOT_FOUND",
  "message": "Not found",
  "timestamp": "2026-10-12T18:00:00.000Z"
}
```

O consumidor decide com base em `code`. Mensagens de erros da aplicação são públicas
e devem ser escritas sem dados sensíveis. Cada endpoint documenta seu DTO de sucesso
e os status de erro aplicáveis usando `ApiErrorResponses` e `ErrorResponseDto`.

## Logs

A API emite JSON por linha compatível com a coleta integrada do Cloud Run,
incluindo logs do NestJS, bootstrap, conclusão HTTP e erros do filtro global.
Severidades e campos de correlação seguem o contrato do Cloud Logging, com
sanitização central e contexto assíncrono isolado por requisição. Não há nova
variável obrigatória, SDK ou permissão IAM de escrita de logs.

O [guia de logging](docs/logging.md) descreve os campos, limites, exemplos,
consultas e o roteiro obrigatório de homologação da ingestão no Cloud Run.
Testes locais verificam a emissão; o aceite no destino exige inspecionar os
`LogEntry` de uma revisão implantada com a mudança.

## Verificação

```bash
npm run lint          # verifica e corrige problemas automaticamente
npm run lint:check    # verifica sem alterar arquivos, falha também em warnings
npm run format
npm run format:check
npm run build
npm test -- --runInBand
npm run test:e2e -- --runInBand
npm run test:cov
```

Os testes ignoram `.env`, usam projeto e bucket fictícios e não acessam a GCP.
Os e2e verificam DTOs, CORS, categorias de erro e o schema compartilhado de erro no OpenAPI.
As rotas usadas para exercitar os contratos HTTP existem somente nos testes.
O TypeScript usa `strict`. O ESLint verifica fronteiras entre camadas; ciclos e dependências
entre módulos também devem ser conferidos na revisão de código.

Para executar o build:

```bash
npm run build
npm run start:prod
```

## Container local

```bash
docker build -t gestao-de-dados-api:local .
docker run --rm --env-file .env -e PORT=8080 -p 8080:8080 gestao-de-dados-api:local
```

O container usa Node 24 e usuário sem privilégios; `.env` não é copiado para a imagem.
Acesso remoto local via container precisa de credenciais ADC disponibilizadas ao runtime;
o exemplo acima apenas inicia a API e seus endpoints locais.

## Implantação no GCP

Cada novo cliente recebe um ambiente de **produção** com sua própria API no Cloud
Run, banco Firestore, bucket, conta de execução, segredo e configuração da
neogov-auth. Prepare esses componentes na ordem abaixo, usando os dados do cliente.

### 1. Definir o ambiente e habilitar os serviços

No console GCP, selecione o projeto de produção do cliente. Registre seu ID e
número, a região dos recursos, o nome do serviço Cloud Run e os domínios da API
e do frontend.

Em **APIs e serviços**, habilite:

| API | Uso |
| --- | --- |
| Cloud Run (`run.googleapis.com`) | Executar a API |
| Firestore (`firestore.googleapis.com`) | Armazenar os dados |
| Cloud Storage (`storage.googleapis.com`) | Armazenar as mídias |
| IAM (`iam.googleapis.com`) | Gerenciar contas de serviço |
| IAM Service Account Credentials (`iamcredentials.googleapis.com`) | Assinar URLs de upload e download |
| Secret Manager (`secretmanager.googleapis.com`) | Disponibilizar a chave BFF à aplicação |

### 2. Criar a conta de execução e liberar a leitura da imagem

Em **IAM e administração → Contas de serviço**, crie uma conta no projeto do
cliente, por exemplo `gestao-de-dados-api-runtime`. Ela será selecionada no Cloud
Run como identidade da aplicação. Os acessos aos dados e ao segredo serão
concedidos nas próximas etapas; não é necessário gerar uma chave JSON.

Para importar a imagem de `artefatos`, o Cloud Run usa seu próprio agente
gerenciado pelo Google: `service-NUMERO_DO_PROJETO@serverless-robot-prod.iam.gserviceaccount.com`.
Conceda a ele `roles/artifactregistry.reader` no repositório `gestao-de-dados-api`,
em `artefatos`, região `us-central1`. Esse acesso permite que a plataforma leia
a imagem, independentemente das permissões da conta principal que faz o deploy.

### 3. Criar o banco Firestore e seus índices

No **Firestore**, crie um banco em modo **Native**, com ID como `gestao-de-dados`,
na região definida para os dados do cliente. Anote esse ID: ele será informado
em `FIRESTORE_DATABASE_ID` na configuração do Cloud Run.

Conceda à conta de execução o papel `roles/datastore.user` no projeto do cliente.
Se houver vários bancos com acessos distintos, restrinja a concessão por condição
IAM ao banco da API. O acesso do backend usa IAM; regras Firebase de clientes web
não substituem essa permissão.

Na área de índices do banco, crie os quatro índices compostos da coleção
`complaints`, com escopo de **coleção**, conforme
[firestore.indexes.json](firestore.indexes.json):

| Índice | Campos, na ordem |
| --- | --- |
| 1 | `reportedBy` crescente, `timestamp` decrescente, `__name__` decrescente |
| 2 | `reportedBy` crescente, `status` crescente, `timestamp` decrescente, `__name__` decrescente |
| 3 | `reportedBy` crescente, `reasonCode` crescente, `timestamp` decrescente, `__name__` decrescente |
| 4 | `reportedBy` crescente, `status` crescente, `reasonCode` crescente, `timestamp` decrescente, `__name__` decrescente |

O campo `__name__` representa o nome do documento; confirme sua ordenação na
configuração final de cada índice. Aguarde todos em estado `READY` antes de
liberar o ambiente. Se o banco já existir, crie apenas os índices ausentes.

As coleções de um banco vazio são criadas pelas escritas da aplicação, seguindo o
[schema](docs/firestore-schema.md). Se o cliente tiver dados legados, faça backup
e execute o [roteiro de migração](docs/implantacao-prod/roteiro-migracao-solicitacoes.md)
antes da liberação.

### 4. Criar o bucket e configurar upload e download

No **Cloud Storage**, crie um bucket para as mídias do cliente, com nome
globalmente único e região adequada à instalação. Ative o acesso uniforme no
nível do bucket e a prevenção de acesso público. Anote o nome para configurar
`STORAGE_BUCKET` no Cloud Run.

Conceda à conta de execução:

| Papel | Onde conceder | Finalidade |
| --- | --- | --- |
| `roles/storage.objectCreator` | Bucket de mídias do cliente | Criar objetos por upload direto |
| `roles/storage.objectViewer` | Mesmo bucket | Ler objetos e conferir seus metadados |
| `roles/iam.serviceAccountTokenCreator` | Na própria conta de execução | Permitir que ela assine URLs por `signBlob` |

Configure também o **CORS do bucket** com os seguintes valores:

| Configuração | Valor |
| --- | --- |
| Origem permitida | Origem HTTPS do frontend do cliente, sem barra final |
| Métodos | `GET` e `PUT` |
| Headers de resposta | `Content-Type` e `x-goog-if-generation-match` |
| Cache do preflight | 300 segundos |

Esse CORS permite que o navegador envie e leia arquivos diretamente no Storage;
é uma configuração separada do CORS da API. Não inclua `OPTIONS` na lista de
métodos. Em bucket compartilhado, preserve as regras dos outros consumidores.
Se houver mídias legadas em outros buckets, conceda também leitura nesses buckets
à conta de execução.

### 5. Preparar a neogov-auth e criar o segredo

Com o responsável pela **neogov-auth**, configure o vínculo entre o tenant do
cliente e o sistema Gestão de Dados. Obtenha a URL da central, a chave BFF desse
vínculo e os valores exatos de `iss` que a instalação aceitará. Se houver
autocadastro, habilite `SELF_SERVICE` no vínculo.

No **Secret Manager** do projeto do cliente:

1. Crie um segredo, por exemplo `neogov-auth-api-key`.
2. Adicione a chave BFF como uma versão desse segredo.
3. Conceda à conta de execução `roles/secretmanager.secretAccessor` nesse segredo.
4. Anote o nome e o número da versão para associá-los ao Cloud Run.

A chave será disponibilizada somente ao backend pela variável
`NEOGOV_AUTH_API_KEY`. Para uma rotação futura, adicione uma versão e atualize
a revisão do serviço para usar esse novo número.

### 6. Criar e configurar o serviço Cloud Run

Selecione uma release aprovada publicada pela `master` e obtenha seu **digest**
no resumo do job `publish` do GitHub Actions. O caminho da imagem é
`us-central1-docker.pkg.dev/artefatos/gestao-de-dados-api/gestao-de-dados-api`;
selecione a referência terminada em `@sha256:…` para fixar a versão.

No **Cloud Run**, crie um serviço no projeto do cliente:

1. Escolha a imagem pelo digest aprovado.
2. Defina o nome do serviço, por exemplo `gestao-de-dados-api`, e sua região.
3. Selecione a conta de execução criada na etapa 2 como identidade do serviço.
4. Configure a porta do container como **8080**.
5. Ajuste CPU, memória, concorrência, timeout e limites de instâncias à carga esperada.
6. Configure as variáveis e a referência ao segredo descritas abaixo.
7. No primeiro deploy, mantenha a invocação restrita até configurar o acesso na etapa 7.
8. Implante o serviço e aguarde a revisão ficar pronta.

Na configuração do container, preencha:

| Variável | Valor para a instalação |
| --- | --- |
| `NODE_ENV` | `production` |
| `GOOGLE_CLOUD_PROJECT` | ID do projeto do cliente |
| `FIRESTORE_DATABASE_ID` | ID do banco criado na etapa 3 |
| `STORAGE_BUCKET` | Nome do bucket criado na etapa 4, sem `gs://` |
| `FRONTEND_ORIGIN` | Origem HTTPS do frontend do cliente, sem barra final |
| `NEOGOV_AUTH_BASE_URL` | URL da central de autenticação |
| `NEOGOV_AUTH_ALLOWED_ISSUERS` | Emissores exatos aceitos, separados por vírgulas |
| `NEOGOV_AUTH_TIMEOUT_MS` | `5000` |
| `AUTH_COOKIE_SECURE` | `true` |
| `AUTH_COOKIE_SAME_SITE` | `lax`; use `none` se frontend e API estiverem em sites distintos |

Na área de secrets do container, associe `NEOGOV_AUTH_API_KEY` ao segredo da
etapa 5 e selecione uma **versão numérica fixa**. As credenciais Google são
fornecidas pela conta de execução vinculada ao serviço.

Em atualizações, edite o serviço existente e crie uma revisão com o novo digest,
preservando as variáveis, o segredo e a política de acesso HTTP do cliente.

### 7. Configurar o acesso do frontend, o domínio e HTTPS

Para chamadas diretas do navegador, configure a invocação do serviço Cloud Run
para permitir requisições sem token IAM Google, concedendo
`roles/run.invoker` a `allUsers` no serviço. As rotas protegidas continuam
exigindo o cookie validado pela neogov-auth. Se a política da organização impedir
essa concessão, defina a alternativa de entrada HTTP com a infraestrutura.

Para disponibilizar a API no domínio do cliente:

1. Defina o hostname da API e identifique a zona DNS responsável.
2. Configure o roteamento até o serviço Cloud Run e seu certificado TLS. Se usar
   Application Load Balancer externo global, prepare IP reservado, NEG serverless,
   backend, URL map, proxy HTTPS e regra de encaminhamento.
3. Publique os registros DNS exigidos pela solução e aguarde o certificado ficar
   válido. Consulte as opções de
   [domínio personalizado](https://docs.cloud.google.com/run/docs/mapping-custom-domains).
4. Configure a URL final da API no frontend e confira sua origem em
   `FRONTEND_ORIGIN` e no CORS do bucket.

O frontend deve enviar `credentials: include` para usar o cookie da API.
Confirme a saída HTTPS do Cloud Run para a neogov-auth. Configure VPC/egresso e
Cloud NAT apenas se a instalação exigir rede privada ou IP fixo de saída.

### 8. Validar e registrar a implantação do cliente

Antes de liberar o ambiente, verifique:

- Revisão pronta, digest aprovado, conta de execução e versão do segredo corretos.
- Quatro índices `READY` no banco do cliente.
- Login, consulta de perfil, logout e recusa de sessão inválida.
- Criação, consulta, filtros, comentários, encerramento e agregados.
- Upload pelo navegador e download por URL assinada, incluindo CORS e expiração.
- Domínio HTTPS, cookies, acesso à central e logs no Cloud Logging.

O boot não testa as dependências remotas. Execute o
[roteiro de homologação](docs/implantacao-prod/homologacao-solicitacoes.md) e confira
a ingestão pelo [guia de logs](docs/logging.md). Defina também a exposição do
Swagger, disponível em `/docs` e `/docs-json`.

Registre cliente, projeto, região, serviço, domínio, commit, digest, revisão,
versão do segredo, horário e responsável. Em uma atualização com falha, use a
área de gerenciamento de tráfego do Cloud Run para direcionar 100% das requisições
à revisão anterior validada. Esse retorno não desfaz mudanças em dados, IAM, DNS
ou segredos.

## Pipeline de publicação e deploy

Para as instalações de produção, use uma imagem publicada pela branch `master`.
O workflow [ci.yml](.github/workflows/ci.yml) executa lint, build e testes
unitários/e2e antes de publicar no Artifact Registry de `artefatos`.

Pull requests executam lint, build, testes unitários/e2e e build Docker sem
publicar imagens ou fazer deploy. A publicação ocorre somente no evento `push`
em `develop` ou `master`, após os testes passarem, incluindo o push gerado pelo
merge de um PR. Execuções manuais executam apenas as validações da aplicação.

A publicação gera as tags `master`, `latest` e a versão do `package.json`, além
do digest registrado no resumo do job `publish`. Use esse digest na etapa 6 da
[implantação](#implantação-no-gcp). A publicação não atualiza as APIs dos clientes:
cada ambiente recebe a versão aprovada em um deploy próprio.

### Variáveis do repositório no GitHub

Configure uma vez em **Settings → Secrets and variables → Actions → Variables**:

| Variável | Valor |
| --- | --- |
| `GCP_ARTIFACT_REGISTRY_LOCATION` | `us-central1` |
| `GCP_ARTIFACT_REGISTRY_REPOSITORY` | `gestao-de-dados-api` |
| `GCP_ARTIFACT_REGISTRY_IMAGE` | `gestao-de-dados-api` |
| `GCP_WORKLOAD_IDENTITY_PROVIDER` | `projects/1012140942605/locations/global/workloadIdentityPools/github/providers/neogovbr` |
| `GCP_SERVICE_ACCOUNT` | `github-publicador@artefatos.iam.gserviceaccount.com` |

A conta publicadora precisa de `roles/artifactregistry.writer` no repositório
de imagens. O repositório GitHub, via provider informado, precisa de
`roles/iam.workloadIdentityUser` nessa conta. Essas permissões são da publicação
central; os acessos ao ambiente de cada cliente são configurados no guia acima.

Atualize a versão do `package.json` a cada release. As tags podem mudar de destino;
registre e implante sempre o digest aprovado para o cliente.
