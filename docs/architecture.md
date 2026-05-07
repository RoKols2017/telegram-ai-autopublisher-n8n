[← Assignment 2](assignment-2-full-text-image-workflow.md) · [Back to README](../README.md) · [Local Deployment →](deployment-local.md)

# Architecture

## Scope split

This repository documents the application workflow layer.

- Infrastructure layer: already provisioned elsewhere
- Application layer: documented here

## Infrastructure layer reference

- Ubuntu/VPS preparation
- Docker runtime
- self-hosted `n8n`
- Redis / PostgreSQL / queue mode
- domain and HTTPS
- backups and monitoring

Those items are intentionally not duplicated here.

## Application workflow layer

```text
Client -> Webhook -> Auth Guard -> LLM Text -> LLM Image Prompt -> Image Generation -> Telegram API
```

## Design decisions

- Separate text generation and image-prompt generation to keep prompt responsibilities narrow.
- Keep webhook auth at the application entry point.
- Store secrets only in `n8n` credentials or external secret storage.
- Export only sanitized workflows to GitHub.

## Components

- Webhook node: receives `POST` JSON
- Auth node: validates `Authorization` header
- OpenAI text node: creates publishable Telegram copy
- Prompt node: converts text intent into image prompt
- OpenAI image node: returns generated image
- Telegram node: posts to channel with caption

## Failure boundaries

- Unauthorized request stops before model usage
- Text generation failures stop image generation
- Telegram publishing failures preserve execution logs for retry diagnosis

## See Also

- [Local Deployment](deployment-local.md) - Local workflow execution setup
- [VPS Deployment](deployment-vps.md) - Production import and activation flow
- [Portfolio Case EN](portfolio-case.en.md) - English portfolio framing of the architecture
