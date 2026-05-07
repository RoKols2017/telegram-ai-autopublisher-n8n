[← Local Deployment](deployment-local.md) · [Back to README](../README.md) · [Security →](security.md)

# VPS Deployment

## Purpose

This repository assumes the VPS and self-hosted `n8n` stack already exist. Deployment here means importing and activating the application-layer workflow on top of that runtime.

## Steps

1. Open the existing `n8n` instance on `<N8N_DOMAIN>`.
2. Import `workflows/assignment-2-text-image-auth-workflow.sanitized.json`.
3. Reconfigure credentials with real OpenAI and Telegram values inside `n8n`.
4. Set the expected bearer token in the auth node or environment-backed expression.
5. Activate the workflow and copy the production webhook URL.
6. Test with `scripts/test_server_webhook.py` and `scripts/test_auth_success.py`.

## Keep out of scope

- Ubuntu bootstrap
- Docker installation
- reverse proxy setup
- Redis/PostgreSQL installation

Those belong to the infrastructure repository.

## Deployment outcome

- authenticated external call reaches `n8n`
- text and image are generated
- post appears in Telegram channel

## See Also

- [Security](security.md) - Secret handling and webhook auth rules
- [Assignment 2](assignment-2-full-text-image-workflow.md) - Full protected production-style workflow
- [Troubleshooting](troubleshooting.md) - Failure modes after deployment
