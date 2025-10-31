import json
input = '''[
    {"id": "001", "x": "2", "name": "Chuck"},
    {"id": "009", "x": "7", "name": "Brent"}
]'''

info = json.loads(input)
print('User count:', len(info))
for item in info:
    print('Name:', item['name'])
    print('Id:', item['id'])
    print('Attribute x:', item['x'])

# This code snippet demonstrates how to parse a JSON array in Python using the json module.
# It loads the JSON data into a list of dictionaries and iterates through each dictionary to access specific fields.