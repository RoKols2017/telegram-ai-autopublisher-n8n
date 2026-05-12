[← VPS Deployment](deployment-vps.md) · [Back to README](../../README.en.md) · [Telegram API →](telegram-api.md)

# Security

## What must never enter Git

- OpenAI API keys
- Telegram bot token
- bearer token
- real `chat_id` values
- private URLs
- raw `n8n` credentials

## Placeholder Policy

Use placeholders only:

- `<OPENAI_API_KEY>`
- `<TELEGRAM_BOT_TOKEN>`
- `<TELEGRAM_CHAT_ID>`
- `<N8N_BEARER_TOKEN>`
- `<PRODUCTION_WEBHOOK_URL>`

## Webhook Protection

- validate `Authorization` before OpenAI calls
- never expose real tokens in public artifacts
- rotate the token immediately if it leaks

## Workflow Export Hygiene

```bash
python scripts/sanitize_workflow_export.py input.json output.json
```

## See Also

- [Telegram API](telegram-api.md) - downstream publishing layer
- [Bearer Token PowerShell](bearer-token-powershell.md) - token generation for tests
- [Troubleshooting](troubleshooting.md) - auth and credential failures
