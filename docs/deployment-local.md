[← Architecture](architecture.md) · [Back to README](../README.md) · [VPS Deployment →](deployment-vps.md)

# Local Deployment

## Use case

Use local deployment for Assignment 1, JSON-path debugging, prompt iteration, and quick webhook tests before moving the workflow to VPS.

## Commands

```bash
docker pull n8nio/n8n:latest
docker volume create n8n_data
docker run -d --name n8n -p 5678:5678 -v n8n_data:/home/node/.n8n n8nio/n8n
docker ps
```

## Local checklist

- `n8n` UI opens on `http://localhost:5678`
- workflow imported successfully
- OpenAI credential created
- Telegram credential or HTTP request node configured
- webhook test URL reachable from local client

## Notes

- Local mode is best for workflow iteration.
- Test URLs in `n8n` can differ from production webhook URLs.
- Keep screenshots from local tests for Assignment 1 evidence.

## See Also

- [Assignment 1](assignment-1-local-text-workflow.md) - Local MVP workflow walkthrough
- [n8n JSON Paths](n8n-json-paths.md) - Expression debugging during local tests
- [Troubleshooting](troubleshooting.md) - Common local runtime issues
