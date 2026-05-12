[← Bearer Token PowerShell](bearer-token-powershell.md) · [Назад к README](../../README.md) · [Portfolio Case →](portfolio-case.md)

# Troubleshooting

## `404` на webhook

- перепутан test URL и production URL
- workflow не активирован

## `403` на webhook

- не передан `Authorization` header
- token mismatch
- auth node сравнивает не то значение

## Ошибка Telegram

- неверный token
- неверный `chat_id`
- у бота нет прав в канале

## Ошибка OpenAI

- неверный API key
- неправильная модель
- quota или rate limit

## See Also

- [Security](security.md) - auth и secrets
- [n8n JSON Paths](n8n-json-paths.md) - mapping ошибок
- [Local Deployment](deployment-local.md) - локальная проверка перед VPS
