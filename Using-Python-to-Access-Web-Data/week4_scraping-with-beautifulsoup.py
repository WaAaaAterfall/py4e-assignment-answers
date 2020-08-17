from urllib.request import urlopen
from bs4 import BeautifulSoup

url = url = input('Enter - ')
html = urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')
count = 0
sum = 0
for tag in tags:
	x = int(tag.text)
	count = count+1
	sum = sum+x
print(sum)
print(count)
