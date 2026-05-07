import os

import requests


url = os.getenv("PRODUCTION_WEBHOOK_URL", "<PRODUCTION_WEBHOOK_URL>")
token = os.getenv("N8N_BEARER_TOKEN", "<N8N_BEARER_TOKEN>")
headers = {"Authorization": f"Bearer {token}"}
payload = {"topic": "Authorized AI Telegram post generation"}

response = requests.post(url, headers=headers, json=payload, timeout=60)
print(response.status_code)
print(response.text)
