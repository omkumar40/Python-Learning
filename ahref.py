from urllib.request import urlopen
from bs4 import BeautifulSoup

#Program for going through links in a web page by user choice and disaplaying the links

#url = 'http://python-data.dr-chuck.net/known_by_Conar.html'
url = input('Enter URL:')
count = int(input('Enter count:'))
position = int(input('Enter position:'))
html = urlopen(url).read()

soup = BeautifulSoup(html,"html.parser")
href = soup('a')

print('Retrieving',url)
for i in range(count):
    link = href[position-1].get('href', None)
    print('Retrieving',link)
    html = urlopen(link).read()
    soup = BeautifulSoup(html,"html.parser")
    href = soup('a')

