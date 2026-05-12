[Назад к README](../../README.md) · [Полный Workflow →](full-workflow.md)

# Text-Only MVP Workflow

## Назначение

Этот MVP показывает минимальную рабочую цепочку для AI-публикации в Telegram: входящий webhook, генерация текста через OpenAI и публикация через Telegram Bot API.

## Поток данных

```text
Webhook -> OpenAI Text Generation -> Telegram sendMessage
```

## Входной JSON

```json
{
  "topic": "AI automation for Telegram content workflows"
}
```

## Что проверяет MVP

- `n8n` принимает `POST`-запрос
- поле `topic` доходит до LLM-узла
- OpenAI возвращает Telegram-ready текст
- Telegram получает сообщение через `sendMessage`
- endpoint отвечает `200`

## Практические пути данных

- topic: `$json.body.topic` или `$json.topic`
- текст OpenAI: проверяется по фактическому output узла в `Executions`

## Как тестировать

```bash
python scripts/test_local_webhook.py
```

Или:

```bash
python main.py "AI automation for Telegram content workflows"
```

## Ожидаемый результат

- статус `200`
- успешный execution в `n8n`
- новый текстовый пост в Telegram-канале

## Скриншоты для портфолио

- `screenshots/text-only-mvp/docker-vps-n8n-stack-running.png`
- `screenshots/text-only-mvp/n8n-workflow-text-only.png`
- `screenshots/text-only-mvp/execution-success.png`
- `screenshots/text-only-mvp/telegram-text-post.png`
- `screenshots/text-only-mvp/status-200.png`

## See Also

- [Полный Workflow](full-workflow.md) - версия с auth и генерацией изображения
- [Локальный запуск](deployment-local.md) - локальный запуск и отладка
- [n8n JSON Paths](n8n-json-paths.md) - как проверять реальные output paths
