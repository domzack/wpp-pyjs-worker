# Image Agent - Agno

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

Image Agent

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

# Image Agent

Copy page

Copy page

This example shows how to create an AI agent that can analyze images and connect them with current events using web searches. Perfect for:

1. News reporting and journalism
2. Travel and tourism content
3. Social media analysis
4. Educational presentations
5. Event coverage

Example images to try:

* Famous landmarks (Eiffel Tower, Taj Mahal, etc.)
* City skylines
* Cultural events and festivals
* Breaking news scenes
* Historical locations

## [​](#code) Code

image\_agent.py

Copy

Ask AI

```
from textwrap import dedent

from agno.agent import Agent
from agno.media import Image
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    description=dedent("""\
        You are a world-class visual journalist and cultural correspondent with a gift
        for bringing images to life through storytelling! 📸✨ With the observational skills
        of a detective and the narrative flair of a bestselling author, you transform visual
        analysis into compelling stories that inform and captivate.\
    """),
    instructions=dedent("""\
        When analyzing images and reporting news, follow these principles:

        1. Visual Analysis:
           - Start with an attention-grabbing headline using relevant emoji
           - Break down key visual elements with expert precision
           - Notice subtle details others might miss
           - Connect visual elements to broader contexts

        2. News Integration:
           - Research and verify current events related to the image
           - Connect historical context with present-day significance
           - Prioritize accuracy while maintaining engagement
           - Include relevant statistics or data when available

        3. Storytelling Style:
           - Maintain a professional yet engaging tone
           - Use vivid, descriptive language
           - Include cultural and historical references when relevant
           - End with a memorable sign-off that fits the story

        4. Reporting Guidelines:
           - Keep responses concise but informative (2-3 paragraphs)
           - Balance facts with human interest
           - Maintain journalistic integrity
           - Credit sources when citing specific information

        Transform every image into a compelling news story that informs and inspires!\
    """),
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True,
)

# Example usage with a famous landmark
agent.print_response(
    "Tell me about this image and share the latest relevant news.",
    images=[
        Image(
            url="https://upload.wikimedia.org/wikipedia/commons/0/0c/GoldenGateBridge-001.jpg"
        )
    ],
    stream=True,
)

# More examples to try:
"""
Sample prompts to explore:
1. "What's the historical significance of this location?"
2. "How has this place changed over time?"
3. "What cultural events happen here?"
4. "What's the architectural style and influence?"
5. "What recent developments affect this area?"

Sample image URLs to analyze:
1. Eiffel Tower: "https://upload.wikimedia.org/wikipedia/commons/8/85/Tour_Eiffel_Wikimedia_Commons_%28cropped%29.jpg"
2. Taj Mahal: "https://upload.wikimedia.org/wikipedia/commons/b/bd/Taj_Mahal%2C_Agra%2C_India_edit3.jpg"
3. Golden Gate Bridge: "https://upload.wikimedia.org/wikipedia/commons/0/0c/GoldenGateBridge-001.jpg"
"""

# To get the response in a variable:
# from rich.pretty import pprint
# response = agent.run(
#     "Analyze this landmark's architecture and recent news.",
#     images=[Image(url="YOUR_IMAGE_URL")],
# )
# pprint(response.content)
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
pip install openai duckduckgo-search agno
```

3

Run the agent

Copy

Ask AI

```
python image_agent.py
```

Was this page helpful?

YesNo

[Suggest edits](https://github.com/agno-agi/agno-docs/edit/main/examples/getting-started/image-agent.mdx)[Raise issue](https://github.com/agno-agi/agno-docs/issues/new?title=Issue on docs&body=Path: /examples/getting-started/image-agent)

[Research Workflow](/examples/getting-started/research-workflow)[Image Generation](/examples/getting-started/image-generation)

[x](https://x.com/AgnoAgi)[github](https://github.com/agno-agi/agno)[discord](https://agno.link/discord)[youtube](https://agno.link/youtube)[website](https://agno.com)

[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=referral&utm_source=agno)

Assistant

Responses are generated using AI and may contain mistakes.