[← Security](security.md) · [Назад к README](../../README.md) · [n8n JSON Paths →](n8n-json-paths.md)

# Telegram API

## Используемые методы

- `sendMessage` для text-only MVP
- `sendPhoto` для полного workflow с изображением

## Минимальные payload examples

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

## Частые проблемы

- бот не админ в канале
- неверный `chat_id`
- устаревший image URL
- слишком длинный caption

## See Also

- [n8n JSON Paths](n8n-json-paths.md) - как корректно мапить поля
- [Text-Only MVP](text-only-mvp-workflow.md) - использование `sendMessage`
- [Full Workflow](full-workflow.md) - использование `sendPhoto`
