import urllib.request
import http, json, ssl

#url = 'https://py4e-data.dr-chuck.net/comments_42.json'
url = 'https://py4e-data.dr-chuck.net/comments_2304137.json'

print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ssl.create_default_context())
data = uh.read().decode()
#print(data)

js = json.loads(data)
print('User count:', len(js['comments']))
total = 0
for item in js['comments']:
    total += int(item['count'])
print('Sum:', total)