[← Bearer Token PowerShell](bearer-token-powershell.md) · [Back to README](../../README.en.md) · [Portfolio Case →](portfolio-case.md)

# Troubleshooting

## `404` from webhook

- test URL and production URL were mixed up
- workflow is not active

## `403` from webhook

- missing `Authorization` header
- token mismatch
- auth node compares against the wrong value

## Telegram failure

- invalid token
- wrong `chat_id`
- bot lacks channel permissions

## OpenAI failure

- invalid API key
- wrong model name
- quota or rate limit issue

## See Also

- [Security](security.md) - auth and secret handling
- [n8n JSON Paths](n8n-json-paths.md) - mapping failures
- [Local Deployment](deployment-local.md) - local verification before VPS rollout
