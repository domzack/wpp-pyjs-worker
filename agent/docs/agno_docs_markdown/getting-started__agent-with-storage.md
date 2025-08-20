# Agent with Storage - Agno

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

Agent with Storage

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

* [Code](#code)
* [Usage](#usage)

Getting Started

# Agent with Storage

Copy page

Copy page

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

Copy

Ask AI

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

Mac

Windows

Copy

Ask AI

```
python3 -m venv .venv
source .venv/bin/activate
```

2

Install libraries

Copy

Ask AI

```
pip install openai lancedb tantivy pypdf duckduckgo-search sqlalchemy agno
```

3

Run the agent

Copy

Ask AI

```
python agent_with_storage.py
```

Was this page helpful?

YesNo

[Suggest edits](https://github.com/agno-agi/agno-docs/edit/main/examples/getting-started/agent-with-storage.mdx)[Raise issue](https://github.com/agno-agi/agno-docs/issues/new?title=Issue on docs&body=Path: /examples/getting-started/agent-with-storage)

[Agent with Knowledge](/examples/getting-started/agent-with-knowledge)[Agent Team](/examples/getting-started/agent-team)

[x](https://x.com/AgnoAgi)[github](https://github.com/agno-agi/agno)[discord](https://agno.link/discord)[youtube](https://agno.link/youtube)[website](https://agno.com)

[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=referral&utm_source=agno)

Assistant

Responses are generated using AI and may contain mistakes.