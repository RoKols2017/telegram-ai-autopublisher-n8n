# AGENTS.md

> Project map for AI agents. Keep this file up-to-date as the project evolves.

## Project Overview

This repository documents an application-layer AI automation workflow built on top of an existing self-hosted `n8n` infrastructure. It packages a portfolio-ready Telegram autopublishing MVP with sanitized workflow exports, prompts, helper scripts, and bilingual documentation.

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
|-- docs/                    # Bilingual technical documentation split into ru/ and en/
|-- evals/                   # Evaluation notes, checklists, failure cases, test topics
|-- notes/                   # Internal notes that are not part of the public docs flow
|-- prompts/                 # Versioned prompt assets separated from workflows
|-- screenshots/             # Portfolio screenshots grouped by workflow stage
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
| `workflows/text-only-mvp-workflow.sanitized.json` | Text-only MVP n8n workflow export |
| `workflows/full-text-image-auth-workflow.sanitized.json` | Full text + image + auth workflow export |
| `scripts/sanitize_workflow_export.py` | Sanitizes exported workflow JSON before commit |
| `.ai-factory/DESCRIPTION.md` | Project specification and stack summary |

## Documentation

| Document | Path | Description |
|----------|------|-------------|
| README | `README.md` | Project landing page in Russian |
| English README | `README.en.md` | English project landing page |
| Docs Index | `docs/README.md` | Language selector for docs |
| RU Text-Only MVP | `docs/ru/text-only-mvp-workflow.md` | Minimal text workflow in Russian |
| RU Full Workflow | `docs/ru/full-workflow.md` | Full protected workflow in Russian |
| RU Architecture | `docs/ru/architecture.md` | Architecture overview in Russian |
| RU Local Deployment | `docs/ru/deployment-local.md` | Local setup in Russian |
| RU VPS Deployment | `docs/ru/deployment-vps.md` | VPS activation in Russian |
| RU Security | `docs/ru/security.md` | Security rules in Russian |
| RU Telegram API | `docs/ru/telegram-api.md` | Telegram publishing in Russian |
| RU JSON Paths | `docs/ru/n8n-json-paths.md` | n8n path notes in Russian |
| RU PowerShell Token | `docs/ru/bearer-token-powershell.md` | Token guide in Russian |
| RU Troubleshooting | `docs/ru/troubleshooting.md` | Failure cases in Russian |
| RU Portfolio Case | `docs/ru/portfolio-case.md` | Portfolio framing in Russian |
| EN Text-Only MVP | `docs/en/text-only-mvp-workflow.md` | Minimal text workflow in English |
| EN Full Workflow | `docs/en/full-workflow.md` | Full protected workflow in English |
| EN Architecture | `docs/en/architecture.md` | Architecture overview in English |
| EN Local Deployment | `docs/en/deployment-local.md` | Local setup in English |
| EN VPS Deployment | `docs/en/deployment-vps.md` | VPS activation in English |
| EN Security | `docs/en/security.md` | Security rules in English |
| EN Telegram API | `docs/en/telegram-api.md` | Telegram publishing in English |
| EN JSON Paths | `docs/en/n8n-json-paths.md` | n8n path notes in English |
| EN PowerShell Token | `docs/en/bearer-token-powershell.md` | Token guide in English |
| EN Troubleshooting | `docs/en/troubleshooting.md` | Failure cases in English |
| EN Portfolio Case | `docs/en/portfolio-case.md` | Portfolio framing in English |

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
