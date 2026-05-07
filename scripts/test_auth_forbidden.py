import os

import requests


url = os.getenv("PRODUCTION_WEBHOOK_URL", "<PRODUCTION_WEBHOOK_URL>")
payload = {"topic": "Request without auth header"}

response = requests.post(url, json=payload, timeout=60)
print(response.status_code)
print(response.text)
