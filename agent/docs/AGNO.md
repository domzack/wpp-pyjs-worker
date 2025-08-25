# Agno — Documentação Consolidada

_Gerado de: C:\mygits\wpp\agent\docs\agno_

---

## agents__agent-state.md


```
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

---

## agents__audio-agent.md


```
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

---

## agents__context-agent.md


```
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

---

## agents__eval-agent.md


```
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

---

## agents__finance-agent.md

This example shows how to create a sophisticated financial analyst that provides
comprehensive market insights using real-time data. The agent combines stock market data,
analyst recommendations, company information, and latest news to deliver professional-grade
financial analysis.
Example prompts to try:

* “What’s the latest news and financial performance of Apple (AAPL)?”
* “Give me a detailed analysis of Tesla’s (TSLA) current market position”
* “How are Microsoft’s (MSFT) financials looking? Include analyst recommendations”
* “Analyze NVIDIA’s (NVDA) stock performance and future outlook”
* “What’s the market saying about Amazon’s (AMZN) latest quarter?”

## [​](#code) Code

finance\_agent.py

```
from textwrap import dedent

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.yfinance import YFinanceTools

finance_agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    tools=[
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            stock_fundamentals=True,
            historical_prices=True,
            company_info=True,
            company_news=True,
        )
    ],
    instructions=dedent("""\
        You are a seasoned Wall Street analyst with deep expertise in market analysis! 📊

        Follow these steps for comprehensive financial analysis:
        1. Market Overview
           - Latest stock price
           - 52-week high and low
        2. Financial Deep Dive
           - Key metrics (P/E, Market Cap, EPS)
        3. Professional Insights
           - Analyst recommendations breakdown
           - Recent rating changes

        4. Market Context
           - Industry trends and positioning
           - Competitive analysis
           - Market sentiment indicators

        Your reporting style:
        - Begin with an executive summary
        - Use tables for data presentation
        - Include clear section headers
        - Add emoji indicators for trends (📈 📉)
        - Highlight key insights with bullet points
        - Compare metrics to industry averages
        - Include technical term explanations
        - End with a forward-looking analysis

        Risk Disclosure:
        - Always highlight potential risk factors
        - Note market uncertainties
        - Mention relevant regulatory concerns
    """),
    add_datetime_to_instructions=True,
    show_tool_calls=True,
    markdown=True,
)

# Example usage with detailed market analysis request
finance_agent.print_response(
    "What's the latest news and financial performance of Apple (AAPL)?", stream=True
)

# Semiconductor market analysis example
finance_agent.print_response(
    dedent("""\
    Analyze the semiconductor market performance focusing on:
    - NVIDIA (NVDA)
    - AMD (AMD)
    - Intel (INTC)
    - Taiwan Semiconductor (TSM)
    Compare their market positions, growth metrics, and future outlook."""),
    stream=True,
)

# Automotive market analysis example
finance_agent.print_response(
    dedent("""\
    Evaluate the automotive industry's current state:
    - Tesla (TSLA)
    - Ford (F)
    - General Motors (GM)
    - Toyota (TM)
    Include EV transition progress and traditional auto metrics."""),
    stream=True,
)

# More example prompts to explore:
"""
Advanced analysis queries:
1. "Compare Tesla's valuation metrics with traditional automakers"
2. "Analyze the impact of recent product launches on AMD's stock performance"
3. "How do Meta's financial metrics compare to its social media peers?"
4. "Evaluate Netflix's subscriber growth impact on financial metrics"
5. "Break down Amazon's revenue streams and segment performance"

Industry-specific analyses:
Semiconductor Market:
1. "How is the chip shortage affecting TSMC's market position?"
2. "Compare NVIDIA's AI chip revenue growth with competitors"
3. "Analyze Intel's foundry strategy impact on stock performance"
4. "Evaluate semiconductor equipment makers like ASML and Applied Materials"

Automotive Industry:
1. "Compare EV manufacturers' production metrics and margins"
2. "Analyze traditional automakers' EV transition progress"
3. "How are rising interest rates impacting auto sales and stock performance?"
4. "Compare Tesla's profitability metrics with traditional auto manufacturers"
"""
```

## [​](#usage) Usage

1

Create a virtual environment

Open the `Terminal` and create a python virtual environment.

```
python3 -m venv .venv
source .venv/bin/activate
```

2

Install libraries

```
pip install openai yfinance agno
```

3

Set environment variables

```
export OPENAI_API_KEY=****
```

4

Run the agent

```
python finance_agent.py
```

---

## agents__image-agent.md

```
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

---

## agents__memory-agent.md


```
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

---

## agents__multimodal-agent.md


```
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



---

## agents__observability-agent.md


```
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



---

## agents__rag-agent.md


```
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



---

## agents__reasoning-agent.md


```
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



---

## agents__storage-agent.md


```
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



---

## agents__testing-agent.md


```
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



---

## agents__tools-agent.md


```
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



---

## agents__tweet-analysis-agent.md

Key capabilities:

* Real-time tweet analysis and sentiment classification
* Engagement metrics analysis (likes, retweets, replies)
* Brand health monitoring and competitive intelligence
* Strategic recommendations and response strategies

## [​](#code) Code

social\_media\_agent.py

```
from textwrap import dedent

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.x import XTools

social_media_agent = Agent(
    name="Social Media Analyst",
    model=OpenAIChat(id="gpt-4o"),
    tools=[
        XTools(
            include_post_metrics=True,
            wait_on_rate_limit=True,
        )
    ],
    instructions=dedent("""\
        You are a senior Brand Intelligence Analyst specializing in social media 
        listening on X (Twitter). 
        Your mission: Transform raw tweet content and engagement metrics into 
        executive-ready intelligence reports.

        Core Analysis Steps:
        1. Data Collection
           - Retrieve tweets using X tools
           - Analyze text content and engagement metrics
           - Focus on likes, retweets, replies, and reach

        2. Sentiment Classification
           - Classify each tweet: Positive/Negative/Neutral/Mixed
           - Identify reasoning (feature praise, bug complaints, etc.)
           - Weight by engagement volume and author influence

        3. Pattern Detection
           - Viral advocacy (high likes & retweets, low replies)
           - Controversy signals (low likes, high replies)
           - Influencer impact and verified account activity

        4. Thematic Analysis
           - Extract recurring keywords and themes
           - Identify feature feedback and pain points
           - Track competitor mentions and comparisons
           - Spot emerging use cases

        Report Format:
        - Executive summary with brand health score (1-10)
        - Key themes with representative quotes
        - Risk analysis and opportunity identification
        - Strategic recommendations (immediate/short-term/long-term)
        - Response playbook for high-impact posts

        Guidelines:
        - Be objective and evidence-backed
        - Focus on actionable insights
        - Highlight urgent issues requiring attention
        - Provide solution-oriented recommendations"""),
    markdown=True,
    show_tool_calls=True,
)

social_media_agent.print_response(
    "Analyze the sentiment of Agno and AgnoAGI on X (Twitter) for past 10 tweets"
)
```

Check out the detailed [Social Media Agent](https://github.com/agno-agi/agno/blob/main/cookbook/examples/agents/social_media_agent.py).

More prompts to try:

* “Analyze sentiment around our brand on X for the past 10 tweets”
* “Monitor competitor mentions and compare sentiment vs our brand”
* “Generate a brand health report from recent social media activity”
* “Identify trending topics and user sentiment about our product”
* “Create a social media intelligence report for executive review”

## [​](#usage) Usage

1

Create a virtual environment

Open the `Terminal` and create a python virtual environment.

```
python3 -m venv .venv
source .venv/bin/activate
```

2

Set your API key

```
export OPENAI_API_KEY=****
```

3

Set your X credentials

```
export X_CONSUMER_KEY=****
export X_CONSUMER_SECRET=****
export X_ACCESS_TOKEN=****
export X_ACCESS_TOKEN_SECRET=****
export X_BEARER_TOKEN=****
```

4

Install libraries

```
pip install openai tweepy agno
```

5

Run the agent

```
python social_media_agent.py
```

---

## agents__vector-db-agent.md


```
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



---

## agents__video-agent.md


```
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



---

## AGNO_DOCS_SUMMARY.md

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

---

## applications__agent-api.md


```
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



---

## applications__agent-cli.md


```
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



---

## applications__fastapi-server.md


```
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



---

## applications__streamlit-dashboard.md


```
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



---

## evals__eval-memory.md


```
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



---

## evals__eval-performance.md


```
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



---

## evals__eval-storage.md


```
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



---

## evals__eval-tools.md


```
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



---

## getting-started__agent-context.md

This example shows how to inject external dependencies into an agent. The context is evaluated when the agent is run, acting like dependency injection for Agents.
Example prompts to try:

* “Summarize the top stories on HackerNews”
* “What are the trending tech discussions right now?”
* “Analyze the current top stories and identify trends”
* “What’s the most upvoted story today?”

## [​](#code) Code

agent\_context.py

```
import json
from textwrap import dedent

import httpx
from agno.agent import Agent
from agno.models.openai import OpenAIChat


def get_top_hackernews_stories(num_stories: int = 5) -> str:
    """Fetch and return the top stories from HackerNews.

    Args:
        num_stories: Number of top stories to retrieve (default: 5)
    Returns:
        JSON string containing story details (title, url, score, etc.)
    """
    # Get top stories
    stories = [
        {
            k: v
            for k, v in httpx.get(
                f"https://hacker-news.firebaseio.com/v0/item/{id}.json"
            )
            .json()
            .items()
            if k != "kids"  # Exclude discussion threads
        }
        for id in httpx.get(
            "https://hacker-news.firebaseio.com/v0/topstories.json"
        ).json()[:num_stories]
    ]
    return json.dumps(stories, indent=4)


# Create a Context-Aware Agent that can access real-time HackerNews data
agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    # Each function in the context is evaluated when the agent is run,
    # think of it as dependency injection for Agents
    context={"top_hackernews_stories": get_top_hackernews_stories},
    # add_context will automatically add the context to the user message
    # add_context=True,
    # Alternatively, you can manually add the context to the instructions
    instructions=dedent("""\
        You are an insightful tech trend observer! 📰

        Here are the top stories on HackerNews:
        {top_hackernews_stories}\
    """),
    markdown=True,
)

# Example usage
agent.print_response(
    "Summarize the top stories on HackerNews and identify any interesting trends.",
    stream=True,
)
```

## [​](#usage) Usage

1

Create a virtual environment

Open the `Terminal` and create a python virtual environment.

```
python3 -m venv .venv
source .venv/bin/activate
```

2

Install libraries

```
pip install openai httpx agno
```

3

Run the agent

```
python agent_context.py
```

---

## getting-started__agent-session.md

This example shows how to create an agent with persistent memory stored in a SQLite database. We set the session\_id on the agent when resuming the conversation, this way the previous chat history is preserved.
Key features:

* Stores conversation history in a SQLite database
* Continues conversations across multiple sessions
* References previous context in responses

## [​](#code) Code

agent\_session.py

```
import json
from typing import Optional

import typer
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.storage.sqlite import SqliteStorage
from rich.console import Console
from rich.json import JSON
from rich.panel import Panel
from rich.prompt import Prompt
from rich import print

console = Console()


def create_agent(user: str = "user"):
    session_id: Optional[str] = None

    # Ask if user wants to start new session or continue existing one
    new = typer.confirm("Do you want to start a new session?")

    # Get existing session if user doesn't want a new one
    agent_storage = SqliteStorage(
        table_name="agent_sessions", db_file="tmp/agents.db"
    )

    if not new:
        existing_sessions = agent_storage.get_all_session_ids(user)
        if len(existing_sessions) > 0:
            session_id = existing_sessions[0]

    agent = Agent(
        user_id=user,
        # Set the session_id on the agent to resume the conversation
        session_id=session_id,
        model=OpenAIChat(id="gpt-4o"),
        storage=agent_storage,
        # Add chat history to messages
        add_history_to_messages=True,
        num_history_responses=3,
        markdown=True,
    )

    if session_id is None:
        session_id = agent.session_id
        if session_id is not None:
            print(f"Started Session: {session_id}\n")
        else:
            print("Started Session\n")
    else:
        print(f"Continuing Session: {session_id}\n")

    return agent


def print_messages(agent):
    """Print the current chat history in a formatted panel"""
    console.print(
        Panel(
            JSON(
                json.dumps(
                    [
                        m.model_dump(include={"role", "content"})
                        for m in agent.memory.messages
                    ]
                ),
                indent=4,
            ),
            title=f"Chat History for session_id: {agent.session_id}",
            expand=True,
        )
    )


def main(user: str = "user"):
    agent = create_agent(user)

    print("Chat with an OpenAI agent!")
    exit_on = ["exit", "quit", "bye"]
    while True:
        message = Prompt.ask(f"[bold] :sunglasses: {user} [/bold]")
        if message in exit_on:
            break

        agent.print_response(message=message, stream=True, markdown=True)
        print_messages(agent)


if __name__ == "__main__":
    typer.run(main)
```

## [​](#usage) Usage

1

Create a virtual environment

Open the `Terminal` and create a python virtual environment.

```
python3 -m venv .venv
source .venv/bin/activate
```

2

Install libraries

```
pip install openai sqlalchemy agno
```

3

Run the agent

```
python agent_session.py
```

---

## getting-started__agent-state.md

This example shows how to create an agent that maintains state across interactions. It demonstrates a simple counter mechanism, but this pattern can be extended to more complex state management like maintaining conversation context, user preferences, or tracking multi-step processes.
Example prompts to try:

* “Increment the counter 3 times and tell me the final count”
* “What’s our current count? Add 2 more to it”
* “Let’s increment the counter 5 times, but tell me each step”
* “Add 4 to our count and remind me where we started”
* “Increase the counter twice and summarize our journey”

## [​](#code) Code

agent\_state.py

```
from textwrap import dedent

from agno.agent import Agent
from agno.models.openai import OpenAIChat


# Define a tool that increments our counter and returns the new value
def increment_counter(agent: Agent) -> str:
    """Increment the session counter and return the new value."""
    agent.session_state["count"] += 1
    return f"The count is now {agent.session_state['count']}"


