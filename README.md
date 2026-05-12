# telegram-ai-autopublisher-n8n

> Application-layer AI automation workflow for Telegram content generation, built on top of self-hosted `n8n`/VPS infrastructure.

Production-style `n8n` workflow for AI-generated Telegram posts with OpenAI text/image generation, Telegram Bot API publishing, Bearer-token webhook auth and Docker/VPS deployment.

English version: [README.en.md](README.en.md)

## Что это

`telegram-ai-autopublisher-n8n` — portfolio-ready application-layer проект поверх уже развернутой self-hosted `n8n` инфраструктуры на VPS. Репозиторий показывает не установку сервера, а инженерную сборку workflow: защищённый webhook, генерация текста и изображения через OpenAI, публикация в Telegram-канал и тестирование через Python.

## Позиционирование кейса

- AI Automation Specialist
- LLM Workflow Engineer
- Prompt Engineer
- n8n / Low-code Automation Engineer
- Telegram Bot API Integrator
- Docker / VPS practitioner
- Engineer who separates infrastructure layer from application workflow layer

## Key Features

- `n8n` webhook workflow for inbound content requests
- OpenAI text generation for Telegram-ready posts
- separate image prompt generation and image generation stages
- Telegram Bot API publishing via `sendMessage` and `sendPhoto`
- Bearer-token webhook protection for production-style access control
- sanitized workflow exports and Python test helpers for public GitHub publishing

## Архитектура

```text
External Client / Python Script
        |
        v
n8n Webhook + Authorization Header
        |
        v
OpenAI Text Generation
        |
        v
OpenAI Image Prompt Generation
        |
        v
OpenAI Image Generation
        |
        v
Telegram Bot API sendPhoto
        |
        v
Telegram Channel
```

Infrastructure layer already exists in separate repositories and notes. This repository focuses only on workflow architecture, prompt design, integration logic, testing, security hygiene, and portfolio packaging.

## Repository Scope

- Text-Only MVP: `Webhook -> OpenAI Text -> Telegram sendMessage`
- Full Workflow: `Webhook + Bearer Auth -> OpenAI Text -> Image Prompt -> Image Generation -> Telegram sendPhoto`
- Sanitized `n8n` workflow exports
- Testing scripts for local and server webhooks
- Security and troubleshooting docs

## Quick Start

1. Copy `.env.example` values into your local shell or secret manager.
2. Import one of the sanitized workflows from `workflows/` into `n8n`.
3. Rebind credentials inside `n8n` using real OpenAI and Telegram credentials.
4. Run a local or VPS webhook test with `python main.py "your topic"`.

## Local n8n Commands

```bash
docker pull n8nio/n8n:latest
docker volume create n8n_data
docker run -d --name n8n -p 5678:5678 -v n8n_data:/home/node/.n8n n8nio/n8n
docker ps
```

## Documentation

| Guide | Description |
|-------|-------------|
| [Docs Index](docs/README.md) | Language selector for full documentation |
| [RU: Text-Only MVP](docs/ru/text-only-mvp-workflow.md) | Minimal text publishing workflow |
| [RU: Full Workflow](docs/ru/full-workflow.md) | Protected text + image workflow |
| [RU: Architecture](docs/ru/architecture.md) | Application-layer boundaries |
| [RU: Local Deployment](docs/ru/deployment-local.md) | Local `n8n` run and testing |
| [RU: VPS Deployment](docs/ru/deployment-vps.md) | Import into existing self-hosted `n8n` |
| [RU: Security](docs/ru/security.md) | Secret hygiene and auth rules |
| [RU: Telegram API](docs/ru/telegram-api.md) | Publishing method details |
| [RU: JSON Paths](docs/ru/n8n-json-paths.md) | Expression mapping notes |
| [RU: PowerShell Token](docs/ru/bearer-token-powershell.md) | Bearer token generation guide |
| [RU: Troubleshooting](docs/ru/troubleshooting.md) | Common runtime failures |
| [RU: Portfolio Case](docs/ru/portfolio-case.md) | Russian portfolio framing |
| [EN: Text-Only MVP](docs/en/text-only-mvp-workflow.md) | Minimal text publishing workflow |
| [EN: Full Workflow](docs/en/full-workflow.md) | Protected text + image workflow |
| [EN: Architecture](docs/en/architecture.md) | Application-layer boundaries |
| [EN: Local Deployment](docs/en/deployment-local.md) | Local `n8n` run and testing |
| [EN: VPS Deployment](docs/en/deployment-vps.md) | Import into existing self-hosted `n8n` |
| [EN: Security](docs/en/security.md) | Secret hygiene and auth rules |
| [EN: Telegram API](docs/en/telegram-api.md) | Publishing method details |
| [EN: JSON Paths](docs/en/n8n-json-paths.md) | Expression mapping notes |
| [EN: PowerShell Token](docs/en/bearer-token-powershell.md) | Bearer token generation guide |
| [EN: Troubleshooting](docs/en/troubleshooting.md) | Common runtime failures |
| [EN: Portfolio Case](docs/en/portfolio-case.md) | English portfolio framing |

## Security

- No real secrets are stored in this repository.
- All examples use placeholders like `<OPENAI_API_KEY>` and `<TELEGRAM_BOT_TOKEN>`.
- Workflow exports must be sanitized before commit.

## Portfolio Value

This case demonstrates that I can build application-layer AI workflows on top of existing infrastructure, connect LLM outputs to real APIs, design prompts for multi-step generation, validate webhook security, and package the result as a clean technical GitHub case study.
