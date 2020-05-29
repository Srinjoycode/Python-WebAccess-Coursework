from urllib.request import urlopen
import ssl
import json
sum=0
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
#input of URL
url = input('Enter - ')
html = urlopen(url, context=ctx).read()
info = json.loads(html)["comments"]
print('User count:', len(info))

for item in info:
    print('Name', item['name'])
    print('count', item['count'])
    num=int(item['count'])
    sum+=num
print("sum:",sum)     