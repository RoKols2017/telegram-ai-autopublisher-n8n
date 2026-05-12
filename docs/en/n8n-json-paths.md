[← Telegram API](telegram-api.md) · [Back to README](../../README.en.md) · [Bearer Token PowerShell →](bearer-token-powershell.md)

# n8n JSON Paths

## Typical input paths

- `{{$json.topic}}`
- `{{$json.body.topic}}`
- `{{$json.headers.authorization}}`

## Typical output fields

- `{{$json.text}}`
- `{{$json.output_text}}`
- `{{$json.image_prompt}}`
- `{{$json.image_url}}`

## Practical workflow

1. Open `Executions`.
2. Inspect the actual node output.
3. Copy the exact path.
4. Update the downstream expression only after verification.

## See Also

- [Bearer Token PowerShell](bearer-token-powershell.md) - auth test flow
- [Troubleshooting](troubleshooting.md) - mapping-related failures
- [Full Workflow](full-workflow.md) - end-to-end data propagation
