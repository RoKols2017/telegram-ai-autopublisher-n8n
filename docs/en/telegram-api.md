[← Security](security.md) · [Back to README](../../README.en.md) · [n8n JSON Paths →](n8n-json-paths.md)

# Telegram API

## Methods used in this repository

- `sendMessage` for the text-only MVP
- `sendPhoto` for the full workflow with image output

## Minimal payload examples

```json
{
  "chat_id": "<TELEGRAM_CHAT_ID>",
  "text": "Generated post text"
}
```

```json
{
  "chat_id": "<TELEGRAM_CHAT_ID>",
  "photo": "<GENERATED_IMAGE_URL>",
  "caption": "Generated caption text"
}
```

## Common issues

- bot is not an admin in the channel
- wrong `chat_id`
- expired image URL
- caption too long for the chosen format

## See Also

- [n8n JSON Paths](n8n-json-paths.md) - field mapping checks
- [Text-Only MVP](text-only-mvp-workflow.md) - `sendMessage` usage
- [Full Workflow](full-workflow.md) - `sendPhoto` usage
