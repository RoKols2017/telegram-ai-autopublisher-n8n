# Project: telegram-ai-autopublisher-n8n

## Overview

Public portfolio repository for an application-layer AI automation workflow built on top of an existing self-hosted `n8n` infrastructure. The project packages two Prompt Engineering 2.0 assignments as a production-style Telegram autopublishing case with OpenAI text and image generation, webhook authorization, testing scripts, and portfolio documentation.

## Core Features

- Webhook-driven `n8n` workflow for Telegram post generation
- OpenAI text generation for Telegram-ready content
- Separate image-prompt generation stage for image model input
- OpenAI image generation and Telegram `sendPhoto` publishing
- Bearer-token authorization for protected webhook access
- Sanitized `n8n` workflow exports for safe public GitHub publishing
- Python `requests` scripts for local and VPS testing
- Bilingual documentation for technical and portfolio audiences

## Tech Stack

- **Primary Platform:** `n8n`
- **Language:** Python 3 for helper scripts
- **Framework:** No application framework; workflow-first automation project
- **Database:** None in repository scope
- **ORM:** None
- **Integrations:** OpenAI API, Telegram Bot API
- **Runtime / Ops Context:** Docker, Linux VPS, self-hosted `n8n`

## Architecture Notes

- This repository documents the application workflow layer only.
- Infrastructure concerns such as Ubuntu hardening, Docker host setup, reverse proxy, Redis, PostgreSQL, and HTTPS termination are intentionally out of scope and handled in separate infrastructure repositories.
- Prompts are stored separately from workflow exports to make prompt iteration and review easier.
- Public artifacts must remain sanitized and placeholder-based.

## Architecture

See `.ai-factory/ARCHITECTURE.md` for detailed architecture guidelines.
Pattern: Layered Architecture

## Non-Functional Requirements

- Logging: rely on `n8n` executions and HTTP responses for workflow-level debugging
- Error handling: reject unauthorized requests before any OpenAI call; capture node-level failures through `n8n` execution logs
- Security: no real secrets in Git; workflow exports must be sanitized before commit
- Documentation: repository should remain portfolio-ready, concise, and bilingual where useful
