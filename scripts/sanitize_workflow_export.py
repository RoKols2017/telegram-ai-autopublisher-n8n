"""Sanitize n8n workflow exports before committing them to GitHub."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


PLACEHOLDERS = {
    re.compile(r"sk-[A-Za-z0-9_-]+", re.IGNORECASE): "<OPENAI_API_KEY>",
    re.compile(r"\b[0-9]{8,12}:[A-Za-z0-9_-]{20,}\b"): "<TELEGRAM_BOT_TOKEN>",
    re.compile(r"https?://[^\s\"']+"): "<PRODUCTION_WEBHOOK_URL>",
    re.compile(r"Bearer\s+[A-Za-z0-9._-]+", re.IGNORECASE): "Bearer <N8N_BEARER_TOKEN>",
    re.compile(r"-100\d{6,}"): "<TELEGRAM_CHAT_ID>",
}

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
    if isinstance(value, list):
        return [sanitize_value(key, item) for item in value]
    if isinstance(value, str):
        sanitized = value
        for pattern, replacement in PLACEHOLDERS.items():
            sanitized = pattern.sub(replacement, sanitized)
        if key in SENSITIVE_KEYS and sanitized and not sanitized.startswith("<"):
            return f"<{key.upper()}>"
        return sanitized
    if key in SENSITIVE_KEYS and value is not None:
        return f"<{key.upper()}>"
    return value


def main() -> int:
    if len(sys.argv) != 3:
        print("Usage: python scripts/sanitize_workflow_export.py input.json output.json")
        return 1

    source = Path(sys.argv[1])
    target = Path(sys.argv[2])

    data = json.loads(source.read_text(encoding="utf-8"))
    sanitized = sanitize_value("root", data)
    target.write_text(json.dumps(sanitized, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Sanitized workflow written to {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
