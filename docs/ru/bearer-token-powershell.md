[← n8n JSON Paths](n8n-json-paths.md) · [Назад к README](../../README.md) · [Troubleshooting →](troubleshooting.md)

# Bearer Token PowerShell

## PowerShell 7+

```powershell
$token = [Convert]::ToHexString([System.Security.Cryptography.RandomNumberGenerator]::GetBytes(32)).ToLower()
$env:N8N_BEARER_TOKEN = $token
Write-Host $token
Write-Host "Bearer $token"
```

## Windows PowerShell 5.1

```powershell
$bytes = New-Object byte[] 32
[System.Security.Cryptography.RandomNumberGenerator]::Create().GetBytes($bytes)
$token = -join ($bytes | ForEach-Object { $_.ToString("x2") })
$env:N8N_BEARER_TOKEN = $token
Write-Host $token
Write-Host "Bearer $token"
```

## Как использовать

- в `.env` храни только сам токен
- в `n8n` auth-check сравнивай с `Bearer <token>`
- запрос с токеном должен вернуть `200`, без токена `403`

## See Also

- [Troubleshooting](troubleshooting.md) - что делать при `403`
- [Security](security.md) - правила хранения токенов
- [VPS Deployment](deployment-vps.md) - где применяется bearer token
