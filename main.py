"""Minimal webhook client for local or VPS n8n testing."""

from __future__ import annotations

import json
import os
import sys

import requests


def main() -> int:
    webhook_url = os.getenv("PRODUCTION_WEBHOOK_URL") or os.getenv("LOCAL_WEBHOOK_URL")
    bearer_token = os.getenv("N8N_BEARER_TOKEN", "")
    topic = " ".join(sys.argv[1:]).strip() or "AI automation for Telegram channel"

    if not webhook_url:
        print("Set LOCAL_WEBHOOK_URL or PRODUCTION_WEBHOOK_URL first.")
        return 1

    headers = {"Content-Type": "application/json"}
    if bearer_token:
        headers["Authorization"] = f"Bearer {bearer_token}"

    payload = {"topic": topic}
    response = requests.post(webhook_url, headers=headers, json=payload, timeout=60)

    print(f"status={response.status_code}")
    try:
        print(json.dumps(response.json(), indent=2, ensure_ascii=False))
    except ValueError:
        print(response.text)

    return 0 if response.ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
