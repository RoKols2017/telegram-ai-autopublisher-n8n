[← Architecture](architecture.md) · [Back to README](../../README.en.md) · [VPS Deployment →](deployment-vps.md)

# Local Deployment

## When to use it

Use the local setup for prompt iteration, JSON-path debugging, and smoke testing before moving the workflow to the VPS runtime.

## Commands

```bash
docker pull n8nio/n8n:latest
docker volume create n8n_data
docker run -d --name n8n -p 5678:5678 -v n8n_data:/home/node/.n8n n8nio/n8n
docker ps
```

## Local checklist

- `n8n` UI opens on `http://localhost:5678`
- workflow imports successfully
- credentials are rebound locally
- webhook test URL responds

## See Also

- [Text-Only MVP](text-only-mvp-workflow.md) - minimal local test flow
- [n8n JSON Paths](n8n-json-paths.md) - expression debugging
- [Troubleshooting](troubleshooting.md) - common local failures
