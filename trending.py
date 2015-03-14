import requests
from bs4 import BeautifulSoup

r = requests.get('https://github.com/trending')

soup = BeautifulSoup(r.content)

print ['https://github.com' + res.a['href'] for res in soup.find_all('h3', 'repo-list-name')]
