import re
handle = open('test.txt')
count = 0
len = 0
for line in handle:
    words = line.rstrip()
    list = re.findall('[0-9]+',words)
    for num in list:
        num = int(num)
        count += num
        len += 1

print(count)
print(len)
