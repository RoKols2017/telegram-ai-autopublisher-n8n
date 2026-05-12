[← Local Deployment](deployment-local.md) · [Назад к README](../../README.md) · [Security →](security.md)

# VPS Deployment

## Назначение

Этот документ описывает не создание VPS, а импорт и активацию workflow в уже работающем self-hosted `n8n` окружении.

## Шаги

1. Открой существующий `n8n` на `<N8N_DOMAIN>`.
2. Импортируй sanitized workflow export из `workflows/`.
3. Перепривяжи OpenAI и Telegram credentials внутри `n8n`.
4. Пропиши bearer token для auth-check.
5. Активируй workflow.
6. Проверь endpoint через `scripts/test_server_webhook.py`.

## Результат

- production webhook отвечает
- auth работает
- Telegram получает текст и изображение

## See Also

- [Security](security.md) - требования к секретам и auth
- [Full Workflow](full-workflow.md) - полная logic chain
- [Troubleshooting](troubleshooting.md) - что проверять при ошибках на сервере
