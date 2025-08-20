The Model class is the base class for all models in Agno. It provides common functionality and parameters that are inherited by specific model implementations like OpenAIChat, Claude, etc.

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `id` | `str` | - | ID of the model to use. |
| `name` | `Optional[str]` | `None` | Name for this Model. Not sent to the Model API. |
| `provider` | `Optional[str]` | `None` | Provider for this Model. Not sent to the Model API. |
| `supports_native_structured_outputs` | `bool` | `False` | Whether the model supports structured outputs natively (e.g. OpenAI). |
| `supports_json_schema_outputs` | `bool` | `False` | Whether the model requires a json\_schema for structured outputs (e.g. LMStudio). |
| `system_prompt` | `Optional[str]` | `None` | System prompt from the model added to the Agent. |
| `instructions` | `Optional[List[str]]` | `None` | Instructions from the model added to the Agent. |
| `tool_message_role` | `str` | `"tool"` | The role of the tool message. |
| `assistant_message_role` | `str` | `"assistant"` | The role of the assistant message. |
| `session_id` | `Optional[str]` | `None` | Session ID of the calling Agent or Workflow. |
| `structured_outputs` | `Optional[bool]` | `None` | Whether to use the structured outputs with this Model. |
| `override_system_role` | `bool` |  |  |