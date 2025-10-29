import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())
fhand.close()

counts = dict()
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    words = line.decode().strip().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)
fhand.close()

import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

fhand = urllib.request.urlopen('https://www.dr-chuck.com/page1.htm')
for line in fhand:
    print(line.decode().strip())
fhand.close()
