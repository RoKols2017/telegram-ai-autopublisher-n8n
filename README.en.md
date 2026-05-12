# telegram-ai-autopublisher-n8n

> Application-layer AI automation workflow for Telegram content generation, built on top of my self-hosted `n8n`/VPS infrastructure.

## Overview

This repository is a portfolio MVP for a production-style AI publishing workflow:

- inbound request to `n8n` webhook
- OpenAI text generation
- separate image-prompt generation step
- image generation step
- Telegram Bot API publishing
- Bearer-token authorization
- testing and operational documentation

## Why this repository exists

The infrastructure layer already exists elsewhere. I already have a self-hosted `n8n` setup on a Linux VPS with a connected domain. This repository intentionally focuses on the application workflow layer:

- workflow design
- prompt design
- OpenAI integration
- Telegram publishing
- binary transfer handling
- webhook protection
- testing and evaluation
- portfolio packaging

## Core Architecture

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

## Included Deliverables

- bilingual repository overview
- sanitized workflow JSON exports
- bilingual documentation sets
- prompt files
- test scripts
- security notes
- troubleshooting and evaluation files

## Key Features

- inbound `n8n` webhook for content requests
- OpenAI text generation for Telegram-ready posts
- separate image-prompt generation and image generation stages
- Telegram Bot API publishing via `sendMessage` and `sendPhoto`
- Bearer-token authorization for protected webhook access
- sanitized public workflow exports and helper scripts for reproducible testing

## Security Model

- no real API keys
- no Telegram bot token
- no chat ID
- no private webhook URLs
- no raw `n8n` credentials in exported JSON

All sensitive values are represented with placeholders.

## Documentation

| Guide | Description |
|-------|-------------|
| [Docs Index](docs/README.md) | Language selector for full documentation |
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
| [EN: Portfolio Case](docs/en/portfolio-case.md) | Hiring-oriented repository framing |
| [RU Docs](docs/ru/text-only-mvp-workflow.md) | Russian documentation set |

## Suggested Topics

- `n8n`
- `openai`
- `telegram-bot`
- `telegram-api`
- `automation`
- `ai-automation`
- `llm`
- `prompt-engineering`
- `docker`
- `vps`
- `webhook`
- `low-code`
- `workflow-automation`
- `api-integration`
- `portfolio-project`
