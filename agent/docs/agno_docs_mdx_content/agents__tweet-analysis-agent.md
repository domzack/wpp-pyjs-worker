Key capabilities:

* Real-time tweet analysis and sentiment classification
* Engagement metrics analysis (likes, retweets, replies)
* Brand health monitoring and competitive intelligence
* Strategic recommendations and response strategies

## [​](#code) Code

social\_media\_agent.py

Copy

Ask AI

```
from textwrap import dedent

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.x import XTools

social_media_agent = Agent(
    name="Social Media Analyst",
    model=OpenAIChat(id="gpt-4o"),
    tools=[
        XTools(
            include_post_metrics=True,
            wait_on_rate_limit=True,
        )
    ],
    instructions=dedent("""\
        You are a senior Brand Intelligence Analyst specializing in social media 
        listening on X (Twitter). 
        Your mission: Transform raw tweet content and engagement metrics into 
        executive-ready intelligence reports.

        Core Analysis Steps:
        1. Data Collection
           - Retrieve tweets using X tools
           - Analyze text content and engagement metrics
           - Focus on likes, retweets, replies, and reach

        2. Sentiment Classification
           - Classify each tweet: Positive/Negative/Neutral/Mixed
           - Identify reasoning (feature praise, bug complaints, etc.)
           - Weight by engagement volume and author influence

        3. Pattern Detection
           - Viral advocacy (high likes & retweets, low replies)
           - Controversy signals (low likes, high replies)
           - Influencer impact and verified account activity

        4. Thematic Analysis
           - Extract recurring keywords and themes
           - Identify feature feedback and pain points
           - Track competitor mentions and comparisons
           - Spot emerging use cases

        Report Format:
        - Executive summary with brand health score (1-10)
        - Key themes with representative quotes
        - Risk analysis and opportunity identification
        - Strategic recommendations (immediate/short-term/long-term)
        - Response playbook for high-impact posts

        Guidelines:
        - Be objective and evidence-backed
        - Focus on actionable insights
        - Highlight urgent issues requiring attention
        - Provide solution-oriented recommendations"""),
    markdown=True,
    show_tool_calls=True,
)

social_media_agent.print_response(
    "Analyze the sentiment of Agno and AgnoAGI on X (Twitter) for past 10 tweets"
)
```

Check out the detailed [Social Media Agent](https://github.com/agno-agi/agno/blob/main/cookbook/examples/agents/social_media_agent.py).

More prompts to try:

* “Analyze sentiment around our brand on X for the past 10 tweets”
* “Monitor competitor mentions and compare sentiment vs our brand”
* “Generate a brand health report from recent social media activity”
* “Identify trending topics and user sentiment about our product”
* “Create a social media intelligence report for executive review”

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

Set your API key

Copy

Ask AI

```
export OPENAI_API_KEY=****
```

3

Set your X credentials

Copy

Ask AI

```
export X_CONSUMER_KEY=****
export X_CONSUMER_SECRET=****
export X_ACCESS_TOKEN=****
export X_ACCESS_TOKEN_SECRET=****
export X_BEARER_TOKEN=****
```

4

Install libraries

Copy

Ask AI

```
pip install openai tweepy agno
```

5

Run the agent

Copy

Ask AI

```
python social_media_agent.py
```