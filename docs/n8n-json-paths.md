[← Telegram API](telegram-api.md) · [Back to README](../README.md) · [Troubleshooting →](troubleshooting.md)

# n8n JSON Paths

## Goal

This file helps inspect the most common path mismatches when wiring nodes.

## Typical inbound paths

- `{{$json.topic}}`
- `{{$json.body.topic}}`
- `{{$json.headers.authorization}}`

## Typical transformed fields

- `{{$json.generated_text}}`
- `{{$json.image_prompt}}`
- `{{$json.image_url}}`

## Practical debugging flow

1. open `Executions`
2. inspect actual node output JSON
3. copy the exact field path
4. replace guessed expressions with confirmed ones

## Warning

Do not assume OpenAI output fields are identical across node versions. Confirm the real output object in your installed `n8n` build.

## See Also

- [Troubleshooting](troubleshooting.md) - Debugging path-related failures
- [Assignment 1](assignment-1-local-text-workflow.md) - MVP field mapping example
- [Assignment 2](assignment-2-full-text-image-workflow.md) - Full workflow field propagation
