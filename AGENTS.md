# AGENTS.md

> Project map for AI agents. Keep this file up-to-date as the project evolves.

## Project Overview

This repository documents an application-layer AI automation workflow built on top of an existing self-hosted `n8n` infrastructure. It packages two Prompt Engineering 2.0 assignments as a portfolio-ready Telegram autopublishing case with sanitized workflow exports, prompts, helper scripts, and documentation.

## Tech Stack

- **Primary Platform:** `n8n`
- **Language:** Python 3
- **Framework:** None
- **Database:** None in repository scope
- **ORM:** None
- **Integrations:** OpenAI API, Telegram Bot API
- **Ops Context:** Docker, Linux VPS, self-hosted `n8n`

## Project Structure

```text
.
|-- .ai-factory/             # AI Factory project metadata and architecture docs
|-- .opencode/               # Local AI skill installation directory
|-- assets/                  # Diagram placeholders for portfolio visuals
|-- docs/                    # Main technical documentation and case-study narrative
|-- evals/                   # Evaluation notes, checklists, failure cases, test topics
|-- notes/                   # Course/lesson summary notes
|-- prompts/                 # Versioned prompt assets separated from workflows
|-- screenshots/             # Screenshot placeholders grouped by assignment
|-- scripts/                 # Python helper scripts for webhook tests and sanitization
|-- workflows/               # Sanitized n8n workflow exports for import into n8n
|-- .ai-factory.json         # Installed AI Factory skills metadata
|-- .env.example             # Placeholder environment variables only
|-- .gitignore               # Local secret and artifact exclusions
|-- AGENTS.md                # This file
|-- LICENSE                  # Repository license
|-- main.py                  # Minimal webhook client for quick manual testing
|-- opencode.json            # Lightweight project metadata for local AI tooling
|-- README.en.md             # English project overview
`-- README.md                # Russian-facing primary landing page
```

## Key Entry Points

| File | Purpose |
|------|---------|
| `README.md` | Main repository landing page and positioning |
| `README.en.md` | English version of the repository overview |
| `main.py` | Minimal manual webhook client for local or VPS tests |
| `workflows/assignment-1-text-only-workflow.sanitized.json` | MVP text-only n8n workflow export |
| `workflows/assignment-2-text-image-auth-workflow.sanitized.json` | Full text + image + auth n8n workflow export |
| `scripts/sanitize_workflow_export.py` | Sanitizes exported workflow JSON before commit |
| `.ai-factory/DESCRIPTION.md` | Project specification and stack summary |

## Documentation

| Document | Path | Description |
|----------|------|-------------|
| README | `README.md` | Project landing page in Russian |
| English README | `README.en.md` | English project landing page |
| Assignment 1 | `docs/assignment-1-local-text-workflow.md` | Local MVP workflow walkthrough |
| Assignment 2 | `docs/assignment-2-full-text-image-workflow.md` | Full protected text+image workflow walkthrough |
| Architecture | `docs/architecture.md` | High-level workflow architecture overview |
| Local Deployment | `docs/deployment-local.md` | Local n8n startup and testing |
| VPS Deployment | `docs/deployment-vps.md` | VPS import and activation steps |
| Security | `docs/security.md` | Secret handling and sanitization rules |
| Telegram API | `docs/telegram-api.md` | Telegram publishing method notes |
| n8n JSON Paths | `docs/n8n-json-paths.md` | Expression mapping and path debugging |
| Troubleshooting | `docs/troubleshooting.md` | Common failure modes and fixes |
| Portfolio Case RU | `docs/portfolio-case.ru.md` | Russian portfolio framing |
| Portfolio Case EN | `docs/portfolio-case.en.md` | English portfolio framing |

## AI Context Files

| File | Purpose |
|------|---------|
| `AGENTS.md` | This file: project structure map and guardrails |
| `.ai-factory/DESCRIPTION.md` | Project specification and tech stack |
| `.ai-factory/ARCHITECTURE.md` | Architecture decisions and implementation boundaries |

## Guardrails

- Never commit real secrets, tokens, chat IDs, private URLs, or VPS-specific internal details.
- Treat every `n8n` workflow export as unsafe until sanitized.
- Keep infrastructure concerns out of this repository unless they are directly needed to explain workflow deployment.
- Prefer small edits and preserve portfolio clarity.

## Scope

- In scope: workflow JSON, prompts, testing scripts, Telegram/OpenAI integration notes, portfolio documentation.
- Out of scope: full Ubuntu hardening, Docker host bootstrap, reverse proxy installation, Redis/PostgreSQL installation guides.

## Validation

- Check placeholder values before publishing.
- Review workflow JSON for credentials, webhook URLs, and internal hostnames.
- Keep screenshots redacted if they contain account names or secrets.

## Agent Rules

- Use only sanitized, placeholder-based examples in committed artifacts.
- Keep repository changes focused on the application workflow layer.
- Do not assume exact `n8n` JSON paths across node versions; verify through execution output.
