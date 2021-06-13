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
handle = input('Enter pinterest handle: ')
url = "https://www.pinterest.ie/"+handle+"/"
print(url)
#driver.get(url)
#html = driver.page_source
#print(html)
#followers_count = html.find("meta")
#print(followers_count)

req = requests.get(url, headers)
soup = BeautifulSoup(req.content, 'html.parser')
meta = soup.find('meta', property="pinterestapp:followers")
print(meta["content"])
#print(soup.prettify())
#followers_count = soup.find_all(class_="UserInfo-statRow-Erw")
#followers_count = soup.find_all(class_="zI7 iyn Hsu")
#followers_count = html.find("div", {"class": "Jea zI7 iyn Hsu"})
#print(followers_count)
