import requests

handle = input('Enter your twitter handle default (BarackObama): ') or 'BarackObama'
link = "https://cdn.syndication.twimg.com/widgets/followbutton/info.json?screen_names="+handle

f = requests.get(link)
print(f.text)
