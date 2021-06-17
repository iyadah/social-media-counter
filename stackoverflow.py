import requests
import json
url = f"https://stackoverflow.com/users/6467496/user120010.json"
f = json.loads(requests.get(url).text)

print(f.json().get("reputation"))
