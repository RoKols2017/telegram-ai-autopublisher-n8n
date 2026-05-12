[← Local Deployment](deployment-local.md) · [Back to README](../../README.en.md) · [Security →](security.md)

# VPS Deployment

## Purpose

This document covers workflow import and activation on an already running self-hosted `n8n` instance. It does not repeat VPS bootstrap or infrastructure setup.

## Steps

1. Open the existing `n8n` instance at `<N8N_DOMAIN>`.
2. Import the sanitized workflow export from `workflows/`.
3. Rebind OpenAI and Telegram credentials inside `n8n`.
4. Configure the bearer token for the auth check.
5. Activate the workflow.
6. Test the endpoint with `scripts/test_server_webhook.py`.

## Outcome

- production webhook responds
- auth guard works
- Telegram receives text and image output

## See Also

- [Security](security.md) - secret handling and auth rules
- [Full Workflow](full-workflow.md) - end-to-end logic chain
- [Troubleshooting](troubleshooting.md) - server-side checks
