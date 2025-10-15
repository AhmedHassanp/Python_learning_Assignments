stuff = dict()
print(stuff.get('candy',-1))

import re
x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print(y)