import urllib
from bs4 import BeautifulSoup
import re

opener = urllib.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
#http = urllib3.PoolManager()

#r = http.request('GET','https://en.wikipedia.org/wiki/List_of_Nigerian_musicians')
url = ("https://en.wikipedia.org/wiki/List_of_Nigerian_musicians")

myUrl = opener.open(r).read()

soup = BeautifulSoup(myUrl)

for link in soup.findAll('a',attrs={'href':re.compile("^/wiki/")}):
    print(link)
#title = soup.title.text

body = soup.find(text="Origin").findNext('td')
outfile = open("",'w')
outfile.write(body.text)
