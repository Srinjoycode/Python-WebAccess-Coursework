import urllib.request
import urllib.parse
import urllib.error
import xml.etree.ElementTree as ET
sum = 0

url = input("Enter location:")
uh = urllib.request.urlopen(url)
data = uh.read()
print("Retrieving:", url)

tree = ET.fromstring(data)
print("retrived:", len(data), "charaters")
lst = tree.findall('comments/comment/count')
print("count:", len(lst))
counts = tree.findall('.//count')

sum = 0

for count in counts:
    sum += int(count.text)

print('Sum: ', sum)
