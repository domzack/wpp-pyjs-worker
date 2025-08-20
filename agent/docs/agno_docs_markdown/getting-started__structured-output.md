# Structured Output - Agno

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

Structured Output

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

# Structured Output

Copy page

Copy page

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

Copy

Ask AI

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
python structured_output.py
```

Was this page helpful?

YesNo

[Suggest edits](https://github.com/agno-agi/agno-docs/edit/main/examples/getting-started/structured-output.mdx)[Raise issue](https://github.com/agno-agi/agno-docs/issues/new?title=Issue on docs&body=Path: /examples/getting-started/structured-output)

[Agent Team](/examples/getting-started/agent-team)[Custom Tools](/examples/getting-started/custom-tools)

[x](https://x.com/AgnoAgi)[github](https://github.com/agno-agi/agno)[discord](https://agno.link/discord)[youtube](https://agno.link/youtube)[website](https://agno.com)

[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=referral&utm_source=agno)

Assistant

Responses are generated using AI and may contain mistakes.