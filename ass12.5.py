# Following Links in Python
# Install BeautifulSoup if needed: pip install beautifulsoup4

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Input: starting URL, count, and position
url = input('Enter URL: ')
count = int(input('Enter count: '))       # Number of times to follow the link
position = int(input('Enter position: ')) # Position of the link to follow (1-based)

# Loop to follow links
for i in range(count):
    print(f'\nRetrieving: {url}')
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all anchor tags
    tags = soup('a')

    # Move to the desired position link
    if len(tags) < position:
        print("Not enough links on this page.")
        break

    link = tags[position - 1].get('href', None)
    url = link  # update for next iteration

print(f'\nFinal URL: {url}')