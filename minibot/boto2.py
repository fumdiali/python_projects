import urllib3
from bs4 import BeautifulSoup
import re

http = urllib3.PoolManager()

#r = http.request('GET', 'https://en.wikipedia.org/wiki/List_of_Nigerian_musicians', fields={'href':re.compile("^/wiki/")})
#print(r.data.decode('utf-8'))
r = http.request('GET',"https://en.wikipedia.org/wiki/List_of_Nigerian_musicians")

'''
myUrl = opener.open(r).read()

soup = BeautifulSoup(myUrl)

for link in soup.findAll('a',attrs={'href':re.compile("^/wiki/")}):
    print(link)
#title = soup.title.text

body = soup.find(text="Origin").findNext('td')
outfile = open("",'w')
outfile.write(body.text)
'''

print(r.read('a','href','re.compile("^/wiki/")'))
#print(r.status)
#print(r.headers)
