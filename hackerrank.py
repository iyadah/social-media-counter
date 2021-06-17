import requests
import json
from bs4 import BeautifulSoup


handle = input('Enter behance handle default (Gennady): ') or 'Gennady'
url = "https://www.hackerrank.com/rest/contests/master/hackers/"+handle+"/profile"
print(url)
header = {'x-requested-with': 'XMLHttpRequest'}
t = requests.get(url, headers=True)

#newDictionary=json.loads(t)
print (t)
