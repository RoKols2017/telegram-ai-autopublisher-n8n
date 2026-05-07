[← VPS Deployment](deployment-vps.md) · [Back to README](../README.md) · [Telegram API →](telegram-api.md)

# Security

## Repository rules

- Never commit real OpenAI keys.
- Never commit Telegram bot token.
- Never commit bearer token.
- Never commit real `chat_id`.
- Never commit raw `n8n` credential payloads.
- Never commit internal VPS URLs, cookies, or emails unless explicitly public.

## Placeholder policy

Use only placeholders such as:

- `<OPENAI_API_KEY>`
- `<TELEGRAM_BOT_TOKEN>`
- `<TELEGRAM_CHAT_ID>`
- `<N8N_BEARER_TOKEN>`
- `<SERVER_IP>`
- `<N8N_DOMAIN>`
- `<PRODUCTION_WEBHOOK_URL>`

## Workflow export hygiene

Before commit:

1. export the workflow from `n8n`
2. run `scripts/sanitize_workflow_export.py`
3. manually inspect the sanitized JSON
4. verify credentials, webhook URLs, headers, and sample values are placeholders

## Webhook protection

- require `Authorization: Bearer ...`
- reject missing token with `403`
- do auth checks before OpenAI calls to avoid unnecessary token spend

## Screenshot hygiene

- blur or crop secrets
- hide account email if visible in `n8n`
- hide channel ID if it should remain private

## See Also

- [Telegram API](telegram-api.md) - Downstream Telegram publishing constraints
- [VPS Deployment](deployment-vps.md) - Where auth and activation are applied
- [Assignment 2](assignment-2-full-text-image-workflow.md) - Protected workflow implementation