# Create a State Manager Agent that maintains state
agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    # Initialize the session state with a counter starting at 0
    session_state={"count": 0},
    tools=[increment_counter],
    # You can use variables from the session state in the instructions
    instructions=dedent("""\
        You are the State Manager, an enthusiastic guide to state management! 🔄
        Your job is to help users understand state management through a simple counter example.

        Follow these guidelines for every interaction:
        1. Always acknowledge the current state (count) when relevant
        2. Use the increment_counter tool to modify the state
        3. Explain state changes in a clear and engaging way

        Structure your responses like this:
        - Current state status
        - State transformation actions
        - Final state and observations

        Starting state (count) is: {count}\
    """),
    show_tool_calls=True,
    markdown=True,
)

# Example usage
agent.print_response(
    "Let's increment the counter 3 times and observe the state changes!",
    stream=True,
)

# More example prompts to try:
"""
Try these engaging state management scenarios:
1. "Update our state 4 times and track the changes"
2. "Modify the counter twice and explain the state transitions"
3. "Increment 3 times and show how state persists"
4. "Let's perform 5 state updates with observations"
5. "Add 3 to our count and explain the state management concept"
"""

print(f"Final session state: {agent.session_state}")
```

## [​](#usage) Usage

1

Create a virtual environment

Open the `Terminal` and create a python virtual environment.

```
python3 -m venv .venv
source .venv/bin/activate
```

2

Install libraries

```
pip install openai agno
```

3

Run the agent

```
python agent_state.py
```

---

## getting-started__agent-team.md

This example shows how to create a powerful team of AI agents working together to provide comprehensive financial analysis and news reporting. The team consists of:

1. Web Agent: Searches and analyzes latest news
2. Finance Agent: Analyzes financial data and market trends
3. Lead Editor: Coordinates and combines insights from both agents

Example prompts to try:

* “What’s the latest news and financial performance of Apple (AAPL)?”
* “Analyze the impact of AI developments on NVIDIA’s stock (NVDA)”
* “How are EV manufacturers performing? Focus on Tesla (TSLA) and Rivian (RIVN)”
* “What’s the market outlook for semiconductor companies like AMD and Intel?”
* “Summarize recent developments and stock performance of Microsoft (MSFT)“

## [​](#code) Code

agent\_team.py

```
from textwrap import dedent

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools

web_agent = Agent(
    name="Web Agent",
    role="Search the web for information",
    model=OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGoTools()],
    instructions=dedent("""\
        You are an experienced web researcher and news analyst! 🔍

        Follow these steps when searching for information:
        1. Start with the most recent and relevant sources
        2. Cross-reference information from multiple sources
        3. Prioritize reputable news outlets and official sources
        4. Always cite your sources with links
        5. Focus on market-moving news and significant developments

        Your style guide:
        - Present information in a clear, journalistic style
        - Use bullet points for key takeaways
        - Include relevant quotes when available
        - Specify the date and time for each piece of news
        - Highlight market sentiment and industry trends
        - End with a brief analysis of the overall narrative
        - Pay special attention to regulatory news, earnings reports, and strategic announcements\
    """),
    show_tool_calls=True,
    markdown=True,
)

finance_agent = Agent(
    name="Finance Agent",
    role="Get financial data",
    model=OpenAIChat(id="gpt-4o"),
    tools=[
        YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True)
    ],
    instructions=dedent("""\
        You are a skilled financial analyst with expertise in market data! 📊

        Follow these steps when analyzing financial data:
        1. Start with the latest stock price, trading volume, and daily range
        2. Present detailed analyst recommendations and consensus target prices
        3. Include key metrics: P/E ratio, market cap, 52-week range
        4. Analyze trading patterns and volume trends
        5. Compare performance against relevant sector indices

        Your style guide:
        - Use tables for structured data presentation
        - Include clear headers for each data section
        - Add brief explanations for technical terms
        - Highlight notable changes with emojis (📈 📉)
        - Use bullet points for quick insights
        - Compare current values with historical averages
        - End with a data-driven financial outlook\
    """),
    show_tool_calls=True,
    markdown=True,
)

agent_team = Agent(
    team=[web_agent, finance_agent],
    model=OpenAIChat(id="gpt-4o"),
    instructions=dedent("""\
        You are the lead editor of a prestigious financial news desk! 📰

        Your role:
        1. Coordinate between the web researcher and financial analyst
        2. Combine their findings into a compelling narrative
        3. Ensure all information is properly sourced and verified
        4. Present a balanced view of both news and data
        5. Highlight key risks and opportunities

        Your style guide:
        - Start with an attention-grabbing headline
        - Begin with a powerful executive summary
        - Present financial data first, followed by news context
        - Use clear section breaks between different types of information
        - Include relevant charts or tables when available
        - Add 'Market Sentiment' section with current mood
        - Include a 'Key Takeaways' section at the end
        - End with 'Risk Factors' when appropriate
        - Sign off with 'Market Watch Team' and the current date\
    """),
    add_datetime_to_instructions=True,
    show_tool_calls=True,
    markdown=True,
)

# Example usage with diverse queries
agent_team.print_response(
    "Summarize analyst recommendations and share the latest news for NVDA", stream=True
)
agent_team.print_response(
    "What's the market outlook and financial performance of AI semiconductor companies?",
    stream=True,
)
agent_team.print_response(
    "Analyze recent developments and financial performance of TSLA", stream=True
)

# More example prompts to try:
"""
Advanced queries to explore:
1. "Compare the financial performance and recent news of major cloud providers (AMZN, MSFT, GOOGL)"
2. "What's the impact of recent Fed decisions on banking stocks? Focus on JPM and BAC"
3. "Analyze the gaming industry outlook through ATVI, EA, and TTWO performance"
4. "How are social media companies performing? Compare META and SNAP"
5. "What's the latest on AI chip manufacturers and their market position?"
"""
```

## [​](#usage) Usage

1

Create a virtual environment

Open the `Terminal` and create a python virtual environment.

```
python3 -m venv .venv
source .venv/bin/activate
```

2

Install libraries

```
pip install openai duckduckgo-search yfinance agno
```

3

Run the agent

```
python agent_team.py
```

---

## getting-started__agent-with-knowledge.md

This example shows how to create an AI cooking assistant that combines knowledge from a curated recipe database with web searching capabilities. The agent uses a PDF knowledge base of authentic Thai recipes and can supplement this information with web searches when needed.
Example prompts to try:

* “How do I make authentic Pad Thai?”
* “What’s the difference between red and green curry?”
* “Can you explain what galangal is and possible substitutes?”
* “Tell me about the history of Tom Yum soup”
* “What are essential ingredients for a Thai pantry?”
* “How do I make Thai basil chicken (Pad Kra Pao)?”

## [​](#code) Code

agent\_with\_knowledge.py

```
from textwrap import dedent

from agno.agent import Agent
from agno.embedder.openai import OpenAIEmbedder
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.vectordb.lancedb import LanceDb, SearchType

# Create a Recipe Expert Agent with knowledge of Thai recipes
agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    instructions=dedent("""\
        You are a passionate and knowledgeable Thai cuisine expert! 🧑‍🍳
        Think of yourself as a combination of a warm, encouraging cooking instructor,
        a Thai food historian, and a cultural ambassador.

        Follow these steps when answering questions:
        1. First, search the knowledge base for authentic Thai recipes and cooking information
        2. If the information in the knowledge base is incomplete OR if the user asks a question better suited for the web, search the web to fill in gaps
        3. If you find the information in the knowledge base, no need to search the web
        4. Always prioritize knowledge base information over web results for authenticity
        5. If needed, supplement with web searches for:
            - Modern adaptations or ingredient substitutions
            - Cultural context and historical background
            - Additional cooking tips and troubleshooting

        Communication style:
        1. Start each response with a relevant cooking emoji
        2. Structure your responses clearly:
            - Brief introduction or context
            - Main content (recipe, explanation, or history)
            - Pro tips or cultural insights
            - Encouraging conclusion
        3. For recipes, include:
            - List of ingredients with possible substitutions
            - Clear, numbered cooking steps
            - Tips for success and common pitfalls
        4. Use friendly, encouraging language

        Special features:
        - Explain unfamiliar Thai ingredients and suggest alternatives
        - Share relevant cultural context and traditions
        - Provide tips for adapting recipes to different dietary needs
        - Include serving suggestions and accompaniments

        End each response with an uplifting sign-off like:
        - 'Happy cooking! ขอให้อร่อย (Enjoy your meal)!'
        - 'May your Thai cooking adventure bring joy!'
        - 'Enjoy your homemade Thai feast!'

        Remember:
        - Always verify recipe authenticity with the knowledge base
        - Clearly indicate when information comes from web sources
        - Be encouraging and supportive of home cooks at all skill levels\
    """),
    knowledge=PDFUrlKnowledgeBase(
        urls=["https://agno-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
        vector_db=LanceDb(
            uri="tmp/lancedb",
            table_name="recipe_knowledge",
            search_type=SearchType.hybrid,
            embedder=OpenAIEmbedder(id="text-embedding-3-small"),
        ),
    ),
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True,
    add_references=True,
)

# Comment out after the knowledge base is loaded
if agent.knowledge is not None:
    agent.knowledge.load()

agent.print_response(
    "How do I make chicken and galangal in coconut milk soup", stream=True
)
agent.print_response("What is the history of Thai curry?", stream=True)
agent.print_response("What ingredients do I need for Pad Thai?", stream=True)
```

## [​](#usage) Usage

1

Create a virtual environment

Open the `Terminal` and create a python virtual environment.

```
python3 -m venv .venv
source .venv/bin/activate
```

2

Install libraries

```
pip install openai lancedb tantivy pypdf duckduckgo-search agno
```

3

Run the agent

```
python agent_with_knowledge.py
```

---

## getting-started__agent-with-storage.md

This example shows how to create an AI cooking assistant that combines knowledge from a curated recipe database with web searching capabilities and persistent storage. The agent uses a PDF knowledge base of authentic Thai recipes and can supplement this information with web searches when needed.
Example prompts to try:

* “How do I make authentic Pad Thai?”
* “What’s the difference between red and green curry?”
* “Can you explain what galangal is and possible substitutes?”
* “Tell me about the history of Tom Yum soup”
* “What are essential ingredients for a Thai pantry?”
* “How do I make Thai basil chicken (Pad Kra Pao)?”

## [​](#code) Code

agent\_with\_storage.py

```
from textwrap import dedent
from typing import List, Optional

import typer
from agno.agent import Agent
from agno.embedder.openai import OpenAIEmbedder
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.models.openai import OpenAIChat
from agno.storage.sqlite import SqliteStorage
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.vectordb.lancedb import LanceDb, SearchType
from rich import print

agent_knowledge = PDFUrlKnowledgeBase(
    urls=["https://agno-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
    vector_db=LanceDb(
        uri="tmp/lancedb",
        table_name="recipe_knowledge",
        search_type=SearchType.hybrid,
        embedder=OpenAIEmbedder(id="text-embedding-3-small"),
    ),
)

agent_storage = SqliteStorage(table_name="recipe_agent", db_file="tmp/agents.db")


def recipe_agent(user: str = "user"):
    session_id: Optional[str] = None

    # Ask the user if they want to start a new session or continue an existing one
    new = typer.confirm("Do you want to start a new session?")

    if not new:
        existing_sessions: List[str] = agent_storage.get_all_session_ids(user)
        if len(existing_sessions) > 0:
            session_id = existing_sessions[0]

    agent = Agent(
        user_id=user,
        session_id=session_id,
        model=OpenAIChat(id="gpt-4o"),
        instructions=dedent("""\
            You are a passionate and knowledgeable Thai cuisine expert! 🧑‍🍳
            Think of yourself as a combination of a warm, encouraging cooking instructor,
            a Thai food historian, and a cultural ambassador.

            Follow these steps when answering questions:
            1. First, search the knowledge base for authentic Thai recipes and cooking information
            2. If the information in the knowledge base is incomplete OR if the user asks a question better suited for the web, search the web to fill in gaps
            3. If you find the information in the knowledge base, no need to search the web
            4. Always prioritize knowledge base information over web results for authenticity
            5. If needed, supplement with web searches for:
               - Modern adaptations or ingredient substitutions
               - Cultural context and historical background
               - Additional cooking tips and troubleshooting

            Communication style:
            1. Start each response with a relevant cooking emoji
            2. Structure your responses clearly:
               - Brief introduction or context
               - Main content (recipe, explanation, or history)
               - Pro tips ou cultural insights
               - Encouraging conclusion
            3. For recipes, include:
               - List of ingredients with possible substitutions
               - Clear, numbered cooking steps
               - Tips for success and common pitfalls
            4. Use friendly, encouraging language

            Special features:
            - Explain unfamiliar Thai ingredients and suggest alternatives
            - Share relevant cultural context and traditions
            - Provide tips for adapting recipes to different dietary needs
            - Include serving suggestions and accompaniments

            End each response with an uplifting sign-off like:
            - 'Happy cooking! ขอให้อร่อย (Enjoy your meal)!'
            - 'May your Thai cooking adventure bring joy!'
            - 'Enjoy your homemade Thai feast!'

            Remember:
            - Always verify recipe authenticity with the knowledge base
            - Clearly indicate when information comes from web sources
            - Be encouraging and supportive of home cooks at all skill levels\
        """),
        storage=agent_storage,
        knowledge=agent_knowledge,
        tools=[DuckDuckGoTools()],
        # Show tool calls in the response
        show_tool_calls=True,
        # To provide the agent with the chat history
        # We can either:
        # 1. Provide the agent with a tool to read the chat history
        # 2. Automatically add the chat history to the messages sent to the model
        #
        # 1. Provide the agent with a tool to read the chat history
        read_chat_history=True,
        # 2. Automatically add the chat history to the messages sent to the model
        # add_history_to_messages=True,
        # Number of historical responses to add to the messages.
        # num_history_responses=3,
        markdown=True,
    )

    print("You are about to chat with an agent!")
    if session_id is None:
        session_id = agent.session_id
        if session_id is not None:
            print(f"Started Session: {session_id}\n")
        else:
            print("Started Session\n")
    else:
        print(f"Continuing Session: {session_id}\n")

    # Runs the agent as a command line application
    agent.cli_app(markdown=True)


if __name__ == "__main__":
    # Comment out after the knowledge base is loaded
    if agent_knowledge is not None:
        agent_knowledge.load()

    typer.run(recipe_agent)
```

## [​](#usage) Usage

1

Create a virtual environment

Open the `Terminal` and create a python virtual environment.

```
python3 -m venv .venv
source .venv/bin/activate
```

2

Install libraries

```
pip install openai lancedb tantivy pypdf duckduckgo-search sqlalchemy agno
```

3

Run the agent

```
python agent_with_storage.py
```

---

## getting-started__agent-with-tools.md

This example shows how to create an AI news reporter agent that can search the web for real-time news and present them with a distinctive NYC personality. The agent combines web searching capabilities with engaging storytelling to deliver news in an entertaining way.
Example prompts to try:

* “What’s the latest headline from Wall Street?”
* “Tell me about any breaking news in Central Park”
* “What’s happening at Yankees Stadium today?”
* “Give me updates on the newest Broadway shows”
* “What’s the buzz about the latest NYC restaurant opening?”

## [​](#code) Code

agent\_with\_tools.py

```
from textwrap import dedent

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools

# Create a News Reporter Agent with a fun personality
agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    instructions=dedent("""\
        You are an enthusiastic news reporter with a flair for storytelling! 🗽
        Think of yourself as a mix between a witty comedian and a sharp journalist.

        Follow these guidelines for every report:
        1. Start with an attention-grabbing headline using relevant emoji
        2. Use the search tool to find current, accurate information
        3. Present news with authentic NYC enthusiasm and local flavor
        4. Structure your reports in clear sections:
        - Catchy headline
        - Brief summary of the news
        - Key details and quotes
        - Local impact or context
        5. Keep responses concise but informative (2-3 paragraphs max)
        6. Include NYC-style commentary and local references
        7. End with a signature sign-off phrase

        Sign-off examples:
        - 'Back to you in the studio, folks!'
        - 'Reporting live from the city that never sleeps!'
        - 'This is [Your Name], live from the heart of Manhattan!'

        Remember: Always verify facts through web searches and maintain that authentic NYC energy!\
    """),
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True,
)

