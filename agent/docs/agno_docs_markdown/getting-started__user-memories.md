# User Memories - Agno

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

User Memories

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

# User Memories

Copy page

Copy page

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

Copy

Ask AI

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
python user_memories.py
```

Was this page helpful?

YesNo

[Suggest edits](https://github.com/agno-agi/agno-docs/edit/main/examples/getting-started/user-memories.mdx)[Raise issue](https://github.com/agno-agi/agno-docs/issues/new?title=Issue on docs&body=Path: /examples/getting-started/user-memories)

[Agent Session](/examples/getting-started/agent-session)[Retry Functions](/examples/getting-started/retry-functions)

[x](https://x.com/AgnoAgi)[github](https://github.com/agno-agi/agno)[discord](https://agno.link/discord)[youtube](https://agno.link/youtube)[website](https://agno.com)

[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=referral&utm_source=agno)

Assistant

Responses are generated using AI and may contain mistakes.