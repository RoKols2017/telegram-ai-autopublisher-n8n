[Back to README](../README.md) · [Assignment 2 →](assignment-2-full-text-image-workflow.md)

# Assignment 1: Local Text Workflow

## Goal

Build and document a minimal viable workflow that receives a `topic` via webhook, generates a Telegram-ready text with OpenAI, and publishes it through Telegram Bot API.

## What is being verified

- `n8n` runs locally
- webhook accepts `POST`
- JSON payload contains `topic`
- OpenAI node uses that topic to generate a post
- Telegram `sendMessage` publishes the result
- the execution returns HTTP `200`

## Local Docker commands

```bash
docker pull n8nio/n8n:latest
docker volume create n8n_data
docker run -d --name n8n -p 5678:5678 -v n8n_data:/home/node/.n8n n8nio/n8n
docker ps
```

## Workflow schema

```text
Webhook -> OpenAI Message Model -> Telegram sendMessage
```

## Input JSON

```json
{
  "topic": "5 practical ways AI automation saves time in content workflows"
}
```

## Data paths

- Input topic path: `$json.body.topic` or `$json.topic`
- Recommended fallback check in `n8n`: inspect the Webhook node output in `Executions`
- OpenAI text output path: depends on node version, commonly `{{$json.text}}`, `{{$json.output_text}}`, or nested under the model response object

## Telegram sendMessage setup

- Method: `POST`
- URL: `https://api.telegram.org/bot<TELEGRAM_BOT_TOKEN>/sendMessage`
- Body fields:
  - `chat_id`: `<TELEGRAM_CHAT_ID>`
  - `text`: map the generated OpenAI text field
  - `parse_mode`: optional, use `Markdown` only if your prompt avoids broken markup

## Example Python request

```python
import requests

payload = {"topic": "5 practical ways AI automation saves time in content workflows"}
response = requests.post(
    "http://localhost:5678/webhook/telegram-ai-autopublisher",
    json=payload,
    timeout=60,
)

print(response.status_code)
print(response.text)
```

## Expected result

- Status code: `200`
- `n8n` execution: successful
- Telegram channel: one new text post

## Required screenshots

- `screenshots/assignment-1/docker-running.png`
- `screenshots/assignment-1/n8n-workflow-text-only.png`
- `screenshots/assignment-1/execution-success.png`
- `screenshots/assignment-1/telegram-text-post.png`
- `screenshots/assignment-1/status-200-local.png`

## Typical errors

- Wrong JSON path for `topic`
- Wrong OpenAI output field mapping
- Telegram returns `400` because `chat_id` is wrong
- Telegram returns `401` because token is invalid
- Webhook test URL expired after switching from test to production mode

## How to fix JSON paths through Executions

1. Open the latest workflow execution.
2. Inspect the Webhook node output and copy the real path to `topic`.
3. Inspect the OpenAI node output and map the exact response field.
4. Re-run the request and verify the downstream Telegram node input.

## See Also

- [Assignment 2](assignment-2-full-text-image-workflow.md) - Full protected workflow with image generation
- [n8n JSON Paths](n8n-json-paths.md) - Path debugging notes for node expressions
- [Troubleshooting](troubleshooting.md) - Common runtime and mapping failures