# Example usage
agent.print_response(
    "Tell me about a breaking news story happening in Times Square.", stream=True
)

# More example prompts to try:
"""
Try these engaging news queries:
1. "What's the latest development in NYC's tech scene?"
2. "Tell me about any upcoming events at Madison Square Garden"
3. "What's the weather impact on NYC today?"
4. "Any updates on the NYC subway system?"
5. "What's the hottest food trend in Manhattan right now?"
"""
```

## [​](#usage) Usage

1

Create a virtual environment

Open the `Terminal` and create a python virtual environment.

```
python3 -m venv .venv
source .venv/bin/activate
```

2

Install libraries

```
pip install openai duckduckgo-search agno
```

3

Run the agent

```
python agent_with_tools.py
```

---

## getting-started__audio-agent.md

This example shows how to create an AI agent that can process audio input and generate audio responses. You can use this agent for various voice-based interactions, from analyzing speech content to generating natural-sounding responses.
Example audio interactions to try:

* Upload a recording of a conversation for analysis
* Have the agent respond to questions with voice output
* Process different languages and accents
* Analyze tone and emotion in speech

## [​](#code) Code

audio\_agent.py

```
from textwrap import dedent

import requests
from agno.agent import Agent
from agno.media import Audio
from agno.models.openai import OpenAIChat
from agno.utils.audio import write_audio_to_file

# Create an AI Voice Interaction Agent
agent = Agent(
    model=OpenAIChat(
        id="gpt-4o-audio-preview",
        modalities=["text", "audio"],
        audio={"voice": "alloy", "format": "wav"},
    ),
    description=dedent("""\
        You are an expert in audio processing and voice interaction, capable of understanding
        and analyzing spoken content while providing natural, engaging voice responses.
        You excel at comprehending context, emotion, and nuance in speech.\
    """),
    instructions=dedent("""\
        As a voice interaction specialist, follow these guidelines:
        1. Listen carefully to audio input to understand both content and context
        2. Provide clear, concise responses that address the main points
        3. When generating voice responses, maintain a natural, conversational tone
        4. Consider the speaker's tone and emotion in your analysis
        5. If the audio is unclear, ask for clarification

        Focus on creating engaging and helpful voice interactions!\
    """),
)

# Fetch the audio file and convert it to a base64 encoded string
url = "https://openaiassets.blob.core.windows.net/$web/API/docs/audio/alloy.wav"
response = requests.get(url)
response.raise_for_status()

# Process the audio and get a response
agent.run(
    "What's in this recording? Please analyze the content and tone.",
    audio=[Audio(content=response.content, format="wav")],
)

# Save the audio response if available
if agent.run_response.response_audio is not None:
    write_audio_to_file(
        audio=agent.run_response.response_audio.content, filename="tmp/response.wav"
    )

# More example interactions to try:
"""
Try these voice interaction scenarios:
1. "Can you summarize the main points discussed in this recording?"
2. "What emotions or tone do you detect in the speaker's voice?"
3. "Please provide a detailed analysis of the speech patterns and clarity"
4. "Can you identify any background noises or audio quality issues?"
5. "What is the overall context and purpose of this recording?"

Note: You can use your own audio files by converting them to base64 format.
Example for using your own audio file:

with open('your_audio.wav', 'rb') as audio_file:
    audio_data = audio_file.read()
    agent.run("Analyze this audio", audio=[Audio(content=audio_data, format="wav")])
"""
```

## [​](#usage) Usage

1

Create a virtual environment

Open the `Terminal` and create a python virtual environment.

```
python3 -m venv .venv
source .venv/bin/activate
```

2

Install libraries

```
pip install openai requests agno
```

3

Run the agent

```
python audio_agent.py
```

---

## getting-started__basic-agent.md

This example shows how to create a basic AI agent with a distinct personality. We’ll create a fun news reporter that combines NYC attitude with creative storytelling. This shows how personality and style instructions can shape an agent’s responses.
Example prompts to try:

* “What’s the latest scoop from Central Park?”
* “Tell me about a breaking story from Wall Street”
* “What’s happening at the Yankees game right now?”
* “Give me the buzz about a new Broadway show”

## [​](#code) Code

basic\_agent.py

```
from textwrap import dedent

from agno.agent import Agent
from agno.models.openai import OpenAIChat

# Create our News Reporter with a fun personality
agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    instructions=dedent("""\
        You are an enthusiastic news reporter with a flair for storytelling! 🗽
        Think of yourself as a mix between a witty comedian and a sharp journalist.

        Your style guide:
        - Start with an attention-grabbing headline using emoji
        - Share news with enthusiasm and NYC attitude
        - Keep your responses concise but entertaining
        - Throw in local references and NYC slang when appropriate
        - End with a catchy sign-off like 'Back to you in the studio!' or 'Reporting live from the Big Apple!'

        Remember to verify all facts while keeping that NYC energy high!\
    """),
    markdown=True,
)

# Example usage
agent.print_response(
    "Tell me about a breaking news story happening in Times Square.", stream=True
)

# More example prompts to try:
"""
Try these fun scenarios:
1. "What's the latest food trend taking over Brooklyn?"
2. "Tell me about a peculiar incident on the subway today"
3. "What's the scoop on the newest rooftop garden in Manhattan?"
4. "Report on an unusual traffic jam caused by escaped zoo animals"
5. "Cover a flash mob wedding proposal at Grand Central"
"""
```

## [​](#usage) Usage

1

Create a virtual environment

Open the `Terminal` and create a python virtual environment.

```
python3 -m venv .venv
source .venv/bin/activate
```

2

Install libraries

```
pip install openai agno
```

3

Run the agent

```
python basic_agent.py
```

---

## getting-started__custom-tools.md

This example shows how to create and use your own custom tool with Agno.
You can replace the Hacker News functionality with any API or service you want!
Some ideas for your own tools:

* Weather data fetcher
* Stock price analyzer
* Personal calendar integration
* Custom database queries
* Local file operations

## [​](#code) Code

custom\_tools.py

```
import json
from textwrap import dedent

import httpx
from agno.agent import Agent
from agno.models.openai import OpenAIChat


def get_top_hackernews_stories(num_stories: int = 10) -> str:
    """Use this function to get top stories from Hacker News.

    Args:
        num_stories (int): Number of stories to return. Defaults to 10.

    Returns:
        str: JSON string of top stories.
    """

    # Fetch top story IDs
    response = httpx.get("https://hacker-news.firebaseio.com/v0/topstories.json")
    story_ids = response.json()

    # Fetch story details
    stories = []
    for story_id in story_ids[:num_stories]:
        story_response = httpx.get(
            f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
        )
        story = story_response.json()
        if "text" in story:
            story.pop("text", None)
        stories.append(story)
    return json.dumps(stories)


# Create a Tech News Reporter Agent with a Silicon Valley personality
agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    instructions=dedent("""\
        You are a tech-savvy Hacker News reporter with a passion for all things technology! 🤖
        Think of yourself as a mix between a Silicon Valley insider and a tech journalist.

        Your style guide:
        - Start with an attention-grabbing tech headline using emoji
        - Present Hacker News stories with enthusiasm and tech-forward attitude
        - Keep your responses concise but informative
        - Use tech industry references and startup lingo when appropriate
        - End with a catchy tech-themed sign-off like 'Back to the terminal!' or 'Pushing to production!'

        Remember to analyze the HN stories thoroughly while keeping the tech enthusiasm high!\
    """),
    tools=[get_top_hackernews_stories],
    show_tool_calls=True,
    markdown=True,
)

# Example questions to try:
# - "What are the trending tech discussions on HN right now?"
# - "Summarize the top 5 stories on Hacker News"
# - "What's the most upvoted story today?"
agent.print_response("Summarize the top 5 stories on hackernews?", stream=True)
```

## [​](#usage) Usage

1

Create a virtual environment

Open the `Terminal` and create a python virtual environment.

```
python3 -m venv .venv
source .venv/bin/activate
```

2

Install libraries

```
pip install openai httpx agno
```

3

Run the agent

```
python custom_tools.py
```

---

## getting-started__human-in-the-loop.md

This example shows how to implement human validation in your agent workflows. It demonstrates:

* Pre-execution validation
* Post-execution review
* Interactive feedback loops
* Quality control checkpoints

Example scenarios:

* Content moderation
* Critical decision approval
* Output quality validation
* Safety checks
* Expert review processes

## [​](#code) Code

human\_in\_the\_loop.py

```
import json
from textwrap import dedent
from typing import Iterator

import httpx
from agno.agent import Agent
from agno.exceptions import StopAgentRun
from agno.tools import FunctionCall, tool
from rich.console import Console
from rich.pretty import pprint
from rich.prompt import Prompt

# This is the console instance used by the print_response method
# We can use this to stop and restart the live display and ask for user confirmation
console = Console()


def pre_hook(fc: FunctionCall):
    # Get the live display instance from the console
    live = console._live

    # Stop the live display temporarily so we can ask for user confirmation
    live.stop()  # type: ignore

    # Ask for confirmation
    console.print(f"\nAbout to run [bold blue]{fc.function.name}[/]")
    message = (
        Prompt.ask("Do you want to continue?", choices=["y", "n"], default="y")
        .strip()
        .lower()
    )

    # Restart the live display
    live.start()  # type: ignore

    # If the user does not want to continue, raise a StopExecution exception
    if message != "y":
        raise StopAgentRun(
            "Tool call cancelled by user",
            agent_message="Stopping execution as permission was not granted.",
        )


@tool(pre_hook=pre_hook)
def get_top_hackernews_stories(num_stories: int) -> Iterator[str]:
    """Fetch top stories from Hacker News after user confirmation.

    Args:
        num_stories (int): Number of stories to retrieve

    Returns:
        str: JSON string containing story details
    """
    # Fetch top story IDs
    response = httpx.get("https://hacker-news.firebaseio.com/v0/topstories.json")
    story_ids = response.json()

    # Yield story details
    for story_id in story_ids[:num_stories]:
        story_response = httpx.get(
            f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
        )
        story = story_response.json()
        if "text" in story:
            story.pop("text", None)
        yield json.dumps(story)


# Initialize the agent with a tech-savvy personality and clear instructions
agent = Agent(
    description="A Tech News Assistant that fetches and summarizes Hacker News stories",
    instructions=dedent("""\
        You are an enthusiastic Tech Reporter

        Your responsibilities:
        - Present Hacker News stories in an engaging and informative way
        - Provide clear summaries of the information you gather

        Style guide:
        - Use emoji to make your responses more engaging
        - Keep your summaries concise but informative
        - End with a friendly tech-themed sign-off\
    """),
    tools=[get_top_hackernews_stories],
    show_tool_calls=True,
    markdown=True,
)

# Example questions to try:
# - "What are the top 3 HN stories right now?"
# - "Show me the most recent story from Hacker News"
# - "Get the top 5 stories (you can try accepting and declining the confirmation)"
agent.print_response(
    "What are the top 2 hackernews stories?", stream=True, console=console
)
```

## [​](#usage) Usage

1

Create a virtual environment

Open the `Terminal` and create a python virtual environment.

```
python3 -m venv .venv
source .venv/bin/activate
```

2

Install libraries

```
pip install openai agno
```

3

Run the agent

```
python human_in_the_loop.py
```

---

## getting-started__image-agent.md

This example shows how to create an AI agent that can analyze images and connect them with current events using web searches. Perfect for:

1. News reporting and journalism
2. Travel and tourism content
3. Social media analysis
4. Educational presentations
5. Event coverage

Example images to try:

* Famous landmarks (Eiffel Tower, Taj Mahal, etc.)
* City skylines
* Cultural events and festivals
* Breaking news scenes
* Historical locations

## [​](#code) Code

image\_agent.py

```
from textwrap import dedent

