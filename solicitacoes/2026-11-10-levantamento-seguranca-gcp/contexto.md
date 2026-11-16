# Contexto

Data: 2026-11-10T14:35:52.230040-03:00

## Prompt recebido

quero que acesse todos os projeto do gcp, e faça um levantamentoo dos pontoos de atenção em questãoo de segurança, como recursos livre para internet e etc
caso va gerar arquivos de verificação, q não terãoo valor documental, gere em pastas tempoorárias e apague no finnal do processoo (podee ajustar a skill para que esse seja um compoortamento padrãoo)
crie um relatório simples e objetivo de tdo que necessita de atençãooo

## Resumo técnico

Objetivo: diagnóstico de segurança em todos os projetos acessíveis pela identidade existente do gcloud. Prioridade: exposição pública de rede, serviços e dados; IAM e credenciais de contas de serviço. Somente leituras de metadados e políticas; sem habilitar APIs, trocar identidade, consultar payloads de segredos ou corrigir recursos. Universo a confirmar por listagem atual, comparado ao mapeamento local de 29 projetos. APIs indisponíveis e falhas serão registradas separadamente. Não é teste de intrusão nem prova de ausência de vulnerabilidades. Artefatos descartáveis em diretório temporário exclusivo, com limpeza ao final; evidências documentais sanitizadas e relatório nesta pasta.
