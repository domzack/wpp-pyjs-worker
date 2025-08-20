This example shows how to retry a function call if it fails or you do not like the output. This is useful for:

* Handling temporary failures
* Improving output quality through retries
* Implementing human-in-the-loop validation

## [​](#code) Code

retry\_functions.py

Copy

Ask AI

```
from typing import Iterator

from agno.agent import Agent
from agno.exceptions import RetryAgentRun
from agno.tools import FunctionCall, tool

num_calls = 0


def pre_hook(fc: FunctionCall):
    global num_calls

    print(f"Pre-hook: {fc.function.name}")
    print(f"Arguments: {fc.arguments}")
    num_calls += 1
    if num_calls < 2:
        raise RetryAgentRun(
            "This wasn't interesting enough, please retry with a different argument"
        )


@tool(pre_hook=pre_hook)
def print_something(something: str) -> Iterator[str]:
    print(something)
    yield f"I have printed {something}"


agent = Agent(tools=[print_something], markdown=True)
agent.print_response("Print something interesting", stream=True)
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
python retry_functions.py
```