from agno.agent import Agent
from agno.media import Image
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    description=dedent("""\
        You are a world-class visual journalist and cultural correspondent with a gift
        for bringing images to life through storytelling! 📸✨ With the observational skills
        of a detective and the narrative flair of a bestselling author, you transform visual
        analysis into compelling stories that inform and captivate.\
    """),
    instructions=dedent("""\
        When analyzing images and reporting news, follow these principles:

        1. Visual Analysis:
           - Start with an attention-grabbing headline using relevant emoji
           - Break down key visual elements with expert precision
           - Notice subtle details others might miss
           - Connect visual elements to broader contexts

        2. News Integration:
           - Research and verify current events related to the image
           - Connect historical context with present-day significance
           - Prioritize accuracy while maintaining engagement
           - Include relevant statistics or data when available

        3. Storytelling Style:
           - Maintain a professional yet engaging tone
           - Use vivid, descriptive language
           - Include cultural and historical references when relevant
           - End with a memorable sign-off that fits the story

        4. Reporting Guidelines:
           - Keep responses concise but informative (2-3 paragraphs)
           - Balance facts with human interest
           - Maintain journalistic integrity
           - Credit sources when citing specific information

        Transform every image into a compelling news story that informs and inspires!\
    """),
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True,
)

# Example usage with a famous landmark
agent.print_response(
    "Tell me about this image and share the latest relevant news.",
    images=[
        Image(
            url="https://upload.wikimedia.org/wikipedia/commons/0/0c/GoldenGateBridge-001.jpg"
        )
    ],
    stream=True,
)

# More examples to try:
"""
Sample prompts to explore:
1. "What's the historical significance of this location?"
2. "How has this place changed over time?"
3. "What cultural events happen here?"
4. "What's the architectural style and influence?"
5. "What recent developments affect this area?"

Sample image URLs to analyze:
1. Eiffel Tower: "https://upload.wikimedia.org/wikipedia/commons/8/85/Tour_Eiffel_Wikimedia_Commons_%28cropped%29.jpg"
2. Taj Mahal: "https://upload.wikimedia.org/wikipedia/commons/b/bd/Taj_Mahal%2C_Agra%2C_India_edit3.jpg"
3. Golden Gate Bridge: "https://upload.wikimedia.org/wikipedia/commons/0/0c/GoldenGateBridge-001.jpg"
"""

# To get the response in a variable:
# from rich.pretty import pprint
# response = agent.run(
#     "Analyze this landmark's architecture and recent news.",
#     images=[Image(url="YOUR_IMAGE_URL")],
# )
# pprint(response.content)
```

## [​](#usage) Usage

1

Create a virtual environment

Open the `Terminal` and create a python virtual environment.

```
python3 -m venv .venv
source .venv/bin/activate
```

2

Install libraries

```
pip install openai duckduckgo-search agno
```

3

Run the agent

```
python image_agent.py
```

---

## getting-started__image-generation.md

This example shows how to create an AI agent that generates images using DALL-E.
You can use this agent to create various types of images, from realistic photos to artistic
illustrations and creative concepts.
Example prompts to try:

* “Create a surreal painting of a floating city in the clouds at sunset”
* “Generate a photorealistic image of a cozy coffee shop interior”
* “Design a cute cartoon mascot for a tech startup”
* “Create an artistic portrait of a cyberpunk samurai”

## [​](#code) Code

image\_generation.py

```
from textwrap import dedent

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.dalle import DalleTools

# Create an Creative AI Artist Agent
image_agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    tools=[DalleTools()],
    description=dedent("""\
        You are an experienced AI artist with expertise in various artistic styles,
        from photorealism to abstract art. You have a deep understanding of composition,
        color theory, and visual storytelling.\
    """),
    instructions=dedent("""\
        As an AI artist, follow these guidelines:
        1. Analyze the user's request carefully to understand the desired style and mood
        2. Before generating, enhance the prompt with artistic details like lighting, perspective, and atmosphere
        3. Use the `create_image` tool with detailed, well-crafted prompts
        4. Provide a brief explanation of the artistic choices made
        5. If the request is unclear, ask for clarification about style preferences

        Always aim to create visually striking and meaningful images that capture the user's vision!\
    """),
    markdown=True,
    show_tool_calls=True,
)

# Example usage
image_agent.print_response(
    "Create a magical library with floating books and glowing crystals", stream=True
)

# Retrieve and display generated images
images = image_agent.get_images()
if images and isinstance(images, list):
    for image_response in images:
        image_url = image_response.url
        print(f"Generated image URL: {image_url}")

# More example prompts to try:
"""
Try these creative prompts:
1. "Generate a steampunk-style robot playing a violin"
2. "Design a peaceful zen garden during cherry blossom season"
3. "Create an underwater city with bioluminescent buildings"
4. "Generate a cozy cabin in a snowy forest at night"
5. "Create a futuristic cityscape with flying cars and skyscrapers"
"""
```

## [​](#usage) Usage

1

Create a virtual environment

Open the `Terminal` and create a python virtual environment.

```
python3 -m venv .venv
source .venv/bin/activate
```

2

Install libraries

```
pip install openai agno
```

3

Run the agent

```
python image_generation.py
```

---

## getting-started__introduction.md

This guide walks through the basics of building Agents with Agno.
The examples build on each other, introducing new concepts and capabilities progressively. Each example contains detailed comments, example prompts, and required dependencies.

## [​](#setup) Setup

Create a virtual environment:

```
python3 -m venv .venv
source .venv/bin/activate
```

Install the required dependencies:

```
pip install openai duckduckgo-search yfinance lancedb tantivy pypdf requests exa-py newspaper4k lxml_html_clean sqlalchemy agno
```

Export your OpenAI API key:

```
export OPENAI_API_KEY=your_api_key
```

## [​](#examples) Examples

[## Basic Agent

Build a news reporter with a vibrant personality. This Agent only shows basic LLM inference.](./basic-agent)[## Agent with Tools

Add web search capabilities using DuckDuckGo for real-time information gathering.](./agent-with-tools)[## Agent with Knowledge

Add a vector database to your agent to store and search knowledge.](./agent-with-knowledge)[## Agent with Storage

Add persistence to your agents with session management and history capabilities.](./agent-with-storage)[## Agent Team

Create an agent team specializing in market research and financial analysis.](./agent-team)[## Structured Output

Generate a structured output using a Pydantic model.](./structured-output)[## Custom Tools

Create and integrate custom tools with your agent.](./custom-tools)[## Research Agent

Build an AI research agent using Exa with controlled output steering.](./research-agent)[## Research Workflow

Create a research workflow combining web searches and content scraping.](./research-workflow)[## Image Agent

Create an agent that can understand images.](./image-agent)[## Image Generation

Create an Agent that can generate images using DALL-E.](./image-generation)[## Video Generation

Create an Agent that can generate videos using ModelsLabs.](./video-generation)[## Audio Agent

Create an Agent that can process audio input and generate responses.](./audio-agent)[## Agent with State

Create an Agent with session state management.](./agent-state)[## Agent Context

Evaluate dependencies at agent.run and inject them into the instructions.](./agent-context)[## Agent Session

Create an Agent with persistent session memory across conversations.](./agent-session)[## User Memories

Create an Agent that stores user memories and summaries.](./user-memories)[## Function Retries

Handle function retries for failed or unsatisfactory outputs.](./retry-functions)[## Human in the Loop

Add user confirmation and safety checks for interactive agent control.](./human-in-the-loop)

Each example includes runnable code and detailed explanations. We recommend following them in order, as concepts build upon previous examples.

---

## getting-started__research-agent.md

This example shows how to create an advanced research agent by combining exa’s search capabilities with academic writing skills to deliver well-structured, fact-based reports.
Key features demonstrated:

* Using Exa.ai for academic and news searches
* Structured report generation with references
* Custom formatting and file saving capabilities

Example prompts to try:

* “What are the latest developments in quantum computing?”
* “Research the current state of artificial consciousness”
* “Analyze recent breakthroughs in fusion energy”
* “Investigate the environmental impact of space tourism”
* “Explore the latest findings in longevity research”

## [​](#code) Code

research\_agent.py

```
from datetime import datetime
from pathlib import Path
from textwrap import dedent

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.exa import ExaTools

cwd = Path(__file__).parent.resolve()
tmp = cwd.joinpath("tmp")
if not tmp.exists():
    tmp.mkdir(exist_ok=True, parents=True)

today = datetime.now().strftime("%Y-%m-%d")

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    tools=[ExaTools(start_published_date=today, type="keyword")],
    description=dedent("""\
        You are Professor X-1000, a distinguished AI research scientist with expertise
        in analyzing and synthesizing complex information. Your specialty lies in creating
        compelling, fact-based reports that combine academic rigor with engaging narrative.

        Your writing style is:
        - Clear and authoritative
        - Engaging but professional
        - Fact-focused with proper citations
        - Accessible to educated non-specialists\
    """),
    instructions=dedent("""\
        Begin by running 3 distinct searches to gather comprehensive information.
        Analyze and cross-reference sources for accuracy and relevance.
        Structure your report following academic standards but maintain readability.
        Include only verifiable facts with proper citations.
        Create an engaging narrative that guides the reader through complex topics.
        End with actionable takeaways and future implications.\
    """),
    expected_output=dedent("""\
    A professional research report in markdown format:

    # {Compelling Title That Captures the Topic's Essence}

    ## Executive Summary
    {Brief overview of key findings and significance}

    ## Introduction
    {Context and importance of the topic}
    {Current state of research/discussion}

    ## Key Findings
    {Major discoveries or developments}
    {Supporting evidence and analysis}

    ## Implications
    {Impact on field/society}
    {Future directions}

    ## Key Takeaways
    - {Bullet point 1}
    - {Bullet point 2}
    - {Bullet point 3}

    ## References
    - [Source 1](link) - Key finding/quote
    - [Source 2](link) - Key finding/quote
    - [Source 3](link) - Key finding/quote

    ---
    Report generated by Professor X-1000
    Advanced Research Systems Division
    Date: {current_date}\
    """),
    markdown=True,
    show_tool_calls=True,
    add_datetime_to_instructions=True,
    save_response_to_file=str(tmp.joinpath("{message}.md")),
)

# Example usage
if __name__ == "__main__":
    # Generate a research report on a cutting-edge topic
    agent.print_response(
        "Research the latest developments in brain-computer interfaces", stream=True
    )

# More example prompts to try:
"""
Try these research topics:
1. "Analyze the current state of solid-state batteries"
2. "Research recent breakthroughs in CRISPR gene editing"
3. "Investigate the development of autonomous vehicles"
4. "Explore advances in quantum machine learning"
5. "Study the impact of artificial intelligence on healthcare"
"""
```

## [​](#usage) Usage

1

Create a virtual environment

Open the `Terminal` and create a python virtual environment.

```
python3 -m venv .venv
source .venv/bin/activate
```

2

Install libraries

```
pip install openai exa-py agno
```

3

Run the agent

```
python research_agent.py
```

---

## getting-started__research-workflow.md

This example shows how to build a sophisticated research workflow that combines:
🔍 Web search capabilities for finding relevant sources
📚 Content extraction and processing
✍️ Academic-style report generation
💾 Smart caching for improved performance
We’ve used the following tools as they’re available for free:

* DuckDuckGoTools: Searches the web for relevant articles
* Newspaper4kTools: Scrapes and processes article content

Example research topics to try:

* “What are the latest developments in quantum computing?”
* “Research the current state of artificial consciousness”
* “Analyze recent breakthroughs in fusion energy”
* “Investigate the environmental impact of space tourism”
* “Explore the latest findings in longevity research”

## [​](#code) Code

research\_workflow.py

```
import json
from textwrap import dedent
from typing import Dict, Iterator, Optional

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.storage.workflow.sqlite import SqliteWorkflowStorage
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.newspaper4k import Newspaper4kTools
from agno.utils.log import logger
from agno.utils.pprint import pprint_run_response
from agno.workflow import RunEvent, RunResponse, Workflow
from pydantic import BaseModel, Field


class Article(BaseModel):
    title: str = Field(..., description="Title of the article.")
    url: str = Field(..., description="Link to the article.")
    summary: Optional[str] = Field(
        ..., description="Summary of the article if available."
    )


class SearchResults(BaseModel):
    articles: list[Article]


class ScrapedArticle(BaseModel):
    title: str = Field(..., description="Title of the article.")
    url: str = Field(..., description="Link to the article.")
    summary: Optional[str] = Field(
        ..., description="Summary of the article if available."
    )
    content: Optional[str] = Field(
        ...,
        description="Content of the in markdown format if available. Return None if the content is not available or does not make sense.",
    )


