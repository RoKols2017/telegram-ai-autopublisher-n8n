[← Text-Only MVP](text-only-mvp-workflow.md) · [Назад к README](../../README.md) · [Architecture →](architecture.md)

# Full Workflow

## Назначение

Полный workflow показывает production-style application layer поверх уже существующей self-hosted `n8n` инфраструктуры: защищённый webhook, генерацию текста, генерацию image prompt, генерацию изображения и публикацию в Telegram.

## Поток данных

```text
Webhook -> Auth Check -> OpenAI Text -> Image Prompt -> OpenAI Image -> Telegram sendPhoto
```

## Входной контракт

```json
{
  "topic": "AI workflow architecture for Telegram content automation",
  "tone": "clear, technical, concise",
  "audience": "founders and developers"
}
```

## Authorization

- заголовок: `Authorization: Bearer <N8N_BEARER_TOKEN>`
- корректный токен: `200`
- отсутствующий или неверный токен: `403`

## Что показывает этот workflow

- разделение text generation и image prompt generation
- раннюю auth-проверку до затратных LLM вызовов
- публикацию в Telegram через `sendPhoto`
- пригодный для GitHub публичный workflow export без секретов

## Ожидаемые артефакты

- успешный execution в `n8n`
- пост в Telegram с изображением
- успешный запрос с токеном
- отклонённый запрос без токена

## Скриншоты для портфолио

- `screenshots/full-workflow/full-workflow-text-image-auth.png`
- `screenshots/full-workflow/execution-success.png`
- `screenshots/full-workflow/telegram-post-with-image.png`
- `screenshots/full-workflow/status-200-with-token.png`
- `screenshots/full-workflow/status-403-without-token.png`
- `screenshots/full-workflow/vps-n8n-running.png`

## See Also

- [Architecture](architecture.md) - границы application-layer решения
- [Security](security.md) - правила по bearer token и secret hygiene
- [Telegram API](telegram-api.md) - `sendPhoto` и `sendMessage`
