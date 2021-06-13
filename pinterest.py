import requests
from bs4 import BeautifulSoup
#from selenium import webdriver
#driver = webdriver.Firefox()
headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }
handle = input('Enter pinterest handle default (bonnietsang): ') or 'bonnietsang'
url = "https://www.pinterest.ie/"+handle+"/"
print(url)
req = requests.get(url, headers)
soup = BeautifulSoup(req.content, 'html.parser')
meta = soup.find('meta', property="pinterestapp:followers")
print(meta["content"])