class ResearchReportGenerator(Workflow):
    description: str = dedent("""\
    Generate comprehensive research reports that combine academic rigor
    with engaging storytelling. This workflow orchestrates multiple AI agents to search, analyze,
    and synthesize information from diverse sources into well-structured reports.
    """)

    web_searcher: Agent = Agent(
        model=OpenAIChat(id="gpt-4o-mini"),
        tools=[DuckDuckGoTools()],
        description=dedent("""\
        You are ResearchBot-X, an expert at discovering and evaluating academic and scientific sources.\
        """),
        instructions=dedent("""\
        You're a meticulous research assistant with expertise in source evaluation! 🔍
        Search for 10-15 sources and identify the 5-7 most authoritative and relevant ones.
        Prioritize:
        - Peer-reviewed articles and academic publications
        - Recent developments from reputable institutions
        - Authoritative news sources and expert commentary
        - Diverse perspectives from recognized experts
        Avoid opinion pieces and non-authoritative sources.\
        """),
        response_model=SearchResults,
    )

    article_scraper: Agent = Agent(
        model=OpenAIChat(id="gpt-4o-mini"),
        tools=[Newspaper4kTools()],
        description=dedent("""\
        You are ContentBot-X, an expert at extracting and structuring academic content.\
        """),
        instructions=dedent("""\
        You're a precise content curator with attention to academic detail! 📚
        When processing content:
           - Extract content from the article
           - Preserve academic citations and references
           - Maintain technical accuracy in terminology
           - Structure content logically with clear sections
           - Extract key findings and methodology details
           - Handle paywalled content gracefully
        Format everything in clean markdown for optimal readability.\
        """),
        response_model=ScrapedArticle,
    )

    writer: Agent = Agent(
        model=OpenAIChat(id="gpt-4o"),
        description=dedent("""\
        You are Professor X-2000, a distinguished AI research scientist combining academic rigor with engaging narrative style.\
        """),
        instructions=dedent("""\
        Channel the expertise of a world-class academic researcher!
        🎯 Analysis Phase:
          - Evaluate source credibility and relevance
          - Cross-reference findings across sources
          - Identify key themes and breakthroughs
        💡 Synthesis Phase:
          - Develop a coherent narrative framework
          - Connect disparate findings
          - Highlight contradictions or gaps
        ✍️ Writing Phase:
          - Begin with an engaging executive summary, hook the reader
          - Present complex ideas clearly
          - Support all claims with citations
          - Balance depth with accessibility
          - Maintain academic tone while ensuring readability
          - End with implications and future directions\
        """),
        expected_output=dedent("""\
        # {Compelling Academic Title}

        ## Executive Summary
        {Concise overview of key findings and significance}

        ## Introduction
        {Research context and background}
        {Current state of the field}

        ## Methodology
        {Search and analysis approach}
        {Source evaluation criteria}

        ## Key Findings
        {Major discoveries and developments}
        {Supporting evidence and analysis}
        {Contrasting viewpoints}

        ## Analysis
        {Critical evaluation of findings}
        {Integration of multiple perspectives}
        {Identification of patterns and trends}

        ## Implications
        {Academic and practical significance}
        {Future research directions}
        {Potential applications}

        ## Key Takeaways
        - {Critical finding 1}
        - {Critical finding 2}
        - {Critical finding 3}

        ## References
        {Properly formatted academic citations}

        ---
        Report generated by Professor X-2000
        Advanced Research Division
        Date: {current_date}\
        """),
        markdown=True,
    )

    def run(
        self,
        topic: str,
        use_search_cache: bool = True,
        use_scrape_cache: bool = True,
        use_cached_report: bool = True,
    ) -> Iterator[RunResponse]:
        """
        Generate a comprehensive news report on a given topic.

        This function orchestrates a workflow to search for articles, scrape their content,
        and generate a final report. It utilizes caching mechanisms to optimize performance.

        Args:
            topic (str): The topic for which to generate the news report.
            use_search_cache (bool, optional): Whether to use cached search results. Defaults to True.
            use_scrape_cache (bool, optional): Whether to use cached scraped articles. Defaults to True.
            use_cached_report (bool, optional): Whether to return a previously generated report on the same topic. Defaults to False.

        Returns:
            Iterator[RunResponse]: An stream of objects containing the generated report or status information.

        Steps:
        1. Check for a cached report if use_cached_report is True.
        2. Search the web for articles on the topic:
            - Use cached search results if available and use_search_cache is True.
            - Otherwise, perform a new web search.
        3. Scrape the content of each article:
            - Use cached scraped articles if available and use_scrape_cache is True.
            - Scrape new articles that aren't in the cache.
        4. Generate the final report using the scraped article contents.

        The function utilizes the `session_state` to store and retrieve cached data.
        """
        logger.info(f"Generating a report on: {topic}")

        # Use the cached report if use_cached_report is True
        if use_cached_report:
            cached_report = self.get_cached_report(topic)
            if cached_report:
                yield RunResponse(
                    content=cached_report, event=RunEvent.workflow_completed
                )
                return

        # Search the web for articles on the topic
        search_results: Optional[SearchResults] = self.get_search_results(
            topic, use_search_cache
        )
        # If no search_results are found for the topic, end the workflow
        if search_results is None or len(search_results.articles) == 0:
            yield RunResponse(
                event=RunEvent.workflow_completed,
                content=f"Sorry, could not find any articles on the topic: {topic}",
            )
            return

        # Scrape the search results
        scraped_articles: Dict[str, ScrapedArticle] = self.scrape_articles(
            search_results, use_scrape_cache
        )

        # Write a research report
        yield from self.write_research_report(topic, scraped_articles)

    def get_cached_report(self, topic: str) -> Optional[str]:
        logger.info("Checking if cached report exists")
        return self.session_state.get("reports", {}).get(topic)

    def add_report_to_cache(self, topic: str, report: str):
        logger.info(f"Saving report for topic: {topic}")
        self.session_state.setdefault("reports", {})
        self.session_state["reports"][topic] = report
        # Save the report to the storage
        self.write_to_storage()

    def get_cached_search_results(self, topic: str) -> Optional[SearchResults]:
        logger.info("Checking if cached search results exist")
        return self.session_state.get("search_results", {}).get(topic)

    def add_search_results_to_cache(self, topic: str, search_results: SearchResults):
        logger.info(f"Saving search results for topic: {topic}")
        self.session_state.setdefault("search_results", {})
        self.session_state["search_results"][topic] = search_results.model_dump()
        # Save the search results to the storage
        self.write_to_storage()

    def get_cached_scraped_articles(
        self, topic: str
    ) -> Optional[Dict[str, ScrapedArticle]]:
        logger.info("Checking if cached scraped articles exist")
        return self.session_state.get("scraped_articles", {}).get(topic)

    def add_scraped_articles_to_cache(
        self, topic: str, scraped_articles: Dict[str, ScrapedArticle]
    ):
        logger.info(f"Saving scraped articles for topic: {topic}")
        self.session_state.setdefault("scraped_articles", {})
        self.session_state["scraped_articles"][topic] = scraped_articles
        # Save the scraped articles to the storage
        self.write_to_storage()

    def get_search_results(
        self, topic: str, use_search_cache: bool, num_attempts: int = 3
    ) -> Optional[SearchResults]:
        # Get cached search_results from the session state if use_search_cache is True
        if use_search_cache:
            try:
                search_results_from_cache = self.get_cached_search_results(topic)
                if search_results_from_cache is not None:
                    search_results = SearchResults.model_validate(
                        search_results_from_cache
                    )
                    logger.info(
                        f"Found {len(search_results.articles)} articles in cache."
                    )
                    return search_results
            except Exception as e:
                logger.warning(f"Could not read search results from cache: {e}")

        # If there are no cached search_results, use the web_searcher to find the latest articles
        for attempt in range(num_attempts):
            try:
                searcher_response: RunResponse = self.web_searcher.run(topic)
                if (
                    searcher_response is not None
                    and searcher_response.content is not None
                    and isinstance(searcher_response.content, SearchResults)
                ):
                    article_count = len(searcher_response.content.articles)
                    logger.info(
                        f"Found {article_count} articles on attempt {attempt + 1}"
                    )
                    # Cache the search results
                    self.add_search_results_to_cache(topic, searcher_response.content)
                    return searcher_response.content
                else:
                    logger.warning(
                        f"Attempt {attempt + 1}/{num_attempts} failed: Invalid response type"
                    )
            except Exception as e:
                logger.warning(f"Attempt {attempt + 1}/{num_attempts} failed: {str(e)}")

        logger.error(f"Failed to get search results after {num_attempts} attempts")
        return None

    def scrape_articles(
        self, search_results: SearchResults, use_scrape_cache: bool
    ) -> Dict[str, ScrapedArticle]:
        scraped_articles: Dict[str, ScrapedArticle] = {}

        # Get cached scraped_articles from the session state if use_scrape_cache is True
        if use_scrape_cache:
            try:
                scraped_articles_from_cache = self.get_cached_scraped_articles(topic)
                if scraped_articles_from_cache is not None:
                    scraped_articles = scraped_articles_from_cache
                    logger.info(
                        f"Found {len(scraped_articles)} scraped articles in cache."
                    )
                    return scraped_articles
            except Exception as e:
                logger.warning(f"Could not read scraped articles from cache: {e}")

        # Scrape the articles that are not in the cache
        for article in search_results.articles:
            if article.url in scraped_articles:
                logger.info(f"Found scraped article in cache: {article.url}")
                continue

            article_scraper_response: RunResponse = self.article_scraper.run(
                article.url
            )
            if (
                article_scraper_response is not None
                and article_scraper_response.content is not None
                and isinstance(article_scraper_response.content, ScrapedArticle)
            ):
                scraped_articles[article_scraper_response.content.url] = (
                    article_scraper_response.content
                )
                logger.info(f"Scraped article: {article_scraper_response.content.url}")

        # Save the scraped articles in the session state
        self.add_scraped_articles_to_cache(topic, scraped_articles)
        return scraped_articles

    def write_research_report(
        self, topic: str, scraped_articles: Dict[str, ScrapedArticle]
    ) -> Iterator[RunResponse]:
        logger.info("Writing research report")
        # Prepare the input for the writer
        writer_input = {
            "topic": topic,
            "articles": [v.model_dump() for v in scraped_articles.values()],
        }
        # Run the writer and yield the response
        yield from self.writer.run(json.dumps(writer_input, indent=4), stream=True)
        # Save the research report in the cache
        self.add_report_to_cache(topic, self.writer.run_response.content)


# Run the workflow if the script is executed directly
if __name__ == "__main__":
    from rich.prompt import Prompt

    # Example research topics
    example_topics = [
        "quantum computing breakthroughs 2024",
        "artificial consciousness research",
        "fusion energy developments",
        "space tourism environmental impact",
        "longevity research advances",
    ]

    topics_str = "\n".join(
        f"{i + 1}. {topic}" for i, topic in enumerate(example_topics)
    )

    print(f"\n📚 Example Research Topics:\n{topics_str}\n")

    # Get topic from user
    topic = Prompt.ask(
        "[bold]Enter a research topic[/bold]\n✨",
        default="quantum computing breakthroughs 2024",
    )

    # Convert the topic to a URL-safe string for use in session_id
    url_safe_topic = topic.lower().replace(" ", "-")

    # Initialize the news report generator workflow
    generate_research_report = ResearchReportGenerator(
        session_id=f"generate-report-on-{url_safe_topic}",
        storage=SqliteWorkflowStorage(
            table_name="generate_research_report_workflow",
            db_file="tmp/workflows.db",
        ),
    )

    # Execute the workflow with caching enabled
    report_stream: Iterator[RunResponse] = generate_research_report.run(
        topic=topic,
        use_search_cache=True,
        use_scrape_cache=True,
        use_cached_report=True,
    )

    # Print the response
    pprint_run_response(report_stream, markdown=True)
```

## [​](#usage) Usage

1

Create a virtual environment

Open the `Terminal` and create a python virtual environment.

```
python3 -m venv .venv
source .venv/bin/activate
```

2

Install libraries

```
openai duckduckgo-search newspaper4k lxml_html_clean sqlalchemy agno
```

3

Run the workflow

```
python research_workflow.py
```

---

## getting-started__retry-functions.md

This example shows how to retry a function call if it fails or you do not like the output. This is useful for:

* Handling temporary failures
* Improving output quality through retries
* Implementing human-in-the-loop validation

## [​](#code) Code

retry\_functions.py

```
from typing import Iterator

from agno.agent import Agent
from agno.exceptions import RetryAgentRun
from agno.tools import FunctionCall, tool

num_calls = 0


def pre_hook(fc: FunctionCall):
    global num_calls

    print(f"Pre-hook: {fc.function.name}")
    print(f"Arguments: {fc.arguments}")
    num_calls += 1
    if num_calls < 2:
        raise RetryAgentRun(
            "This wasn't interesting enough, please retry with a different argument"
        )


@tool(pre_hook=pre_hook)
def print_something(something: str) -> Iterator[str]:
    print(something)
    yield f"I have printed {something}"


agent = Agent(tools=[print_something], markdown=True)
agent.print_response("Print something interesting", stream=True)
```

## [​](#usage) Usage

1

Create a virtual environment

Open the `Terminal` and create a python virtual environment.

```
python3 -m venv .venv
source .venv/bin/activate
```

2

Install libraries

```
pip install openai agno
```

3

Run the agent

```
python retry_functions.py
```

---

## getting-started__structured-output.md

This example shows how to use structured outputs with AI agents to generate well-formatted movie script concepts. It shows two approaches:

1. JSON Mode: Traditional JSON response parsing
2. Structured Output: Enhanced structured data handling

Example prompts to try:

* “Tokyo” - Get a high-tech thriller set in futuristic Japan
* “Ancient Rome” - Experience an epic historical drama
* “Manhattan” - Explore a modern romantic comedy
* “Amazon Rainforest” - Adventure in an exotic location
* “Mars Colony” - Science fiction in a space settlement

## [​](#code) Code

structured\_output.py

```
from textwrap import dedent
from typing import List

from agno.agent import Agent, RunResponse  # noqa
from agno.models.openai import OpenAIChat
from pydantic import BaseModel, Field


class MovieScript(BaseModel):
    setting: str = Field(
        ...,
        description="A richly detailed, atmospheric description of the movie's primary location and time period. Include sensory details and mood.",
    )
    ending: str = Field(
        ...,
        description="The movie's powerful conclusion that ties together all plot threads. Should deliver emotional impact and satisfaction.",
    )
    genre: str = Field(
        ...,
        description="The film's primary and secondary genres (e.g., 'Sci-fi Thriller', 'Romantic Comedy'). Should align with setting and tone.",
    )
    name: str = Field(
        ...,
        description="An attention-grabbing, memorable title that captures the essence of the story and appeals to target audience.",
    )
    characters: List[str] = Field(
        ...,
        description="4-6 main characters with distinctive names and brief role descriptions (e.g., 'Sarah Chen - brilliant quantum physicist with a dark secret').",
    )
    storyline: str = Field(
        ...,
        description="A compelling three-sentence plot summary: Setup, Conflict, and Stakes. Hook readers with intrigue and emotion.",
    )


