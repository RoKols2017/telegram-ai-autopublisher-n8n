[← Assignment 1](assignment-1-local-text-workflow.md) · [Back to README](../README.md) · [Architecture →](architecture.md)

# Assignment 2: Full Text + Image + Auth Workflow

## Goal

Turn the MVP into a production-style application-layer workflow with request authorization, text generation, image-prompt generation, image generation, and Telegram publishing through `sendPhoto`.

## Workflow schema

```text
Webhook -> Auth Check -> OpenAI Text -> Image Prompt Builder -> OpenAI Image -> Telegram sendPhoto
```

## Input contract

```json
{
  "topic": "AI workflow architecture for Telegram content automation",
  "tone": "clear, technical, concise",
  "audience": "founders and developers"
}
```

## Authorization contract

- Header: `Authorization: Bearer <N8N_BEARER_TOKEN>`
- Missing or invalid token: return `403`
- Valid token: continue execution and return `200`

## OpenAI stages

- Stage 1: generate final Telegram post text
- Stage 2: generate a visual prompt derived from the same topic and text intent
- Stage 3: generate an image with the visual prompt

## Telegram publishing

- Use `sendPhoto`
- Send the generated image URL or binary, depending on the selected `n8n` node configuration
- Caption can reuse the generated text or a shorter derivative

## Evidence to collect

- successful execution in `n8n`
- `200` with valid bearer token
- `403` without token
- final Telegram post with image
- VPS `n8n` runtime screenshot

## Required screenshots

- `screenshots/assignment-2/full-workflow-text-image-auth.png`
- `screenshots/assignment-2/execution-success.png`
- `screenshots/assignment-2/telegram-post-with-image.png`
- `screenshots/assignment-2/status-200-with-token.png`
- `screenshots/assignment-2/status-403-without-token.png`
- `screenshots/assignment-2/vps-n8n-running.png`

## Operational notes

- Keep this repository focused on workflow logic, not base VPS provisioning.
- Rebind credentials after importing the sanitized workflow.
- If the image node returns temporary URLs, publish immediately or download and forward binary data in the same execution.

## See Also

- [Architecture](architecture.md) - Application-layer structure and boundaries
- [Security](security.md) - Bearer token and secret handling rules
- [Telegram API](telegram-api.md) - `sendPhoto` integration details
