# Architecture: Layered Architecture

## Overview

This repository uses a lightweight layered architecture adapted for a workflow-first portfolio project rather than a full application service. The goal is to keep artifacts separated by concern: workflow definitions, prompt assets, executable test helpers, and human-facing documentation.

Layered architecture fits this project because the codebase is small, the operational flow is linear, and the main risk is not domain complexity but mixing infrastructure concerns, secrets, and application-layer workflow logic. The structure should stay easy to navigate, easy to publish publicly, and easy to extend with new workflow cases.

## Decision Rationale

- **Project type:** Public portfolio repository for `n8n`-based AI automation workflows
- **Tech stack:** `n8n`, Python 3 helper scripts, OpenAI API, Telegram Bot API
- **Key factor:** Clear separation between documentation, workflow artifacts, prompt assets, and executable test helpers

## Folder Structure

```text
.
|-- .ai-factory/            # AI Factory context and project architecture rules
|-- assets/                 # Static portfolio visuals and diagram placeholders
|-- docs/                   # Explanatory layer: architecture, assignments, security, deployment
|-- evals/                  # Validation layer: expected results, test topics, failure cases
|-- notes/                  # Course-summary notes and learning artifacts
|-- prompts/                # Prompt layer: system prompts and prompt versioning
|-- screenshots/            # Evidence layer: screenshots grouped by assignment
|-- scripts/                # Execution layer: local/VPS webhook tests and workflow sanitizer
|-- workflows/              # Integration layer: sanitized n8n workflow exports
|-- main.py                 # Minimal manual client for webhook smoke testing
|-- README.md               # Primary landing page
`-- README.en.md            # English landing page
```

## Dependency Rules

Artifacts should depend inward on simpler, more stable project layers.

- `README*` and `docs/` may reference `workflows/`, `prompts/`, `scripts/`, `screenshots/`, and `evals/`
- `scripts/` may depend on environment variables and external HTTP APIs, but should not depend on screenshots or notes
- `workflows/` may encode integration logic and prompt references, but should not embed real credentials or infrastructure-specific secrets
- `prompts/` should remain reusable text assets, independent from test evidence and screenshots

- ✅ Documentation can explain workflow behavior implemented in `workflows/` and exercised by `scripts/`
- ✅ Scripts can test webhook endpoints described in docs
- ❌ Scripts should not become a second application runtime that duplicates `n8n` workflow logic
- ❌ Workflow exports should not become a dump of infrastructure setup unrelated to application automation
- ❌ Any layer should not commit real secrets, private URLs, or raw credentials

## Layer Communication

- `External client -> scripts/main.py -> n8n webhook -> OpenAI/Telegram integrations`
- `docs/` communicates architecture and operating instructions to humans
- `workflows/` communicates executable automation logic to `n8n`
- `prompts/` communicates generation constraints to LLM stages
- `evals/` communicates expected outcomes and failure boundaries

## Key Principles

1. Keep infrastructure and application workflow concerns separate.
2. Treat public workflow JSON as publishable artifacts, not as raw internal exports.
3. Keep prompts versioned and inspectable outside the `n8n` editor.
4. Prefer small Python helpers for testing and sanitization instead of building a larger service layer.
5. Preserve portfolio clarity: every file should either explain, test, or implement the workflow case.

## Code Examples

### Minimal webhook test helper

```python
import os

import requests


payload = {"topic": "Telegram AI autopublishing workflow with n8n"}
url = os.getenv("LOCAL_WEBHOOK_URL", "http://localhost:5678/webhook/telegram-ai-autopublisher")

response = requests.post(url, json=payload, timeout=60)
print(response.status_code)
print(response.text)
```

### Sanitization boundary for exported workflows

```python
SENSITIVE_KEYS = {
    "apiKey",
    "token",
    "password",
    "chat_id",
    "chatId",
    "webhookUrl",
    "email",
    "host",
}


def sanitize_value(key: str, value):
    if isinstance(value, dict):
        return {k: sanitize_value(k, v) for k, v in value.items()}
    if isinstance(value, str) and key in SENSITIVE_KEYS and value:
        return f"<{key.upper()}>"
    return value
```

## Anti-Patterns

- ❌ Mixing VPS bootstrap instructions into this repository as if it were the infrastructure source of truth
- ❌ Committing raw `n8n` exports with credentials, private webhook URLs, or real chat IDs
- ❌ Hiding prompt logic only inside screenshots or the `n8n` UI instead of versioning it in `prompts/`
- ❌ Growing `scripts/` into a parallel backend that duplicates the real workflow path
- ❌ Assuming fixed `n8n` JSON paths across node versions without checking real execution output
