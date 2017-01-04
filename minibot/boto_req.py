# my web scraper bot,using 'requests' and beautifulsoup

import requests
from bs4 import BeautifulSoup


url = "https://en.wikipedia.org/wiki/List_of_Nigerian_films"
r = requests.get(url)

soup = BeautifulSoup(r.content)
#links = soup.findAll('a')

#for link in links:
##    #print()
    #print(link.text, link.get('href'))
##    

g_data = soup.findAll("div", {"class":"mw-content-ltr"})
for data in g_data:
    print(data.contents[0].text)
