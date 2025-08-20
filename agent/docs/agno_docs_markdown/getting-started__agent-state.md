# Agent State - Agno

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

Agent State

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

# Agent State

Copy page

Copy page

This example shows how to create an agent that maintains state across interactions. It demonstrates a simple counter mechanism, but this pattern can be extended to more complex state management like maintaining conversation context, user preferences, or tracking multi-step processes.
Example prompts to try:

* “Increment the counter 3 times and tell me the final count”
* “What’s our current count? Add 2 more to it”
* “Let’s increment the counter 5 times, but tell me each step”
* “Add 4 to our count and remind me where we started”
* “Increase the counter twice and summarize our journey”

## [​](#code) Code

agent\_state.py

Copy

Ask AI

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
pip install openai agno
```

3

Run the agent

Copy

Ask AI

```
python agent_state.py
```

Was this page helpful?

YesNo

[Suggest edits](https://github.com/agno-agi/agno-docs/edit/main/examples/getting-started/agent-state.mdx)[Raise issue](https://github.com/agno-agi/agno-docs/issues/new?title=Issue on docs&body=Path: /examples/getting-started/agent-state)

[Audio Agent](/examples/getting-started/audio-agent)[Agent Context](/examples/getting-started/agent-context)

[x](https://x.com/AgnoAgi)[github](https://github.com/agno-agi/agno)[discord](https://agno.link/discord)[youtube](https://agno.link/youtube)[website](https://agno.com)

[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=referral&utm_source=agno)

Assistant

Responses are generated using AI and may contain mistakes.