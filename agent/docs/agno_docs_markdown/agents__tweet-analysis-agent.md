# Tweet Analysis Agent - Agno

[Agno home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/black.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/white.svg)](/)

Search...

⌘KAsk AI

* [Discord](https://agno.link/discord)
* [Community](https://community.agno.com/)
* [agno-agi/agno](https://github.com/agno-agi/agno)
* [agno-agi/agno](https://github.com/agno-agi/agno)

Search...

Navigation

Agents

Tweet Analysis Agent

[User Guide](/introduction)[Examples](/examples/introduction)[Workspaces](/workspaces/introduction)[FAQs](/faq/environment-variables)[API reference](/reference/agents/agent)[Changelog](/changelog/overview)

##### Examples

* [Examples](/examples/introduction)
* Getting Started
* Agents

  + [Finance Agent](/examples/agents/finance-agent)
  + [Tweet Analysis Agent](/examples/agents/tweet-analysis-agent)
  + [Youtube Agent](/examples/agents/youtube-agent)
  + [Research Agent](/examples/agents/research-agent)
  + [Research Agent using Exa](/examples/agents/research-agent-exa)
  + [Teaching Assistant](/examples/agents/teaching-assistant)
  + [Recipe Creator](/examples/agents/recipe-creator)
  + [Movie Recommender](/examples/agents/movie-recommender)
  + [Books Recommender](/examples/agents/books-recommender)
  + [Travel Agent](/examples/agents/travel-planner)
  + [Startup Analyst Agent](/examples/agents/startup-analyst-agent)
* Teams
* Workflows
* Workflows v2 (Beta)
* Applications
* Streamlit Apps
* Evals

##### Agent Concepts

* Reasoning
* Multimodal
* RAG
* User Control Flows
* Knowledge
* Memory
* Async
* Hybrid Search
* Storage
* Tools
* Vector Databases
* Context
* Embedders
* Agent State
* Observability
* Testing
* Miscellaneous

##### Models

* Anthropic
* AWS Bedrock
* AWS Bedrock Claude
* Azure AI Foundry
* Azure OpenAI
* Cerebras
* Cerebras OpenAI
* Cohere
* DashScope
* DeepInfra
* DeepSeek
* Fireworks
* Gemini
* Groq
* Hugging Face
* IBM
* LangDB
* LM Studio
* LiteLLM
* LiteLLM OpenAI
* Meta
* Mistral
* Nebius
* NVIDIA
* Ollama
* OpenAI
* Perplexity
* Portkey
* Together
* XAI
* Vercel
* vLLM

On this page

* [Code](#code)
* [Usage](#usage)

Agents

# Tweet Analysis Agent

Copy page

An agent that analyzes tweets and provides comprehensive brand monitoring and sentiment analysis.

Copy page

Key capabilities:

* Real-time tweet analysis and sentiment classification
* Engagement metrics analysis (likes, retweets, replies)
* Brand health monitoring and competitive intelligence
* Strategic recommendations and response strategies

## [​](#code) Code

social\_media\_agent.py

Copy

Ask AI

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

Mac

Windows

Copy

Ask AI

```
python3 -m venv .venv
source .venv/bin/activate
```

2

Set your API key

Copy

Ask AI

```
export OPENAI_API_KEY=****
```

3

Set your X credentials

Copy

Ask AI

```
export X_CONSUMER_KEY=****
export X_CONSUMER_SECRET=****
export X_ACCESS_TOKEN=****
export X_ACCESS_TOKEN_SECRET=****
export X_BEARER_TOKEN=****
```

4

Install libraries

Copy

Ask AI

```
pip install openai tweepy agno
```

5

Run the agent

Copy

Ask AI

```
python social_media_agent.py
```

Was this page helpful?

YesNo

[Suggest edits](https://github.com/agno-agi/agno-docs/edit/main/examples/agents/tweet-analysis-agent.mdx)[Raise issue](https://github.com/agno-agi/agno-docs/issues/new?title=Issue on docs&body=Path: /examples/agents/tweet-analysis-agent)

[Finance Agent](/examples/agents/finance-agent)[Youtube Agent](/examples/agents/youtube-agent)

[x](https://x.com/AgnoAgi)[github](https://github.com/agno-agi/agno)[discord](https://agno.link/discord)[youtube](https://agno.link/youtube)[website](https://agno.com)

[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=referral&utm_source=agno)

Assistant

Responses are generated using AI and may contain mistakes.