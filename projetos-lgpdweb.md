# Projetos GCP relacionados ao LGPDWeb

Na consulta de 20/10/2026, foram encontrados **26 projetos com `lgpdweb` no nome ou no ID**, sem diferenciar maiúsculas e minúsculas, acessíveis à conta `desenvolvimento@neogov.com.br`. Todos estavam com status `ACTIVE`.

A lista considera os projetos visíveis à autenticação existente do Google Cloud CLI. Projetos com outros nomes ou sem acesso para essa conta podem também hospedar componentes do LGPDWeb.

## Lista de projetos

| Nome do projeto | ID do projeto |
| --- | --- |
| LGPDWEB | `lgpdweb` |
| pm-neogov-qa-lgpdweb | `pm-neogov-qa-lgpdweb` |
| cides-lgpdweb | `cides-lgpdweb` |
| cisalp-lgpdweb | `cisalp-lgpdweb` |
| cachoeira-dourada-lgpdweb | `cachoeiradouradamglgpdweb` |
| CM-ARAGUARI-LGPDWEB | `cm-araguari-lgpdweb` |
| cm-campo-florido-lgpdweb | `cm-campo-florido-lgpdweb` |
| CamaraConceicaoAlagoasLGPDweb | `camaraconceicaoalagoaslgpdweb` |
| cm-estrela-do-sul-lgpdweb | `cm-estrela-do-sul-lgpdweb` |
| cm-frutal-lgpdweb | `camarafrutallgpdweb` |
| cm-ituiutaba-lgpdweb | `camaraituiutabalgpdweb-a1a06` |
| CamaraItuiutabaOuvidoria | `camaraituiutabalgpdweb` |
| cm-nova-ponte-lgpdweb | `novapontelgpdweb` |
| cm-teresopolis-lgpdweb | `camarateresopolislgpdweb` |
| pm-delta-lgpdweb | `pmdeltamglgpdweb` |
| pm-estrela-do-sul-lgpdweb | `pm-estreladosul-mg-lgpdweb` |
| pm-frutal-lgpdweb | `frutallgpdweb-3dab8` |
| pm-ituiutaba-lgpdweb | `prefeituraituiutabalgpdweb` |
| PM-MACHADO-LGPDWEB | `pm-machado-lgpdweb` |
| pm-monte-carmelo-lgpdweb | `pm-montecarmelo-mg-lgpdweb` |
| PM-Pedrinopolis-LGPDweb | `pm-pedrinopolis-lgpdweb` |
| pm-sao-simao-lgpdweb | `saosimaolgpdweb-1a6e5` |
| pm-sga-lgpdweb | `pmsgalgpdweb-32cf8` |
| pm-teresopolis-lgpdweb | `prefeiturateresopolislgpdweb` |
| pm-tupaciguara-mg-lgpdweb | `pm-tupaciguara-mg-lgpdweb` |
| sae-ituiutaba-lgpdweb | `lgpdwebsaaeituiutaba` |

O projeto `CamaraItuiutabaOuvidoria` foi incluído porque seu ID contém `lgpdweb`.

## Ambiente conhecido

O projeto `pm-neogov-qa-lgpdweb` corresponde ao ambiente de **QA de Gestão de Dados e LGPDweb**, conforme associação confirmada pelo usuário em 12/10/2026 e registrada em [AGENTS.md](AGENTS.md). Os ambientes dos demais projetos não foram classificados nesta consulta.

## Origem da consulta

A listagem foi obtida com o comando de leitura abaixo, seguido da seleção dos nomes ou IDs que contêm `lgpdweb`:

```bash
gcloud projects list --format='json(projectId,name,lifecycleState)'
```

O status `ACTIVE` indica o estado do projeto no GCP e não comprova a disponibilidade das aplicações hospedadas.
