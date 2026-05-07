# telegram-ai-autopublisher-n8n

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

- Assignment 1: `Webhook -> OpenAI Text -> Telegram sendMessage`
- Assignment 2: `Webhook + Bearer Auth -> OpenAI Text -> Image Prompt -> Image Generation -> Telegram sendPhoto`
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
| [Assignment 1](docs/assignment-1-local-text-workflow.md) | Local MVP text-only workflow |
| [Assignment 2](docs/assignment-2-full-text-image-workflow.md) | Full text + image + auth workflow |
| [Architecture](docs/architecture.md) | Application-layer design boundaries |
| [Local Deployment](docs/deployment-local.md) | Local `n8n` run and workflow testing |
| [VPS Deployment](docs/deployment-vps.md) | Import and activate on self-hosted `n8n` |
| [Security](docs/security.md) | Secret hygiene and webhook protection |
| [Telegram API](docs/telegram-api.md) | `sendMessage` and `sendPhoto` usage |
| [n8n JSON Paths](docs/n8n-json-paths.md) | Expression and output mapping notes |
| [Troubleshooting](docs/troubleshooting.md) | Common failures and fixes |
| [Portfolio Case RU](docs/portfolio-case.ru.md) | Russian portfolio framing |
| [Portfolio Case EN](docs/portfolio-case.en.md) | English portfolio framing |

## Security

- No real secrets are stored in this repository.
- All examples use placeholders like `<OPENAI_API_KEY>` and `<TELEGRAM_BOT_TOKEN>`.
- Workflow exports must be sanitized before commit.

## Portfolio Value

This case demonstrates that I can build application-layer AI workflows on top of existing infrastructure, connect LLM outputs to real APIs, design prompts for multi-step generation, validate webhook security, and package the result as a clean technical GitHub case study.
