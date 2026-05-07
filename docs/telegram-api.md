[← Security](security.md) · [Back to README](../README.md) · [n8n JSON Paths →](n8n-json-paths.md)

# Telegram API Integration

## Supported methods in this project

- `sendMessage` for Assignment 1
- `sendPhoto` for Assignment 2

## sendMessage payload

```json
{
  "chat_id": "<TELEGRAM_CHAT_ID>",
  "text": "Generated post text"
}
```

## sendPhoto payload

```json
{
  "chat_id": "<TELEGRAM_CHAT_ID>",
  "photo": "<GENERATED_IMAGE_URL>",
  "caption": "Generated caption text"
}
```

## Common pitfalls

- bot is not an admin in the channel
- wrong `chat_id`
- invalid token
- caption too long for the chosen message style
- remote image URL expired before Telegram fetched it

## Practical note

If image URLs are short-lived, prefer immediate publish or fetch the binary and pass it through the workflow in the same execution chain.

## See Also

- [n8n JSON Paths](n8n-json-paths.md) - Mapping Telegram request fields from node outputs
- [Troubleshooting](troubleshooting.md) - Telegram delivery failure cases
- [Assignment 1](assignment-1-local-text-workflow.md) - `sendMessage` workflow usage
