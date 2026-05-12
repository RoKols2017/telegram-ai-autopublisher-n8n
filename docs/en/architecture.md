[← Full Workflow](full-workflow.md) · [Back to README](../../README.en.md) · [Local Deployment →](deployment-local.md)

# Architecture

## Scope Boundary

This repository documents the application workflow layer only.

In scope:

- `n8n` workflow design
- prompt design
- OpenAI integration
- Telegram publishing
- auth logic
- test helpers
- portfolio documentation

Out of scope:

- Ubuntu hardening
- Docker host bootstrap
- reverse proxy
- Redis / PostgreSQL setup
- full VPS provisioning

## Core Flow

```text
Client -> Webhook -> Auth Guard -> LLM Text -> LLM Image Prompt -> LLM Image -> Telegram API
```

## Design Decisions

- prompts are kept outside workflow JSON in `prompts/`
- workflow exports are committed only in sanitized form
- Python scripts stay thin and support testing, not a separate backend
- infrastructure setup remains in separate repositories

## See Also

- [Local Deployment](deployment-local.md) - local validation path
- [VPS Deployment](deployment-vps.md) - deployment on existing self-hosted `n8n`
- [Portfolio Case](portfolio-case.md) - hiring-oriented framing
