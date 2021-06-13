import requests
from bs4 import BeautifulSoup

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }

handle = input('Enter behance handle default (designerpreis): ') or 'designerpreis'

url = "https://www.behance.net/"+handle+"?tracking_source=search_projects_recommended"
print(url)
req = requests.get(url, headers)
soup = BeautifulSoup(req.content, 'html.parser')
#print(soup.prettify())
#followers_count = soup.find_all(class_="UserInfo-statRow-Erw")
followers_count = soup.find_all(class_="UserInfo-statValue-1_- e2e-UserInfo-statValue-followers-count")
print(followers_count[0].string)
