# Генерация `N8N_BEARER_TOKEN` в PowerShell

Короткая инструкция для создания токена авторизации webhook в n8n.

## PowerShell 7+

```powershell
$token = [Convert]::ToHexString([System.Security.Cryptography.RandomNumberGenerator]::GetBytes(32)).ToLower()
$env:N8N_BEARER_TOKEN = $token

Write-Host "Token for .env / PowerShell:"
Write-Host $token

Write-Host "`nValue for n8n Auth Check:"
Write-Host "Bearer $token"
```

## Windows PowerShell 5.1

Если команда выше не работает, используй совместимый вариант:

```powershell
$bytes = New-Object byte[] 32
[System.Security.Cryptography.RandomNumberGenerator]::Create().GetBytes($bytes)
$token = -join ($bytes | ForEach-Object { $_.ToString("x2") })
$env:N8N_BEARER_TOKEN = $token

Write-Host "Token:"
Write-Host $token

Write-Host "`nValue for n8n Auth Check:"
Write-Host "Bearer $token"
```

## Как использовать

В переменную окружения или `.env` сохраняй только сам токен:

```env
N8N_BEARER_TOKEN=<generated_token>
```

В узле `Auth Check` в n8n указывай полное значение:

```text
Bearer <generated_token>
```

## Проверка

Запрос с токеном должен вернуть `200`:

```powershell
$env:N8N_BEARER_TOKEN="<generated_token>"
python main.py "AI automation для Telegram"
```

Запрос без токена должен вернуть `403`:

```powershell
Remove-Item Env:N8N_BEARER_TOKEN
python main.py "AI automation для Telegram"
```

## Важно

- Не коммить реальный токен в GitHub.
- В репозитории используй только placeholder: `<N8N_BEARER_TOKEN>`.
- Если токен попал в публичный репозиторий, сгенерируй новый и замени его в n8n.
