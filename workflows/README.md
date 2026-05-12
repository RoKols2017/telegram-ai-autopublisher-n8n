# Workflows

This directory contains sanitized `n8n` exports only.

## Files

- `text-only-mvp-workflow.sanitized.json`
- `full-text-image-auth-workflow.sanitized.json`

## Import steps

1. Import the JSON into `n8n`.
2. Reattach real credentials inside the UI.
3. Replace placeholder values with environment-backed expressions or manual `n8n` values.
4. Test before activation.

## Security note

Do not export a workflow and commit it directly. Run the sanitizer first and manually review the result.
