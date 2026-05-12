[← Architecture](architecture.md) · [Назад к README](../../README.md) · [VPS Deployment →](deployment-vps.md)

# Local Deployment

## Когда использовать

Локальный запуск нужен для быстрой проверки JSON paths, prompt iteration и smoke tests до выкладки workflow на VPS.

## Команды

```bash
docker pull n8nio/n8n:latest
docker volume create n8n_data
docker run -d --name n8n -p 5678:5678 -v n8n_data:/home/node/.n8n n8nio/n8n
docker ps
```

## Локальный checklist

- UI доступен на `http://localhost:5678`
- workflow импортирован
- credentials в `n8n` привязаны локально
- webhook test URL отвечает

## See Also

- [Text-Only MVP](text-only-mvp-workflow.md) - минимальный workflow для локального теста
- [n8n JSON Paths](n8n-json-paths.md) - отладка выражений
- [Troubleshooting](troubleshooting.md) - типовые локальные сбои
