import requests
handle = input('Enter your github: ')
link = 'https://api.github.com/users/'+handle
f = requests.get(link)
print(f.text)
