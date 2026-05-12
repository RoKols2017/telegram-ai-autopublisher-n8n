[← VPS Deployment](deployment-vps.md) · [Назад к README](../../README.md) · [Telegram API →](telegram-api.md)

# Security

## Что не должно попадать в Git

- OpenAI API keys
- Telegram bot token
- bearer token
- реальные `chat_id`
- private URLs
- raw `n8n` credentials

## Placeholder Policy

Используются только значения вида:

- `<OPENAI_API_KEY>`
- `<TELEGRAM_BOT_TOKEN>`
- `<TELEGRAM_CHAT_ID>`
- `<N8N_BEARER_TOKEN>`
- `<PRODUCTION_WEBHOOK_URL>`

## Webhook Protection

- проверяй `Authorization` header до вызовов OpenAI
- не логируй реальные токены в публичные артефакты
- если токен утёк, сразу ротируй его

## Workflow Export Hygiene

```bash
python scripts/sanitize_workflow_export.py input.json output.json
```

## See Also

- [Telegram API](telegram-api.md) - downstream publishing layer
- [Bearer Token PowerShell](bearer-token-powershell.md) - генерация токена для тестов
- [Troubleshooting](troubleshooting.md) - auth и credential failures
