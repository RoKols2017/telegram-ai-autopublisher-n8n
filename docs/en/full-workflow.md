[← Text-Only MVP](text-only-mvp-workflow.md) · [Back to README](../../README.en.md) · [Architecture →](architecture.md)

# Full Workflow

## Purpose

The full workflow presents the production-style application layer built on top of an existing self-hosted `n8n` runtime: protected webhook, text generation, image-prompt generation, image generation, and Telegram publishing.

## Data Flow

```text
Webhook -> Auth Check -> OpenAI Text -> Image Prompt -> OpenAI Image -> Telegram sendPhoto
```

## Input contract

```json
{
  "topic": "AI workflow architecture for Telegram content automation",
  "tone": "clear, technical, concise",
  "audience": "founders and developers"
}
```

## Authorization

- header: `Authorization: Bearer <N8N_BEARER_TOKEN>`
- valid token: `200`
- missing or invalid token: `403`

## What this workflow demonstrates

- separate text generation and image-prompt generation
- auth validation before expensive model calls
- Telegram publishing through `sendPhoto`
- public GitHub-safe workflow exports with placeholders only

## Expected artifacts

- successful `n8n` execution
- Telegram post with generated image
- successful authorized request
- rejected unauthorized request

## Portfolio evidence

- `screenshots/full-workflow/full-workflow-text-image-auth.png`
- `screenshots/full-workflow/execution-success.png`
- `screenshots/full-workflow/telegram-post-with-image.png`
- `screenshots/full-workflow/status-200-with-token.png`
- `screenshots/full-workflow/status-403-without-token.png`
- `screenshots/full-workflow/vps-n8n-running.png`

## See Also

- [Architecture](architecture.md) - application-layer boundaries
- [Security](security.md) - token and secret handling
- [Telegram API](telegram-api.md) - `sendPhoto` and `sendMessage`
