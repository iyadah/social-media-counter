import requests
import json
handle = input('Enter your github default (paulmillr): ') or 'paulmillr'
link = 'https://api.github.com/users/'+handle
f = json.loads(requests.get(link).text)
print(f['followers'])