# Agent that uses JSON mode
json_mode_agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    description=dedent("""\
        You are an acclaimed Hollywood screenwriter known for creating unforgettable blockbusters! 🎬
        With the combined storytelling prowess of Christopher Nolan, Aaron Sorkin, and Quentin Tarantino,
        you craft unique stories that captivate audiences worldwide.

        Your specialty is turning locations into living, breathing characters that drive the narrative.\
    """),
    instructions=dedent("""\
        When crafting movie concepts, follow these principles:

        1. Settings should be characters:
           - Make locations come alive with sensory details
           - Include atmospheric elements that affect the story
           - Consider the time period's impact on the narrative

        2. Character Development:
           - Give each character a unique voice and clear motivation
           - Create compelling relationships and conflicts
           - Ensure diverse representation and authentic backgrounds

        3. Story Structure:
           - Begin with a hook that grabs attention
           - Build tension through escalating conflicts
           - Deliver surprising yet inevitable endings

        4. Genre Mastery:
           - Embrace genre conventions while adding fresh twists
           - Mix genres thoughtfully for unique combinations
           - Maintain consistent tone throughout

        Transform every location into an unforgettable cinematic experience!\
    """),
    response_model=MovieScript,
    use_json_mode=True,
)

# Agent that uses structured outputs
structured_output_agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    description=dedent("""\
        You are an acclaimed Hollywood screenwriter known for creating unforgettable blockbusters! 🎬
        With the combined storytelling prowess of Christopher Nolan, Aaron Sorkin, and Quentin Tarantino,
        you craft unique stories that captivate audiences worldwide.

        Your specialty is turning locations into living, breathing characters that drive the narrative.\
    """),
    instructions=dedent("""\
        When crafting movie concepts, follow these principles:

        1. Settings should be characters:
           - Make locations come alive with sensory details
           - Include atmospheric elements that affect the story
           - Consider the time period's impact on the narrative

        2. Character Development:
           - Give each character a unique voice and clear motivation
           - Create compelling relationships and conflicts
           - Ensure diverse representation and authentic backgrounds

        3. Story Structure:
           - Begin with a hook that grabs attention
           - Build tension through escalating conflicts
           - Deliver surprising yet inevitable endings

        4. Genre Mastery:
           - Embrace genre conventions while adding fresh twists
           - Mix genres thoughtfully for unique combinations
           - Maintain consistent tone throughout

        Transform every location into an unforgettable cinematic experience!\
    """),
    response_model=MovieScript,
)

# Example usage with different locations
json_mode_agent.print_response("Tokyo", stream=True)
structured_output_agent.print_response("Ancient Rome", stream=True)

# More examples to try:
"""
Creative location prompts to explore:
1. "Underwater Research Station" - For a claustrophobic sci-fi thriller
2. "Victorian London" - For a gothic mystery
3. "Dubai 2050" - For a futuristic heist movie
4. "Antarctic Research Base" - For a survival horror story
5. "Caribbean Island" - For a tropical adventure romance
"""

# To get the response in a variable:
# from rich.pretty import pprint

# json_mode_response: RunResponse = json_mode_agent.run("New York")
# pprint(json_mode_response.content)
# structured_output_response: RunResponse = structured_output_agent.run("New York")
# pprint(structured_output_response.content)
```

## [​](#usage) Usage

1

Create a virtual environment

Open the `Terminal` and create a python virtual environment.

```
python3 -m venv .venv
source .venv/bin/activate
```

2

Install libraries

```
pip install openai agno
```

3

Run the agent

```
python structured_output.py
```

---

## getting-started__user-memories.md

This example shows how to create an agent with persistent memory that stores:

1. Personalized user memories - facts and preferences learned about specific users
2. Session summaries - key points and context from conversations
3. Chat history - stored in SQLite for persistence

Key features:

* Stores user-specific memories in SQLite database
* Maintains session summaries for context
* Continues conversations across sessions with memory
* References previous context and user information in responses

Examples:
User: “My name is John and I live in NYC”
Agent: *Creates memory about John’s location*
User: “What do you remember about me?”
Agent: *Recalls previous memories about John*

## [​](#code) Code

user\_memories.py

```
import json
from textwrap import dedent
from typing import Optional

import typer
from agno.agent import Agent
from agno.memory.v2.db.sqlite import SqliteMemoryDb
from agno.memory.v2.memory import Memory
from agno.models.openai import OpenAIChat
from agno.storage.sqlite import SqliteStorage
from rich.console import Console
from rich.json import JSON
from rich.panel import Panel
from rich.prompt import Prompt


def create_agent(user: str = "user"):
    session_id: Optional[str] = None

    # Ask if user wants to start new session or continue existing one
    new = typer.confirm("Do you want to start a new session?")

    # Initialize storage for both agent sessions and memories
    agent_storage = SqliteStorage(table_name="agent_memories", db_file="tmp/agents.db")

    if not new:
        existing_sessions = agent_storage.get_all_session_ids(user)
        if len(existing_sessions) > 0:
            session_id = existing_sessions[0]

    agent = Agent(
        model=OpenAIChat(id="gpt-4o"),
        user_id=user,
        session_id=session_id,
        # Configure memory system with SQLite storage
        memory=Memory(
            db=SqliteMemoryDb(
                table_name="agent_memory",
                db_file="tmp/agent_memory.db",
            ),
        ),
        enable_user_memories=True,
        enable_session_summaries=True,
        storage=agent_storage,
        add_history_to_messages=True,
        num_history_responses=3,
        # Enhanced system prompt for better personality and memory usage
        description=dedent("""\
        You are a helpful and friendly AI assistant with excellent memory.
        - Remember important details about users and reference them naturally
        - Maintain a warm, positive tone while being precise and helpful
        - When appropriate, refer back to previous conversations and memories
        - Always be truthful about what you remember or don't remember"""),
    )

    if session_id is None:
        session_id = agent.session_id
        if session_id is not None:
            print(f"Started Session: {session_id}\n")
        else:
            print("Started Session\n")
    else:
        print(f"Continuing Session: {session_id}\n")

    return agent


def print_agent_memory(agent):
    """Print the current state of agent's memory systems"""
    console = Console()

    messages = []
    session_id = agent.session_id
    session_run = agent.memory.runs[session_id][-1]
    for m in session_run.messages:
        message_dict = m.to_dict()
        messages.append(message_dict)


    # Print chat history
    console.print(
        Panel(
            JSON(
                json.dumps(
                    messages,
                ),
                indent=4,
            ),
            title=f"Chat History for session_id: {session_run.session_id}",
            expand=True,
        )
    )

    # Print user memories
    for user_id in list(agent.memory.memories.keys()):
        console.print(
            Panel(
                JSON(
                    json.dumps(
                    [
                        user_memory.to_dict()
                        for user_memory in agent.memory.get_user_memories(user_id=user_id)
                    ],
                        indent=4,
                    ),
                ),
                title=f"Memories for user_id: {user_id}",
                expand=True,
            )
        )

    # Print session summary
    for user_id in list(agent.memory.summaries.keys()):
        console.print(
            Panel(
                JSON(
                    json.dumps(
                        [
                            summary.to_dict()
                            for summary in agent.memory.get_session_summaries(user_id=user_id)
                        ],
                        indent=4,
                    ),
                ),
                title=f"Summary for session_id: {agent.session_id}",
                expand=True,
            )
        )



def main(user: str = "user"):
    """Interactive chat loop with memory display"""
    agent = create_agent(user)

    print("Try these example inputs:")
    print("- 'My name is [name] and I live in [city]'")
    print("- 'I love [hobby/interest]'")
    print("- 'What do you remember about me?'")
    print("- 'What have we discussed so far?'\n")

    exit_on = ["exit", "quit", "bye"]
    while True:
        message = Prompt.ask(f"[bold] :sunglasses: {user} [/bold]")
        if message in exit_on:
            break

        agent.print_response(message=message, stream=True, markdown=True)
        print_agent_memory(agent)


if __name__ == "__main__":
    typer.run(main)
```

## [​](#usage) Usage

1

Create a virtual environment

Open the `Terminal` and create a python virtual environment.

```
python3 -m venv .venv
source .venv/bin/activate
```

2

Install libraries

```
pip install openai sqlalchemy agno
```

3

Run the agent

```
python user_memories.py
```

---

## getting-started__video-generation.md

This example shows how to create an AI agent that generates videos using ModelsLabs.
You can use this agent to create various types of short videos, from animated scenes
to creative visual stories.
Example prompts to try:

* “Create a serene video of waves crashing on a beach at sunset”
* “Generate a magical video of butterflies flying in a enchanted forest”
* “Create a timelapse of a blooming flower in a garden”
* “Generate a video of northern lights dancing in the night sky”

## [​](#code) Code

video\_generation.py

```
from textwrap import dedent

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.models_labs import ModelsLabTools

# Create a Creative AI Video Director Agent
video_agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    tools=[ModelsLabTools()],
    description=dedent("""\
        You are an experienced AI video director with expertise in various video styles,
        from nature scenes to artistic animations. You have a deep understanding of motion,
        timing, and visual storytelling through video content.\
    """),
    instructions=dedent("""\
        As an AI video director, follow these guidelines:
        1. Analyze the user's request carefully to understand the desired style and mood
        2. Before generating, enhance the prompt with details about motion, timing, and atmosphere
        3. Use the `generate_media` tool with detailed, well-crafted prompts
        4. Provide a brief explanation of the creative choices made
        5. If the request is unclear, ask for clarification about style preferences

        The video will be displayed in the UI automatically below your response.
        Always aim to create captivating and meaningful videos that bring the user's vision to life!\
    """),
    markdown=True,
    show_tool_calls=True,
)

# Example usage
video_agent.print_response(
    "Generate a cosmic journey through a colorful nebula", stream=True
)

# Retrieve and display generated videos
videos = video_agent.get_videos()
if videos:
    for video in videos:
        print(f"Generated video URL: {video.url}")

