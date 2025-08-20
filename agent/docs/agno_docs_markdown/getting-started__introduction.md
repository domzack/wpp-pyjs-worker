# Introduction - Agno

[Agno home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/black.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/agno/logo/white.svg)](/)

Search...

⌘KAsk AI

* [Discord](https://agno.link/discord)
* [Community](https://community.agno.com/)
* [agno-agi/agno](https://github.com/agno-agi/agno)
* [agno-agi/agno](https://github.com/agno-agi/agno)

Search...

Navigation

Getting Started

Introduction

[User Guide](/introduction)[Examples](/examples/introduction)[Workspaces](/workspaces/introduction)[FAQs](/faq/environment-variables)[API reference](/reference/agents/agent)[Changelog](/changelog/overview)

##### Examples

* [Examples](/examples/introduction)
* Getting Started

  + [Introduction](/examples/getting-started/introduction)
  + [Basic Agent](/examples/getting-started/basic-agent)
  + [Agent with Tools](/examples/getting-started/agent-with-tools)
  + [Agent with Knowledge](/examples/getting-started/agent-with-knowledge)
  + [Agent with Storage](/examples/getting-started/agent-with-storage)
  + [Agent Team](/examples/getting-started/agent-team)
  + [Structured Output](/examples/getting-started/structured-output)
  + [Custom Tools](/examples/getting-started/custom-tools)
  + [Research Agent](/examples/getting-started/research-agent)
  + [Research Workflow](/examples/getting-started/research-workflow)
  + [Image Agent](/examples/getting-started/image-agent)
  + [Image Generation](/examples/getting-started/image-generation)
  + [Video Generation](/examples/getting-started/video-generation)
  + [Audio Agent](/examples/getting-started/audio-agent)
  + [Agent State](/examples/getting-started/agent-state)
  + [Agent Context](/examples/getting-started/agent-context)
  + [Agent Session](/examples/getting-started/agent-session)
  + [User Memories](/examples/getting-started/user-memories)
  + [Retry Functions](/examples/getting-started/retry-functions)
  + [Human in the Loop](/examples/getting-started/human-in-the-loop)
* Agents
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

* [Setup](#setup)
* [Examples](#examples)

Getting Started

# Introduction

Copy page

Copy page

This guide walks through the basics of building Agents with Agno.
The examples build on each other, introducing new concepts and capabilities progressively. Each example contains detailed comments, example prompts, and required dependencies.

## [​](#setup) Setup

Create a virtual environment:

Copy

Ask AI

```
python3 -m venv .venv
source .venv/bin/activate
```

Install the required dependencies:

Copy

Ask AI

```
pip install openai duckduckgo-search yfinance lancedb tantivy pypdf requests exa-py newspaper4k lxml_html_clean sqlalchemy agno
```

Export your OpenAI API key:

Copy

Ask AI

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

Was this page helpful?

YesNo

[Suggest edits](https://github.com/agno-agi/agno-docs/edit/main/examples/getting-started/introduction.mdx)[Raise issue](https://github.com/agno-agi/agno-docs/issues/new?title=Issue on docs&body=Path: /examples/getting-started/introduction)

[Examples](/examples/introduction)[Basic Agent](/examples/getting-started/basic-agent)

[x](https://x.com/AgnoAgi)[github](https://github.com/agno-agi/agno)[discord](https://agno.link/discord)[youtube](https://agno.link/youtube)[website](https://agno.com)

[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=referral&utm_source=agno)

Assistant

Responses are generated using AI and may contain mistakes.