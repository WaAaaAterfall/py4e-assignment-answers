import xml.etree.ElementTree as ET
import urllib.request, urllib.parse, urllib.error
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')

print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
input = uh.read()

print('Retrieved', len(input), 'characters')
tree = ET.fromstring(input)

lst = tree.findall('comments/comment')
print('User count: ', len(lst))
sum = 0
count = 0
for item in lst:
    sum += int(item.find('count').text)
#     count += 1
# print('Counts:', count)  //same as len(lst)
print('Sum:', sum)
