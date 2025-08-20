# Agent Session - Agno

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

Agent Session

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

# Agent Session

Copy page

Copy page

This example shows how to create an agent with persistent memory stored in a SQLite database. We set the session\_id on the agent when resuming the conversation, this way the previous chat history is preserved.
Key features:

* Stores conversation history in a SQLite database
* Continues conversations across multiple sessions
* References previous context in responses

## [​](#code) Code

agent\_session.py

Copy

Ask AI

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
pip install openai sqlalchemy agno
```

3

Run the agent

Copy

Ask AI

```
python agent_session.py
```

Was this page helpful?

YesNo

[Suggest edits](https://github.com/agno-agi/agno-docs/edit/main/examples/getting-started/agent-session.mdx)[Raise issue](https://github.com/agno-agi/agno-docs/issues/new?title=Issue on docs&body=Path: /examples/getting-started/agent-session)

[Agent Context](/examples/getting-started/agent-context)[User Memories](/examples/getting-started/user-memories)

[x](https://x.com/AgnoAgi)[github](https://github.com/agno-agi/agno)[discord](https://agno.link/discord)[youtube](https://agno.link/youtube)[website](https://agno.com)

[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=referral&utm_source=agno)

Assistant

Responses are generated using AI and may contain mistakes.