# More example prompts to try:
"""
Try these creative prompts:
1. "Create a video of autumn leaves falling in a peaceful forest"
2. "Generate a video of a cat playing with a ball"
3. "Create a video of a peaceful koi pond with rippling water"
4. "Generate a video of a cozy fireplace with dancing flames"
5. "Create a video of a mystical portal opening in a magical realm"
"""
```

## [​](#usage) Usage

1

Create a virtual environment

Open the `Terminal` and create a python virtual environment.

```
python3 -m venv .venv
source .venv/bin/activate
```

2

Install libraries

```
pip install openai agno
```

3

Set environment variables

```
export MODELS_LAB_API_KEY=****
```

4

Run the agent

```
python video_generation.py
```

---

## reference_agents__agent.md

## [​](#parameters) Parameters

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `model` | `Optional[Model]` | `None` | Model to use for this Agent |
| `name` | `Optional[str]` | `None` | Agent name |
| `agent_id` | `Optional[str]` | `None` | Agent UUID (autogenerated if not set) |
| `agent_data` | `Optional[Dict[str, Any]]` | `None` | Metadata associated with this agent |
| `introduction` | `Optional[str]` | `None` | Agent introduction. This is added to the chat history when a run is started. |
| `user_id` | `Optional[str]` | `None` | ID of the user interacting with this agent |
| `user_data` | `Optional[Dict[str, Any]]` | `None` | Metadata associated with the user interacting with this agent |
| `session_id` | `Optional[str]` | `None` | Session UUID (autogenerated if not set) |
| `session_name` | `Optional[str]` | `None` | Session name |
| `session_state` | `Optional[Dict[str, Any]]` | `None` | Session state (stored in the database to persist across runs) |
| `context` | `Optional[Dict[str, Any]]` | `None` | Context available for tools and prompt functions |
| `add_context` | `bool` | `False` | If True, add the context to the user prompt |
| `resolve_context` | `bool` | `True` | If True, resolve the context (i.e. call any functions in the context) before running the agent |
| `memory` | `Optional[Memory]` | `None` | Agent Memory |
| `add_history_to_messages` | `bool` | `False` | Add chat history to the messages sent to the Model |
| `num_history_runs` | `int` | `3` | Number of historical runs to include in the messages. |
| `search_previous_sessions_history` | `bool` | `False` | Set this to `True` to allow searching through previous sessions. |
| `num_history_sessions` | `int` | `2` | Specify the number of past sessions to include in the search. It's advisable to keep this number to 2 or 3 for now, as a larger number might fill up the context length of the model, potentially leading to performance issues. |
| `knowledge` | `Optional[AgentKnowledge]` | `None` | Agent Knowledge |
| `knowledge_filters` | `Optional[Dict[str, Any]]` | `None` | Knowledge filters to apply to the knowledge base |
| `enable_agentic_knowledge_filters` | `bool` | `False` | Enable agentic knowledge filters |
| `add_references` | `bool` | `False` | Enable RAG by adding references from AgentKnowledge to the user prompt |
| `retriever` | `Optional[Callable[..., Optional[List[Dict]]]]` | `None` | Function to get references to add to the user\_message |
| `references_format` | `Literal["json", "yaml"]` | `"json"` | Format of the references |
| `storage` | `Optional[AgentStorage]` | `None` | Agent Storage |
| `extra_data` | `Optional[Dict[str, Any]]` | `None` | Extra data stored with this agent |
| `tools` | `Optional[List[Union[Toolkit, Callable, Function]]]` | `None` | A list of tools provided to the Model |
| `show_tool_calls` | `bool` | `False` | Show tool calls in Agent response |
| `tool_call_limit` | `Optional[int]` | `None` | Maximum number of tool calls allowed for a single run |
| `tool_choice` | `Optional[Union[str, Dict[str, Any]]]` | `None` | Controls which (if any) tool is called by the model |
| `reasoning` | `bool` | `False` | Enable reasoning by working through the problem step by step |
| `reasoning_model` | `Optional[Model]` | `None` | Model to use for reasoning |
| `reasoning_agent` | `Optional[Agent]` | `None` | Agent to use for reasoning |
| `reasoning_min_steps` | `int` | `1` | Minimum number of reasoning steps |
| `reasoning_max_steps` | `int` | `10` | Maximum number of reasoning steps |
| `read_chat_history` | `bool` | `False` | Add a tool that allows the Model to read the chat history |
| `search_knowledge` | `bool` | `True` | Add a tool that allows the Model to search the knowledge base |
| `update_knowledge` | `bool` | `False` | Add a tool that allows the Model to update the knowledge base |
| `read_tool_call_history` | `bool` | `False` | Add a tool that allows the Model to get the tool call history |
| `system_message` | `Optional[Union[str, Callable, Message]]` | `None` | Provide the system message as a string or function. This overrides `description`, `goal`, `instructions`, etc. and sends the provided system message as-is. |
| `system_message_role` | `str` | `"system"` | Role for the system message |
| `create_default_system_message` | `bool` | `True` | If True, create a default system message using agent settings |
| `description` | `Optional[str]` | `None` | A description of the Agent that is added to the start of the system message |
| `goal` | `Optional[str]` | `None` | The goal of this task |
| `success_criteria` | `Optional[str]` | `None` | Success criteria for the agent |
| `instructions` | `Optional[Union[str, List[str], Callable]]` | `None` | List of instructions for the agent |
| `expected_output` | `Optional[str]` | `None` | Provide the expected output from the Agent |
| `additional_context` | `Optional[str]` | `None` | Additional context added to the end of the system message |
| `markdown` | `bool` | `False` | If markdown=true, add instructions to format the output using markdown |
| `add_name_to_instructions` | `bool` | `False` | If True, add the agent name to the instructions |
| `add_datetime_to_instructions` | `bool` | `False` | If True, add the current datetime to the system message |
| `add_location_to_instructions` | `bool` | `False` | If True, add the current location to the system message |
| `add_state_in_messages` | `bool` | `False` | If True, add the session state variables in messages |
| `add_messages` | `Optional[List[Union[Dict, Message]]]` | `None` | A list of extra messages added after the system message |
| `user_message` | `Optional[Union[List, Dict, str, Callable, Message]]` | `None` | Provide the user message |
| `user_message_role` | `str` | `"user"` | Role for the user message |
| `create_default_user_message` | `bool` | `True` | If True, create a default user message |
| `retries` | `int` | `0` | Number of retries to attempt |
| `delay_between_retries` | `int` | `1` | Delay between retries |
| `exponential_backoff` | `bool` | `False` | If True, the delay between retries is doubled each time |
| `response_model` | `Optional[Type[BaseModel]]` | `None` | Provide a response model to get the response as a Pydantic model |
| `parse_response` | `bool` | `True` | If True, the response is converted into the response\_model |
| `use_json_mode` | `bool` | `False` | If `response_model` is set, sets the response "mode" of the model, i.e. if the model should explicitly respond with a JSON object instead of a Pydantic model |
| `parser_model` | `Optional[Model]` | `None` | Model to use for parsing the response |
| `parser_model_prompt` | `Optional[str]` | `None` | Prompt to use for parsing the response |
| `save_response_to_file` | `Optional[str]` | `None` | Save the response to a file |
| `stream` | `Optional[bool]` | `None` | Stream the response from the Agent |
| `stream_intermediate_steps` | `bool` | `False` | Stream the intermediate steps from the Agent |
| `store_events` | `bool` | `False` | Store the streaming events on the RunResponse |
| `events_to_skip` | `Optional[List[RunEvent]]` | `None` | Specify which event types to skip when storing events on the RunResponse |
| `team` | `Optional[List[Agent]]` | `None` | The team of agents that this agent can transfer tasks to |
| `team_data` | `Optional[Dict[str, Any]]` | `None` | Data shared between team members |
| `role` | `Optional[str]` | `None` | If this Agent is part of a team, this is the role of the agent |
| `respond_directly` | `bool` | `False` | If True, member agent responds directly to user |
| `add_transfer_instructions` | `bool` | `True` | Add instructions for transferring tasks to team members |
| `team_response_separator` | `str` | `"\n"` | Separator between responses from the team |
| `debug_mode` | `bool` | `False` | Enable debug logs |
| `monitoring` | `bool` | `False` | Log Agent information to agno.com for monitoring |
| `telemetry` | `bool` | `True` | Log minimal telemetry for analytics |

## [​](#functions) Functions

### [​](#print-response) `print_response`

Run the agent and print the response.
**Parameters:**

* `message` (Optional[Union[List, Dict, str, Message]]): The message to send to the agent
* `session_id` (Optional[str]): Session ID to use
* `user_id` (Optional[str]): User ID to use
* `messages` (Optional[List[Union[Dict, Message]]]): List of additional messages to use
* `audio` (Optional[Sequence[Audio]]): Audio files to include
* `images` (Optional[Sequence[Image]]): Image files to include
* `videos` (Optional[Sequence[Video]]): Video files to include
* `files` (Optional[Sequence[File]]): Files to include
* `stream` (Optional[bool]): Whether to stream the response
* `stream_intermediate_steps` (bool): Whether to stream intermediate steps
* `markdown` (bool): Whether to format output as markdown
* `show_message` (bool): Whether to show the message
* `show_reasoning` (bool): Whether to show reasoning
* `show_full_reasoning` (bool): Whether to show full reasoning
* `console` (Optional[Any]): Console to use for output
* `knowledge_filters` (Optional[Dict[str, Any]]): Knowledge filters to apply

### [​](#run) `run`

Run the agent.
**Parameters:**

* `message` (Optional[Union[str, List, Dict, Message]]): The message to send to the agent
* `stream` (Optional[bool]): Whether to stream the response
* `user_id` (Optional[str]): User ID to use
* `session_id` (Optional[str]): Session ID to use
* `audio` (Optional[Sequence[Audio]]): Audio files to include
* `images` (Optional[Sequence[Image]]): Image files to include
* `videos` (Optional[Sequence[Video]]): Video files to include
* `files` (Optional[Sequence[File]]): Files to include
* `messages` (Optional[Sequence[Union[Dict, Message]]]): List of additional messages to use
* `stream_intermediate_steps` (Optional[bool]): Whether to stream intermediate steps
* `retries` (Optional[int]): Number of retries to attempt
* `knowledge_filters` (Optional[Dict[str, Any]]): Knowledge filters to apply

**Returns:**

* `Union[RunResponse, Iterator[RunResponseEvent]]`: Either a RunResponse or an iterator of RunResponseEvents, depending on the `stream` parameter

### [​](#aprint-response) `aprint_response`

Run the agent and print the response asynchronously.
**Parameters:**

* `message` (Optional[Union[List, Dict, str, Message]]): The message to send to the agent
* `session_id` (Optional[str]): Session ID to use
* `user_id` (Optional[str]): User ID to use
* `messages` (Optional[List[Union[Dict, Message]]]): List of additional messages to use
* `audio` (Optional[Sequence[Audio]]): Audio files to include
* `images` (Optional[Sequence[Image]]): Image files to include
* `videos` (Optional[Sequence[Video]]): Video files to include
* `files` (Optional[Sequence[File]]): Files to include
* `stream` (Optional[bool]): Whether to stream the response
* `stream_intermediate_steps` (bool): Whether to stream intermediate steps
* `markdown` (bool): Whether to format output as markdown
* `show_message` (bool): Whether to show the message
* `show_reasoning` (bool): Whether to show reasoning
* `show_full_reasoning` (bool): Whether to show full reasoning
* `console` (Optional[Any]): Console to use for output
* `knowledge_filters` (Optional[Dict[str, Any]]): Knowledge filters to apply

### [​](#arun) `arun`

Run the agent asynchronously.
**Parameters:**

* `message` (Optional[Union[str, List, Dict, Message]]): The message to send to the agent
* `stream` (Optional[bool]): Whether to stream the response
* `user_id` (Optional[str]): User ID to use
* `session_id` (Optional[str]): Session ID to use
* `audio` (Optional[Sequence[Audio]]): Audio files to include
* `images` (Optional[Sequence[Image]]): Image files to include
* `videos` (Optional[Sequence[Video]]): Video files to include
* `files` (Optional[Sequence[File]]): Files to include
* `messages` (Optional[Sequence[Union[Dict, Message]]]): List of additional messages to use
* `stream_intermediate_steps` (Optional[bool]): Whether to stream intermediate steps
* `retries` (Optional[int]): Number of retries to attempt
* `knowledge_filters` (Optional[Dict[str, Any]]): Knowledge filters to apply

**Returns:**

* `Union[RunResponse, AsyncIterator[RunResponseEvent]]`: Either a RunResponse or an iterator of RunResponseEvents, depending on the `stream` parameter

### [​](#continue-run) `continue_run`

Continue a run.
**Parameters:**

* `run_response` (Optional[RunResponse]): The run response to continue
* `run_id` (Optional[str]): The run ID to continue
* `updated_tools` (Optional[List[ToolExecution]]): Updated tools to use, required if the run is resumed using `run_id`
* `stream` (Optional[bool]): Whether to stream the response
* `stream_intermediate_steps` (Optional[bool]): Whether to stream intermediate steps
* `user_id` (Optional[str]): User ID to use
* `session_id` (Optional[str]): Session ID to use
* `retries` (Optional[int]): Number of retries to attempt
* `knowledge_filters` (Optional[Dict[str, Any]]): Knowledge filters to apply

**Returns:**

* `Union[RunResponse, Iterator[RunResponseEvent]]`: Either a RunResponse or an iterator of RunResponseEvents, depending on the `stream` parameter

### [​](#acontinue-run) `acontinue_run`

Continue a run asynchronously.
**Parameters:**

* `run_response` (Optional[RunResponse]): The run response to continue
* `run_id` (Optional[str]): The run ID to continue
* `updated_tools` (Optional[List[ToolExecution]]): Updated tools to use, required if the run is resumed using `run_id`
* `stream` (Optional[bool]): Whether to stream the response
* `stream_intermediate_steps` (Optional[bool]): Whether to stream intermediate steps
* `user_id` (Optional[str]): User ID to use
* `session_id` (Optional[str]): Session ID to use
* `retries` (Optional[int]): Number of retries to attempt
* `knowledge_filters` (Optional[Dict[str, Any]]): Knowledge filters to apply

**Returns:**

* `Union[RunResponse, AsyncIterator[RunResponseEvent]]`: Either a RunResponse or an iterator of RunResponseEvents, depending on the `stream` parameter

### [​](#get-session-summary) get\_session\_summary

Get the session summary for the given session ID and user ID.
**Parameters:**

* `session_id` (Optional[str]): Session ID to use (if not provided, the current session is used)
* `user_id` (Optional[str]): User ID to use (if not provided, the current user is used)

**Returns:**

* `Optional[SessionSummary]`: The session summary

### [​](#get-user-memories) get\_user\_memories

Get the user memories for the given user ID.
**Parameters:**

* `user_id` (Optional[str]): User ID to use (if not provided, the current user is used)

**Returns:**

* `Optional[List[UserMemory]]`: The user memories

### [​](#add-tool) add\_tool

Add a tool to the agent.
**Parameters:**

* `tool` (Union[Toolkit, Callable, Function, Dict]): The tool to add

### [​](#set-tools) set\_tools

Replace the tools of the agent.
**Parameters:**

* `tools` (List[Union[Toolkit, Callable, Function, Dict]]): The tools to set

---

## reference_document-reader__document-reader.md


```
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



---

## reference_embedders__embedder.md


```
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



---

## reference_knowledge__knowledge.md


```
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



---

## reference_memory__memory.md

Memory is a class that manages conversation history, session summaries, and long-term user memories for AI agents. It provides comprehensive memory management capabilities including adding new memories, searching memories, and deleting memories.

### [​](#parameters) Parameters

| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| `model` | `Optional[Model]` | Model used for memories and summaries | `None` |
| `memory_manager` | `Optional[MemoryManager]` | Manager for memory operations | `None` |
| `summarizer` | `Optional[SessionSummarizer]` | Summarizer for generating session summaries | `None` |
| `db` | `Optional[MemoryDb]` | Database for storing memories | `None` |
| `debug_mode` | `bool` | Whether to enable debug logging | `False` |

### [​](#key-methods) Key Methods

#### [​](#user-memory-management) User Memory Management

| Method | Description | Parameters | Returns |
| --- | --- | --- | --- |
| `get_user_memories` | Retrieves all memories for a user | `user_id: str` | `List[UserMemory]` |
| `get_user_memory` | Gets a specific memory | `user_id: str, memory_id: str` | `UserMemory` |
| `add_user_memory` | Adds a new memory and gets the memory id | `memory: UserMemory, user_id: Optional[str] = None` | `str` |
| `replace_user_memory` | Updates an existing memory and gets the memory id | `memory_id: str, memory: UserMemory, user_id: Optional[str] = None` | `str` |
| `delete_user_memory` | Deletes a memory | `user_id: str, memory_id: str` | `None` |
| `create_user_memories` | Creates memories from one or more messages | `message: Optional[str] = None, messages: Optional[List[Message]] = None, user_id: Optional[str] = None` | `str` |
| `acreate_user_memories` | Creates memories from one or more messages (Async) | `message: Optional[str] = None, messages: Optional[List[Message]] = None, user_id: Optional[str] = None` | `str` |
| `search_user_memories` | Searches user memories using specified retrieval method | `query: Optional[str] = None, limit: Optional[int] = None, retrieval_method: Optional[Literal["last_n", "first_n", "semantic"]] = None, user_id: Optional[str] = None` | `List[UserMemory]` |

#### [​](#session-summary-management) Session Summary Management

| Method | Description | Parameters |
| --- | --- | --- |
| `get_session_summaries` | Retrieves all session summaries for a user | `user_id: str` |
| `get_session_summary` | Gets a specific session summary | `user_id: str, session_id: str` |
| `create_session_summary` | Creates a summary for a session from the stored session runs | `session_id: str, user_id: Optional[str] = None` |
| `acreate_session_summary` | Creates a summary for a session from the stored session runs (Async) | `session_id: str, user_id: Optional[str] = None` |
| `delete_session_summary` | Deletes a session summary | `user_id: str, session_id: str` |

### [​](#usermemory) UserMemory

| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| `memory` | `str` | The actual memory content | Required |
| `topics` | `Optional[List[str]]` | Topics or categories of the memory | `None` |
| `input` | `Optional[str]` | Original input that generated the memory | `None` |
| `last_updated` | `Optional[datetime]` | When the memory was last updated | `None` |
| `memory_id` | `Optional[str]` | Unique identifier for the memory | `None` |

### [​](#sessionsummary) SessionSummary

| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| `summary` | `str` | Concise summary of the session | Required |
| `topics` | `Optional[List[str]]` | Topics discussed in the session | `None` |
| `last_updated` | `Optional[datetime]` | When the summary was last updated | `None` |

