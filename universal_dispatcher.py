import json
import requests

# Load message input
with open('message_input.json') as f:
    data = json.load(f)

url = data["target_url"]
method = data.get("method", "POST").upper()
headers = data.get("headers", {})
body = data.get("body", {})

try:
    if method == "POST":
        response = requests.post(url, headers=headers, json=body)
    elif method == "GET":
        response = requests.get(url, headers=headers, params=body)
    else:
        print(f"Unsupported method: {method}")
        exit()

    print(f"✅ Sent to {url} — Status: {response.status_code}")
    print(response.text)
except Exception as e:
    print(f"❌ Error sending message: {e}")

