import json
import urllib.request, urllib.parse, urllib.error

address = input('Enter location: ')
fhand = urllib.request.urlopen(address)
print('Retrieving:', address)
data = fhand.read().decode()
print('Retrieved', len(data), 'characters')

try:
    js = json.loads(data)
except:
    js = None
info = js["comments"]

sum = 0
count = 0
for item in info:
    sum += item["count"]
    count += 1

print('Sum:',sum,' Count:',count)
