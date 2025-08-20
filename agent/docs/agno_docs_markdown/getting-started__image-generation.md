# Image Generation - Agno

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

Image Generation

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

# Image Generation

Copy page

Copy page

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

Copy

Ask AI

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
python image_generation.py
```

Was this page helpful?

YesNo

[Suggest edits](https://github.com/agno-agi/agno-docs/edit/main/examples/getting-started/image-generation.mdx)[Raise issue](https://github.com/agno-agi/agno-docs/issues/new?title=Issue on docs&body=Path: /examples/getting-started/image-generation)

[Image Agent](/examples/getting-started/image-agent)[Video Generation](/examples/getting-started/video-generation)

[x](https://x.com/AgnoAgi)[github](https://github.com/agno-agi/agno)[discord](https://agno.link/discord)[youtube](https://agno.link/youtube)[website](https://agno.com)

[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=referral&utm_source=agno)

Assistant

Responses are generated using AI and may contain mistakes.