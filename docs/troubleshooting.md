[← n8n JSON Paths](n8n-json-paths.md) · [Back to README](../README.md) · [Portfolio Case RU →](portfolio-case.ru.md)

# Troubleshooting

## Webhook returns 404

- check whether you are using test URL or production URL
- confirm workflow is active when using production webhook

## Webhook returns 403

- missing `Authorization` header
- token format does not match `Bearer <N8N_BEARER_TOKEN>`
- auth node compares against the wrong placeholder or env-backed value

## Telegram node fails

- verify bot token
- verify bot has rights in the target channel
- verify `chat_id`

## OpenAI node fails

- invalid API key
- wrong model name
- quota or rate-limit issue
- malformed prompt mapping from previous node

## Wrong output text or empty caption

- inspect the exact OpenAI response path in `Executions`
- normalize output in an intermediate `Set` node if needed

## Image not delivered

- generated URL expired
- Telegram could not fetch the remote file
- prefer binary transfer if remote URL reliability is low

## See Also

- [Security](security.md) - Auth and secret-related failure causes
- [n8n JSON Paths](n8n-json-paths.md) - Output mapping checks during debugging
- [VPS Deployment](deployment-vps.md) - Production execution context
