# telegram-ai-autopublisher-n8n

Application-layer AI automation workflow for Telegram content generation, built on top of my self-hosted `n8n`/VPS infrastructure.

## Overview

This repository is a portfolio case study built around two Prompt Engineering 2.0 assignments. Instead of presenting them as homework, it packages them as a production-style engineering workflow:

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
- assignment docs
- prompt files
- test scripts
- security notes
- troubleshooting and evaluation files

## Security Model

- no real API keys
- no Telegram bot token
- no chat ID
- no private webhook URLs
- no raw `n8n` credentials in exported JSON

All sensitive values are represented with placeholders.

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
