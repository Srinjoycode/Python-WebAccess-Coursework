
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
#input of info from user
url = input('Enter - ')
count=int(input("Enter count:"))
position=int(input("enter position:"))
#initialising counters
posCounter=1
countCounter=1
# Retrieve 
while countCounter<=count:
    #establishing link to the url
    posCounter=1
    print(f"Retrieving: {url}")
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    for tag in tags:
        if posCounter<position:
            posCounter+=1
        else:
            url=tag.get('href', None)
            break
    if countCounter<count:
        countCounter+=1
    elif countCounter==count:

        nameReq=tag.contents[0]
        print(f"last name in sequence is {nameReq}")
        break           