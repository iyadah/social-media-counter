# Python 3.5
# Also found: https://github.com/syphon5/blog/tree/master/pinterest_follower_scraper

#Import visualization packages
import seaborn as sns
import matplotlib.pyplot as plt
#Import HTTPS requests package
import requests
#Import web scraping package
from bs4 import BeautifulSoup
#Import data analysis package
import pandas as pd
#Import user-agent spoof package
from fake_useragent import UserAgent
#Import random number
from random import randint
#Import sleep time
from time import sleep
#Import time
import time

#Spoof the user-agent so Pinterest thinks you are visitng from a browser
ua = UserAgent()

#Set the user-agent header for the HTTPS request
headers = {'User-Agent': str(ua.chrome)}
#Action Required: Put your list of Pinterest URLs in quote, separated by commas, inside the square brackets. See example below.
urls = ['https://www.pinterest.com/deltaco/','https://www.pinterest.com/fuzzystacos/', 'https://www.pinterest.com/torchystacos/',
       'https://www.pinterest.com/tacobueno/', 'https://www.pinterest.com/tacocabana/']

#Create empty list to store future dictionary of pinterest URLs, followers, and date
output = []
#Run a for loop to iterate through list of URLs and retrieve follower data
for i, j in enumerate(urls):
    print("Scraping URL: " + j)
	#Scrape the Pinterest website code with spoofed user-agent
    response = requests.get(urls[i], headers=headers)
	#Parse the content with BeautifulSoup 
    soup = BeautifulSoup(response.content, 'html.parser')
	#Action Required: Replace the quoted contents for class_= with the updated class you find in Pinterest's website source code in tutorial. This grabs the follower counts.
    followers = soup.find_all(class_='_su _st _sv _sm _5k _sn _sr _nl _nm _nn _no')[0].get_text()
	#Only keep the number portion of the follower count text. Exampe: "583 Followers"...keep 583
    followers = ''.join(c for c in followers if c.isnumeric())
	#Convert follower number to integer
    followers = int(followers)
    print(followers)