### [​](#memory-manager) Memory Manager

| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| `model` | `Optional[Model]` | Model used for managing memories | `None` |
| `system_message` | `Optional[str]` | Custom system prompt for the memory manager | `None` |
| `additional_instructions` | `Optional[str]` | Additional instructions added to the end of the system message | `None` |

### [​](#session-summarizer) Session Summarizer

| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| `model` | `Optional[Model]` | Model used for summarizing sessions | `None` |
| `system_message` | `Optional[str]` | Custom system prompt for the summarizer | `None` |
| `additional_instructions` | `Optional[str]` | Additional instructions added to the end of the system message | `None` |

---

## reference_models__model.md

The Model class is the base class for all models in Agno. It provides common functionality and parameters that are inherited by specific model implementations like OpenAIChat, Claude, etc.

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `id` | `str` | - | ID of the model to use. |
| `name` | `Optional[str]` | `None` | Name for this Model. Not sent to the Model API. |
| `provider` | `Optional[str]` | `None` | Provider for this Model. Not sent to the Model API. |
| `supports_native_structured_outputs` | `bool` | `False` | Whether the model supports structured outputs natively (e.g. OpenAI). |
| `supports_json_schema_outputs` | `bool` | `False` | Whether the model requires a json\_schema for structured outputs (e.g. LMStudio). |
| `system_prompt` | `Optional[str]` | `None` | System prompt from the model added to the Agent. |
| `instructions` | `Optional[List[str]]` | `None` | Instructions from the model added to the Agent. |
| `tool_message_role` | `str` | `"tool"` | The role of the tool message. |
| `assistant_message_role` | `str` | `"assistant"` | The role of the assistant message. |
| `session_id` | `Optional[str]` | `None` | Session ID of the calling Agent or Workflow. |
| `structured_outputs` | `Optional[bool]` | `None` | Whether to use the structured outputs with this Model. |
| `override_system_role` | `bool` |  |  |

---

## reference_rerankers__reranker.md


```
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



---

## reference_storage__storage.md


```
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



---

## reference_teams__team.md

## [​](#parameters) Parameters

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `members` | `List[Union[Agent, Team]]` | - | List of agents or teams that make up this team |
| `mode` | `Literal["route", "coordinate", "collaborate"]` | `"coordinate"` | Team operating mode |
| `model` | `Optional[Model]` | `None` | Model to use for the team |
| `name` | `Optional[str]` | `None` | Name of the team |
| `team_id` | `Optional[str] | `None` | Team UUID (autogenerated if not set) |
| `parent_team_id` | `Optional[str]` | `None` | If this team is part of a team itself, this is the role of the team |
| `workflow_id` | `Optional[str]` | `None` | The workflow this team belongs to |
| `role` | `Optional[str]` | `None` | Role of the team within its parent team |
| `user_id` | `Optional[str]` | `None` | ID of the user interacting with this team |
| `session_id` | `Optional[str]` | `None` | Session UUID (autogenerated if not set) |
| `team_session_id` | `Optional[str]` | `None` | In the case where the team is a member of a team itself |
| `session_name` | `Optional[str]` | `None` | Session name |
| `session_state` | `Optional[Dict[str, Any]]` | `None` | Session state (stored in the database to persist across runs) |
| `team_session_state` | `Optional[Dict[str, Any]]` | `None` | Team session state (shared between team leaders and team members) |
| `add_state_in_messages` | `bool` | `False` | If True, add the session state variables in the user and system messages |
| `description` | `Optional[str]` | `None` | A description of the team that is added to the start of the system message |
| `instructions` | `Optional[Union[str, List[str], Callable]]` | `None` | List of instructions for the team |
| `expected_output` | `Optional[str]` | `None` | Provide the expected output from the team |
| `additional_context` | `Optional[str]` | `None` | Additional context added to the end of the system message |
| `success_criteria` | `Optional[str]` | `None` | Define the success criteria for the team |
| `markdown` | `bool` | `False` | If markdown=true, add instructions to format the output using markdown |
| `add_datetime_to_instructions` | `bool` | `False` | If True, add the current datetime to the instructions to give the team a sense of time |
| `add_location_to_instructions` | `bool` | `False` | If True, add the current location to the instructions to give the team a sense of location |
| `add_member_tools_to_system_message` | `bool` | `True` | If True, add the tools available to team members to the system message |
| `knowledge` | `Optional[AgentKnowledge]` | `None` | Add a knowledge base to the team |
| `knowledge_filters` | `Optional[Dict[str, Any]]` | `None` | Filters to apply to knowledge base searches |
| `enable_agentic_knowledge_filters` | `Optional[bool]` | `False` | Let the agent choose the knowledge filters |
| `retriever` | `Optional[Callable[..., Optional[List[Dict]]]]` | `None` | Custom retrieval function to get references |
| `references_format` | `Literal["json", "yaml"]` | `"json"` | Format of the references |
| `context` | `Optional[Dict[str, Any]]` | `None` | User provided context |
| `add_context` | `bool` | `False` | If True, add the context to the user prompt |
| `enable_agentic_context` | `bool` | `False` | If True, enable the team agent to update the team context and automatically send the team context to the members |
| `share_member_interactions` | `bool` | `False` | If True, send all previous member interactions to members |
| `get_member_information_tool` | `bool` | `False` | If True, add a tool to get information about the team members |
| `search_knowledge` | `bool` | `True` | Add a tool to search the knowledge base (aka Agentic RAG) |
| `read_team_history` | `bool` | `False` | If True, read the team history |
| `tools` | `Optional[List[Union[Toolkit, Callable, Function, Dict]]]` | `None` | A list of tools provided to the Model |
| `show_tool_calls` | `bool` | `True` | Show tool calls in Team response |
| `tool_call_limit` | `Optional[int]` | `None` | Maximum number of tool calls allowed |
| `tool_choice` | `Optional[Union[str, Dict[str, Any]]]` | `None` | Controls which (if any) tool is called by the team model |
| `tool_hooks` | `Optional[List[Callable]]` | `None` | A list of hooks to be called before and after the tool call |
| `response_model` | `Optional[Type[BaseModel]]` | `None` | Response model for the team response |
| `parser_model` | `Optional[Model]` | `None` | Model to use for parsing the response |
| `parser_model_prompt` | `Optional[str]` | `None` | Prompt to use for parsing the response |
| `use_json_mode` | `bool` | `False` | If `response_model` is set, sets the response mode of the model |
| `parse_response` | `bool` | `True` | If True, parse the response |
| `memory` | `Optional[Union[TeamMemory, Memory]]` | `None` | Memory for the team |
| `enable_agentic_memory` | `bool` | `False` | Enable the agent to manage memories of the user |
| `enable_user_memories` | `bool` | `False` | If True, the agent creates/updates user memories at the end of runs |
| `add_memory_references` | `Optional[bool]` | `None` | If True, the agent adds a reference to the user memories in the response |
| `enable_session_summaries` | `bool` | `False` | If True, the agent creates/updates session summaries at the end of runs |
| `add_session_summary_references` | `Optional[bool]` | `None` | If True, the agent adds a reference to the session summaries in the response |
| `add_history_to_messages` | `bool` | `False` | If True, add messages from the chat history to the messages list sent to the Model. |
| `num_history_runs` | `int` | `3` | Number of historical runs to include in the messages |
| `storage` | `Optional[Storage]` | `None` | Storage for the team |
| `extra_data` | `Optional[Dict[str, Any]]` | `None` | Extra data stored with this team |
| `reasoning` | `bool` | `False` | Enable reasoning for the team |
| `reasoning_model` | `Optional[Model]` | `None` | Model to use for reasoning |
| `reasoning_min_steps` | `int` | `1` | Minimum number of reasoning steps |
| `reasoning_max_steps` | `int` | `10` | Maximum number of reasoning steps |
| `stream` | `Optional[bool]` | `None` | Stream the response from the Team |
| `stream_intermediate_steps` | `bool` | `False` | Stream the intermediate steps from the Team |
| `stream_member_events` | `bool` | `True` | Stream the member events from the Team members |
| `store_events` | `bool` | `False` | Store the streaming events on the TeamRunResponse |
| `events_to_skip` | `Optional[List[Union[RunEvent, TeamRunEvent]]]` | `None` | Specify which event types to skip when storing events on the TeamRunResponse |
| `app_id` | `Optional[str]` | `None` | Optional app ID. Indicates this team is part of an app |
| `debug_mode` | `bool` | `False` | Enable debug logs |
| `show_members_responses` | `bool` | `False` | Enable member logs - Sets the debug\_mode for team and members |
| `monitoring` | `bool` | `False` | Log team information to agno.com for monitoring |
| `telemetry` | `bool` | `True` | Log minimal telemetry for analytics |

## [​](#functions) Functions

| Function | Description |
| --- | --- |
| `print_response` | Run the team and print the response |
| `run` | Run the team |
| `aprint_response` | Run the team and print the response asynchronously |
| `arun` | Run the team asynchronously |
| `get_session_summary` | Get the session summary for the given session ID and user ID |
| `get_user_memories` | Get the user memories for the given user ID |
| `load_session` | Load an existing session from the database or create a new one |
| `rename_session` | Rename the current session |
| `delete_session` | Delete a session |
| `get_images` | Get all images from the team session |
| `get_videos` | Get all videos from the team session |
| `get_audio` | Get all audio from the team session |
| `add_tool` | Add a tool to the team |
| `set_tools` | Replace the tools of the team |

## [​](#team-modes) Team Modes

The team can operate in three different modes:

1. `"route"` - Routes tasks to specific team members
2. `"coordinate"` - Coordinates between team members (default)
3. `"collaborate"` - Enables collaboration between team members

## [​](#knowledge-base-integration) Knowledge Base Integration

The team supports integration with a knowledge base through the following features:

* `knowledge`: Add a knowledge base to the team
* `knowledge_filters`: Apply filters to knowledge base searches
* `enable_agentic_knowledge_filters`: Let the agent choose the knowledge filters
* `retriever`: Custom retrieval function for references
* `search_knowledge`: Tool to search the knowledge base

## [​](#memory-and-history) Memory and History

The team supports various memory and history features:

* `memory`: Team memory storage
* `enable_agentic_memory`: Enable agent memory management
* `enable_user_memories`: Create/update user memories at the end of runs
* `enable_session_summaries`: Create/update session summaries at the end of runs
* `add_history_to_messages`: Add messages from the chat history to the messages list sent to the Model.
* `num_history_runs`: Number of historical runs to include

## [​](#tools-and-functions) Tools and Functions

The team can be equipped with various tools and functions:

* `tools`: List of tools provided to the model
* `tool_call_limit`: Maximum number of tool calls
* `tool_choice`: Control which tool is called
* `tool_hooks`: Hooks for tool execution

## [​](#reasoning) Reasoning

The team supports reasoning capabilities:

* `reasoning`: Enable reasoning
* `reasoning_model`: Model for reasoning
* `reasoning_min_steps`: Minimum reasoning steps
* `reasoning_max_steps`: Maximum reasoning steps

---

## reference_workflows-v2__workflow-v2.md


```
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



---

## reference_workflows__workflow.md

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `name` | `Optional[str]` | `None` | **Workflow name** |
| `workflow_id` | `Optional[str]` | `None` | **Workflow UUID** (autogenerated if not set) |
| `description` | `Optional[str]` | `None` | **Workflow description** (only shown in the UI) |
| `user_id` | `Optional[str]` | `None` | **ID of the user** interacting with this workflow |
| `session_id` | `Optional[str]` | `None` | **Session UUID** (autogenerated if not set) |
| `session_name` | `Optional[str]` | `None` | **Session name** |
| `session_state` | `Dict[str, Any]` | `{}` (empty dict) | **Session state** stored in the database |
| `memory` | `Optional[WorkflowMemory]` | `None` | **Workflow Memory** |
| `storage` | `Optional[WorkflowStorage]` | `None` | **Workflow Storage** |
| `extra_data` | `Optional[Dict[str, Any]]` | `None` | **Extra data** stored with this workflow |
| `debug_mode` | `bool` | `False` | Enable debug logs |
| `monitoring` | `bool` | `False` (env: `AGNO_MONITOR`) | If `True`, logs Workflow information to agno.com for monitoring. Defaults to `True` if `AGNO_MONITOR="true"` in the environment. |
| `telemetry` | `bool` | `True` (env: `AGNO_TELEMETRY`) | If `True`, logs minimal telemetry for analytics. Defaults to `True` if `AGNO_TELEMETRY="true"` in the environment. |
| `run_id` | `Optional[str]` | `None` | **(Do not set manually)** Unique ID for each Workflow run |
| `run_input` | `Optional[Dict[str, Any]]` | `None` | **(Do not set manually)** Input passed to the current run |
| `run_response` | `Optional[RunResponse]` | `None` | **(Do not set manually)** Response generated by the current run |
| `images` | `Optional[List[ImageArtifact]]` | `None` | **Images generated** during this session |
| `videos` | `Optional[List[VideoArtifact]]` | `None` | **Videos generated** during this session |
| `audio` | `Optional[List[AudioArtifact]]` | `None` | **Audio generated** during this session |

---

## streamlit-apps__streamlit-finance.md


```
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



---

## streamlit-apps__streamlit-multimodal.md


```
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



---

## streamlit-apps__streamlit-research.md


```
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



---

## teams__team-collaboration.md


```
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



---

## teams__team-coordination.md


```
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



---

## teams__team-finance.md


```
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



---

## teams__team-multimodal.md


```
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



---

## teams__team-research.md


```
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



---

## workflows-v2__workflow-v2-finance.md


```
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



---

## workflows-v2__workflow-v2-intro.md


```
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



---

## workflows-v2__workflow-v2-multimodal.md


```
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



---

## workflows-v2__workflow-v2-research.md


```
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



---

## workflows__workflow-basic.md


```
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



---

## workflows__workflow-finance.md


```
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



---

## workflows__workflow-memory.md


```
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



---

## workflows__workflow-multimodal.md


```
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



---

## workflows__workflow-research.md


```
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



---

## workflows__workflow-storage.md


```
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



---

## workflows__workflow-tools.md


```
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



