[← Full Workflow](full-workflow.md) · [Назад к README](../../README.md) · [Local Deployment →](deployment-local.md)

# Architecture

## Scope Boundary

Этот репозиторий описывает только application workflow layer.

Внутри scope:

- `n8n` workflow design
- prompt design
- OpenAI integration
- Telegram publishing
- auth logic
- testing scripts
- portfolio documentation

Вне scope:

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

- prompts вынесены из workflow JSON в `prompts/`
- workflow exports хранятся только в sanitized виде
- Python scripts используются как thin test helpers, а не как отдельный backend
- инфраструктурный слой не дублируется в этом репозитории

## See Also

- [Local Deployment](deployment-local.md) - локальный контур для отладки
- [VPS Deployment](deployment-vps.md) - запуск поверх существующего self-hosted `n8n`
- [Portfolio Case](portfolio-case.md) - как этот MVP позиционируется в GitHub
