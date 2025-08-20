# Agno Documentation Summary

> Arquivo consolidado gerado a partir do README.md do repositório Agno. Use este documento como ponto de partida; para indexar toda a documentação adicional (cookbook, docs/*.md, exemplos), eu posso agregar mais arquivos se você confirmar.

<div align="center" id="top">
  <a href="https://docs.agno.com">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://agno-public.s3.us-east-1.amazonaws.com/assets/logo-dark.svg">
      <source media="(prefers-color-scheme: light)" srcset="https://agno-public.s3.us-east-1.amazonaws.com/assets/logo-light.svg">
      <img src="https://agno-public.s3.us-east-1.amazonaws.com/assets/logo-light.svg" alt="Agno">
    </picture>
  </a>
</div>
<div align="center">
  <a href="https://docs.agno.com">📚 Documentação</a> &nbsp;|&nbsp;
  <a href="https://docs.agno.com/examples/introduction">💡 Exemplos</a> &nbsp;|&nbsp;
  <a href="https://github.com/agno-agi/agno/stargazers">🌟 Dê uma estrela</a>
</div>

## O que é Agno?

[Agno](https://docs.agno.com) é um framework full-stack para construir Sistemas Multi-Agente com memória, conhecimento e raciocínio.

Use o Agno para construir os 5 níveis de Sistemas Agênticos:
- Nível 1: Agentes com ferramentas e instruções.
- Nível 2: Agentes com conhecimento e armazenamento.
- Nível 3: Agentes com memória e raciocínio.
- Nível 4: Equipes de Agentes que podem raciocinar e colaborar.
- Nível 5: Workflows Agênticos com estado e determinismo.

Exemplo: Agente de Raciocínio Nível 1 que usa a API YFinance para responder perguntas:

```python reasoning_finance_agent.py
from agno.agent import Agent
from agno.models.anthropic import Claude
from agno.tools.reasoning import ReasoningTools
from agno.tools.yfinance import YFinanceTools

reasoning_agent = Agent(
    model=Claude(id="claude-sonnet-4-20250514"),
    tools=[
        ReasoningTools(add_instructions=True),
        YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True, company_news=True),
    ],
    instructions="Use tables to display data.",
    markdown=True,
)
```

https://github.com/user-attachments/assets/4ef27ba6-a781-4fb0-b49c-bfd838123c83

## Como começar

Se você é novo no Agno, leia a documentação para construir seu [primeiro Agente](https://docs.agno.com/introduction/agents), converse com ele no [playground](https://docs.agno.com/introduction/playground) e monitore no [agno.com](https://docs.agno.com/introduction/monitoring).

Depois disso, confira a [Galeria de Exemplos](https://docs.agno.com/examples) e construa aplicações do mundo real com Agno.

## Por que Agno?

O Agno ajuda a construir sistemas agênticos de alta qualidade e alto desempenho, economizando horas de pesquisa e boilerplate. Aqui estão alguns recursos que diferenciam o Agno:

- **Agnóstico ao modelo**: fornece uma interface unificada para 23+ provedores de modelos, sem lock-in.
- **Altamente performático**: Agentes instanciam em **~3μs** e usam **~6.5Kib** de memória em média.
- **Raciocínio como primeira classe**: raciocínio melhora a confiabilidade; Agno suporta 3 abordagens: Reasoning Models, `ReasoningTools` ou nossa abordagem customizada de `chain-of-thought`.
- **Nativamente multimodal**: Agentes Agno aceitam texto, imagem, áudio e vídeo como entrada e geram texto, imagem, áudio e vídeo como saída.
- **Arquitetura avançada multi-agente**: Agno fornece uma arquitetura líder de mercado (**Agent Teams**) com raciocínio, memória e contexto compartilhado.
- **Busca Agêntica embutida**: Agentes podem buscar informações em tempo de execução usando 20+ bancos de dados vetoriais. Agno oferece RAG Agêntico de ponta, **totalmente assíncrono e de alto desempenho.**
- **Memória & Armazenamento de Sessão integrados**: Drivers de `Storage` e `Memory` embutidos proporcionam memória de longo prazo e armazenamento de sessão aos agentes.
- **Saídas Estruturadas**: Agentes podem retornar respostas totalmente tipadas usando saídas estruturadas do modelo ou `json_mode`.
- **Rotas FastAPI prontas**: Após construir seus agentes, sirva-os usando rotas FastAPI pré-construídas. 0 a produção em minutos.
- **Monitoramento**: monitore sessões de agentes e desempenho em tempo real em [agno.com](https://app.agno.com).

## Instalação

```shell
pip install -U agno
```

## Exemplo — Agente de Raciocínio

Vamos construir um Agente de Raciocínio para entender as capacidades do Agno.

Salve este código em um arquivo: `reasoning_agent.py`.

```python
from agno.agent import Agent
from agno.models.anthropic import Claude
from agno.tools.reasoning import ReasoningTools
from agno.tools.yfinance import YFinanceTools

agent = Agent(
    model=Claude(id="claude-sonnet-4-20250514"),
    tools=[
        ReasoningTools(add_instructions=True),
        YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True, company_news=True),
    ],
    instructions=[
        "Use tables to display data",
        "Only output the report, no other text",
    ],
    markdown=True,
)
agent.print_response(
    "Write a report on NVDA",
    stream=True,
    show_full_reasoning=True,
    stream_intermediate_steps=True,
)
```

Depois, crie um ambiente virtual, instale dependências, exporte sua `ANTHROPIC_API_KEY` e execute o agente.

```shell
uv venv --python 3.12
source .venv/bin/activate

uv pip install agno anthropic yfinance

export ANTHROPIC_API_KEY=sk-ant-api03-xxxx

python reasoning_agent.py
```

Podemos ver que o Agente está raciocinando sobre a tarefa, usando `ReasoningTools` e `YFinanceTools` para coletar informações. Veja como a saída se parece:

https://github.com/user-attachments/assets/bbb99955-9848-49a9-9732-3e19d77b2ff8

## Exemplo — Equipes Multi-Agente

Agentes são a unidade atômica de trabalho e funcionam melhor quando têm um escopo estreito e poucas ferramentas. Quando o número de ferramentas cresce além do que o modelo pode lidar ou você precisa tratar múltiplos conceitos, use uma equipe de agentes para distribuir a carga.

```python
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools
from agno.team import Team

web_agent = Agent(
    name="Web Agent",
    role="Search the web for information",
    model=OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGoTools()],
    instructions="Always include sources",
    show_tool_calls=True,
    markdown=True,
)

finance_agent = Agent(
    name="Finance Agent",
    role="Get financial data",
    model=OpenAIChat(id="gpt-4o"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True)],
    instructions="Use tables to display data",
    show_tool_calls=True,
    markdown=True,
)

agent_team = Team(
    mode="coordinate",
    members=[web_agent, finance_agent],
    model=OpenAIChat(id="gpt-4o"),
    success_criteria="A comprehensive financial news report with clear sections and data-driven insights.",
    instructions=["Always include sources", "Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)

agent_team.print_response("What's the market outlook and financial performance of AI semiconductor companies?", stream=True)
```

Instale dependências e execute a equipe de agentes:

```shell
pip install duckduckgo-search yfinance

python agent_team.py
```

[Veja este exemplo no cookbook](./cookbook/getting_started/05_agent_team.py)

## Workflows

### O que são Workflows
Workflows (nível 5) são orquestrações determinísticas de Agents e Steps que mantêm estado, checkpoints e regras de retry/branching. Eles permitem construir aplicações agênticas com fluxo de trabalho previsível, reexecutável e observável.

### Como funcionam
- Cada Workflow é composto por passos (steps) que podem ser Agents, funções ou tarefas discretas.
- O estado do Workflow é persistido em um driver de Storage (ex.: Redis, Postgres, S3) para permitir retomar/re-tentar e auditoria.
- Workflows suportam condicionais, dependências entre steps, retries e timeouts.
- Determinismo: ao usar inputs e checkpoints imutáveis, o Workflow pode ser reexecutado para obter o mesmo resultado (útil para reprodutibilidade e depuração).
- Observabilidade: logs, métricas e checkpoints tornam possível monitorar a execução e inspecionar o estado histórico.

### Como usar (visão geral)
1. Defina tasks/Agents pequenas com responsabilidade única.
2. Crie um Workflow com steps ordenados e dependências explícitas.
3. Escolha um driver de Storage para persistência de estado.
4. Configure success_criteria, timeouts e políticas de retry.
5. Execute o Workflow de forma síncrona ou assíncrona e monitore via painel ou logs.

### Exemplo (ilustrativo)
> Observação: o snippet abaixo é um exemplo de alto nível. Consulte a documentação oficial (docs.agno.com) para a API exata.

```python
from agno.workflow import Workflow, Step
from agno.agent import Agent
from agno.models.openai import OpenAIChat

# Agents (pequenas responsabilidades)
fetch_agent = Agent(name="fetch", role="Coletar dados", model=OpenAIChat(id="gpt-4o"), tools=[])
analyze_agent = Agent(name="analyze", role="Analisar dados", model=OpenAIChat(id="gpt-4o"))

# Definição do Workflow
wf = Workflow(
    id="report_workflow",
    steps=[
        Step(id="fetch", run=fetch_agent),
        Step(id="analyze", run=analyze_agent, depends_on=["fetch"]),
        Step(id="format", run=lambda ctx: f"# Report\n\n{ctx['analyze'].result}", depends_on=["analyze"]),
    ],
    state_store="redis://localhost:6379/0",
    deterministic=True,
    max_retries=2,
)

# Executar
result = wf.run({"ticker": "NVDA"})
print(result.output)
```

### Boas práticas
- Mantenha steps pequenos e idempotentes.
- Use storage persistente para checkpoints e retomada.
- Defina timeouts e políticas de retry explícitas.
- Teste cada step isoladamente (testes unitários) e o Workflow de ponta a ponta (testes de integração).
- Instrumente logs e métricas para monitoramento em produção.

### Solução de problemas
- Para retomar execuções, use o ID do Workflow e o estado persistido.
- Inspecione checkpoints e logs para identificar onde ocorreu a falha.
- Habilite verbose/debug em ambientes de teste para capturar o raciocínio completo dos Agents.

## Desempenho

No Agno, somos obcecados por desempenho. Por quê? Porque mesmo fluxos de IA simples podem gerar milhares de agentes. Ao escalar para um número modesto de usuários, o desempenho vira um gargalo. O Agno é projetado para construir sistemas agênticos de alto desempenho:

- Instanciação de agente: ~3μs em média
- Uso de memória: ~6.5Kib em média

> Testado em um Apple M4 MacBook Pro.

Enquanto o tempo de execução de um agente é limitado pela inferência, devemos minimizar o tempo de execução, reduzir uso de memória e paralelizar chamadas de ferramentas. Esses números podem parecer triviais no início, mas nossa experiência mostra que se acumulam mesmo em escala moderada.

### Tempo de instanciação

Vamos medir o tempo necessário para iniciar um Agente com 1 ferramenta. Executaremos a avaliação 1000 vezes para obter uma linha de base.

Você deve rodar a avaliação em sua própria máquina; não aceite esses resultados sem verificar.

```shell
# Setup do ambiente virtual
./scripts/perf_setup.sh
source .venvs/perfenv/bin/activate
# OU Instale dependências manualmente
# pip install openai agno langgraph langchain_openai

# Agno
python evals/performance/instantiation_with_tool.py

# LangGraph
python evals/performance/other/langgraph_instantiation.py
```

> A avaliação acima é executada em um Apple M4 MacBook Pro. Também roda como GitHub Action neste repositório.

LangGraph está à direita; **vamos iniciá-lo primeiro e dar uma vantagem**.

Agno está à esquerda — note como termina antes do LangGraph atingir metade do tempo de execução e antes de iniciar a medição de memória. É assim que o Agno é rápido.

https://github.com/user-attachments/assets/ba466d45-75dd-45ac-917b-0a56c5742e23

### Uso de memória

Para medir uso de memória usamos a biblioteca `tracemalloc`. Primeiro calculamos uma linha de base executando uma função vazia, depois executamos o Agente 1000x e calculamos a diferença. Isso fornece uma medida (razoável) isolada do uso de memória do Agente.

Recomendamos executar a avaliação em sua própria máquina e inspecionar o código para entender como funciona. Se encontrarmos erro, por favor informe.

### Conclusão

Agentes do Agno são projetados para desempenho; embora compartilhemos benchmarks contra outros frameworks, devemos lembrar que precisão e confiabilidade são mais importantes que velocidade.

Como cada framework é diferente e não poderemos otimizar outros frameworks como fazemos com o Agno, em benchmarks futuros iremos comparar apenas com nós mesmos.

## Índice completo da documentação

Para LLMs e assistentes de IA entenderem e navegar pela documentação completa do Agno, fornecemos um arquivo [LLMs.txt](https://docs.agno.com/llms.txt) ou [LLMs-Full.txt](https://docs.agno.com/llms-full.txt).

Esse arquivo é formatado especificamente para sistemas de IA analisarem e referenciaram nossa documentação de forma eficiente.

### Configuração do Cursor

Ao construir agentes Agno, usar a documentação do Agno como fonte no Cursor pode acelerar seu desenvolvimento.

1. No Cursor, abra o menu "Cursor Settings".
2. Encontre a seção "Indexing & Docs".
3. Adicione `https://docs.agno.com/llms-full.txt` à lista de URLs de documentação.
4. Salve as alterações.

Agora o Cursor terá acesso à documentação do Agno.

## Documentação, comunidade e mais exemplos

- Docs: <a href="https://docs.agno.com" target="_blank" rel="noopener noreferrer">docs.agno.com</a>
- Cookbook: <a href="https://github.com/agno-agi/agno/tree/main/cookbook" target="_blank" rel="noopener noreferrer">Cookbook</a>
- Fórum da comunidade: <a href="https://community.agno.com/" target="_blank" rel="noopener noreferrer">community.agno.com</a>
- Discord: <a href="https://discord.gg/4MtYHHrgA8" target="_blank" rel="noopener noreferrer">discord</a>

## Contribuições

Aceitamos contribuições — leia nosso [guia de contribuição](https://github.com/agno-agi/agno/blob/main/CONTRIBUTING.md) para começar.

## Telemetria

O Agno registra qual modelo um agente usou para que possamos priorizar atualizações para os provedores mais populares. Você pode desativar isso definindo `AGNO_TELEMETRY=false` no seu ambiente.

<p align="left">
  <a href="#top">⬆️ Voltar ao topo</a>
</p>