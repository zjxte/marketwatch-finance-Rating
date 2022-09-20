import requests
from bs4 import BeautifulSoup
import re

url = 'https://www.marketwatch.com/tools/upgrades-downgrades'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
    'Host': 'www.marketwatch.com',
}

response = requests.get(url, headers = headers)
html_content = response.text

soup = BeautifulSoup(html_content,'html.parser')

for tr in soup.find_all('tr'):
  tds = tr.find_all('td')
  print(tds)
