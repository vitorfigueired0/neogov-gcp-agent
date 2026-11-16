# Verificação DNS/HTTPS — acompanhamento assumido pelo usuário

> Conservação documental — 13/11/2026: por pedido do usuário, foram mantidos o contexto, o relatório final e as entregas finais. Arquivos auxiliares, evidências separadas, scripts, verificações, diffs e backups locais foram removidos; referências a eles no histórico descrevem a execução original, não arquivos ainda disponíveis. Os resultados não foram reconsultados no GCP durante esta limpeza. Recuperação que dependa dos backups removidos exige outra cópia ou versão disponível no Git.

Data: 2026-11-12T10:37:12.426499-03:00, America/Sao_Paulo. Projeto `pm-sao-joao-del-rei-mg`, região us-central1.

## Resultado observado

Após o usuário informar publicação do CNAME, a consulta local e a consulta ao DNS público Google confirmaram `api.pmsaojoaodelreimg.gestaodedados.neogov.com.br` → `ghs.googlehosted.com.`, TTL observado 14400 s. Não se afirma propagação em todos os caches. Uma consulta direta a ns1.pajehost.com.br falhou na resolução do nome do nameserver; o limite foi preservado, sem alterar DNS ou concluir que o CNAME estava errado.

Às 10:33 de São Paulo, o mapeamento Cloud Run ainda informava Ready=Unknown e CertificateProvisioned=Unknown/CertificatePending; DomainRoutable=True. O teste TLS terminou com SSLEOFError. Portanto, **HTTPS no domínio definitivo não foi confirmado nesta etapa**. Evidências: DNS e TLS (auxiliar removido; resultado consolidado neste relatório) e estado do mapeamento (auxiliar removido; resultado consolidado neste relatório).

O usuário assumiu explicitamente o acompanhamento do Ready/certificado. A segunda consulta foi abortada antes de produzir evidência. Não foram retomadas consultas remotas após esse pedido; a inspeção local confirmou ausência de processo próprio de acompanhamento. Nenhum mapeamento foi recriado ou configuração alterada para forçar emissão.

## Estado e pendências conhecidas

- O [deploy anterior](../2026-11-12-deploy-gestao-dados-sao-joao/relatorio.md) comprovou a API Cloud Run Ready, com documentação HTTP 200, recusa de sessão ausente/inválida 401 e CORS 204. Não foi feito novo deploy ou novo teste no Cloud Run nesta etapa.
- DNS/certificado: usuário acompanhará; usar o domínio definitivo após validar certificado. A URL padrão Cloud Run segue como referência do deploy anterior.
- Frontend: fora do escopo de alterações. Conferir se sua URL base aponta para `https://api.pmsaojoaodelreimg.gestaodedados.neogov.com.br`; não foi declarada integração ponta a ponta do frontend.
- Homologação funcional: login com usuário real, CRUD e upload/download não exercitados. Nenhuma credencial real de usuário ou dado de negócio foi usado.
- Recuperação: a preparação desta implantação não ativou agenda de backup/PITR; definir política antes de dados reais. Não reconsultado nesta etapa.
- Se houver consumo de GET /complaints/aggregates por relatórios, a configuração específica de autorização ainda precisa ser definida/homologada: o contrato OpenAPI observado cita AGGREGATES_ALLOWED_CALLERS e AGGREGATES_TOKEN_AUDIENCE, e essas duas variáveis não constam na configuração de serviço verificada no deploy. Não foi inferido um principal autorizado nem configurada essa integração automaticamente; o comportamento desse endpoint não foi testado. Isso não impede o processo HTTP de iniciar.

## Arquivos, reversão e limites

Somente registros locais nesta pasta foram criados: contexto sanitizado, evidências, scripts documentais e este relatório. O consolidador para HTTPS pronto foi preparado mas **não executado**; não foi produzido catálogo ou relatório declarando certificado válido. Os três arquivos do catálogo comparados aos backups permanecem inalterados nesta solicitação: true. O [catálogo anterior](../../ativos/gestao-de-dados-api/inventario.md) mantém sua data e os limites do deploy documentado.

Não houve criação, alteração ou exclusão de recursos GCP, DNS ou IAM. Sem mudança remota a reverter. Os arquivos locais podem ser removidos sem afetar GCP, mas isso elimina o histórico; backups preservados. Nenhum temporário de payload foi criado e nenhum segredo foi acessado. A autenticação existente foi preservada, sem login/troca de identidade. Leituras e requisições podem produzir uso/logs residuais; nenhuma análise monetária foi feita.

As verificações locais estão em verificacoes.txt. O pedido foi encerrado com certificado ainda não verificado pelo agente e acompanhamento transferido ao usuário, conforme sua instrução.
