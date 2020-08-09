#program to find the sum and average in an web page of span element

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
#url=http://py4e-data.dr-chuck.net/comments_862639.html
url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
tags=soup('span')
num=list()
for tag in tags:
    num.append(tag.contents[0])
num=list(map(int,num))
print('Count',len(num))
print('Sum',sum(num))