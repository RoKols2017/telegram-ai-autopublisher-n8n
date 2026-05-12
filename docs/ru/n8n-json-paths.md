[← Telegram API](telegram-api.md) · [Назад к README](../../README.md) · [Bearer Token PowerShell →](bearer-token-powershell.md)

# n8n JSON Paths

## Типовые входные пути

- `{{$json.topic}}`
- `{{$json.body.topic}}`
- `{{$json.headers.authorization}}`

## Типовые выходные поля

- `{{$json.text}}`
- `{{$json.output_text}}`
- `{{$json.image_prompt}}`
- `{{$json.image_url}}`

## Практический подход

1. Открой `Executions`.
2. Посмотри реальный output узла.
3. Скопируй точный path.
4. Только после этого правь expression в следующем узле.

## See Also

- [Bearer Token PowerShell](bearer-token-powershell.md) - проверка auth-сценариев
- [Troubleshooting](troubleshooting.md) - ошибки из-за неверного mapping
- [Full Workflow](full-workflow.md) - полный контекст передачи данных
