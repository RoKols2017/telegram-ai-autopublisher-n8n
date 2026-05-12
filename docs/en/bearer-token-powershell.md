[← n8n JSON Paths](n8n-json-paths.md) · [Back to README](../../README.en.md) · [Troubleshooting →](troubleshooting.md)

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

## How to use it

- store only the raw token in `.env`
- compare against `Bearer <token>` inside the `n8n` auth check
- request with token should return `200`; request without token should return `403`

## See Also

- [Troubleshooting](troubleshooting.md) - what to check for `403`
- [Security](security.md) - token hygiene rules
- [VPS Deployment](deployment-vps.md) - where the token is applied
