[Back to README](../../README.en.md) · [Full Workflow →](full-workflow.md)

# Text-Only MVP Workflow

## Purpose

This MVP demonstrates the minimal working flow for AI-assisted Telegram publishing: inbound webhook, OpenAI text generation, and Telegram Bot API delivery.

## Data Flow

```text
Webhook -> OpenAI Text Generation -> Telegram sendMessage
```

## Input JSON

```json
{
  "topic": "AI automation for Telegram content workflows"
}
```

## What this MVP validates

- `n8n` accepts the `POST` request
- the `topic` field reaches the LLM node
- OpenAI returns Telegram-ready text
- Telegram receives the message through `sendMessage`
- the endpoint returns `200`

## Practical data paths

- topic: `$json.body.topic` or `$json.topic`
- OpenAI text output: confirm the real field in `Executions`

## How to test

```bash
python scripts/test_local_webhook.py
```

Or:

```bash
python main.py "AI automation for Telegram content workflows"
```

## Expected result

- `200` response
- successful `n8n` execution
- new text post in the target Telegram channel

## Portfolio evidence

- `screenshots/text-only-mvp/docker-vps-n8n-stack-running.png`
- `screenshots/text-only-mvp/n8n-workflow-text-only.png`
- `screenshots/text-only-mvp/execution-success.png`
- `screenshots/text-only-mvp/telegram-text-post.png`
- `screenshots/text-only-mvp/status-200.png`

## See Also

- [Full Workflow](full-workflow.md) - protected flow with image generation
- [Local Deployment](deployment-local.md) - local setup and debugging loop
- [n8n JSON Paths](n8n-json-paths.md) - output mapping checks
