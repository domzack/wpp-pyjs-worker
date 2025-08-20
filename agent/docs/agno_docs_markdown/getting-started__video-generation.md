# Video Generation - Agno

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

Video Generation

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

# Video Generation

Copy page

Copy page

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

Copy

Ask AI

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

Set environment variables

Copy

Ask AI

```
export MODELS_LAB_API_KEY=****
```

4

Run the agent

Copy

Ask AI

```
python video_generation.py
```

Was this page helpful?

YesNo

[Suggest edits](https://github.com/agno-agi/agno-docs/edit/main/examples/getting-started/video-generation.mdx)[Raise issue](https://github.com/agno-agi/agno-docs/issues/new?title=Issue on docs&body=Path: /examples/getting-started/video-generation)

[Image Generation](/examples/getting-started/image-generation)[Audio Agent](/examples/getting-started/audio-agent)

[x](https://x.com/AgnoAgi)[github](https://github.com/agno-agi/agno)[discord](https://agno.link/discord)[youtube](https://agno.link/youtube)[website](https://agno.com)

[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=referral&utm_source=agno)

Assistant

Responses are generated using AI and may contain mistakes.