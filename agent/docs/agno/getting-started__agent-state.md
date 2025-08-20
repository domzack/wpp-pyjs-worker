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