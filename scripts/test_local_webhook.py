import os

import requests


payload = {"topic": "Telegram AI autopublishing workflow with n8n"}
url = os.getenv("LOCAL_WEBHOOK_URL", "http://localhost:5678/webhook/telegram-ai-autopublisher")

response = requests.post(url, json=payload, timeout=60)
print(response.status_code)
print(response.text)
