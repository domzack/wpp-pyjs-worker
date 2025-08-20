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