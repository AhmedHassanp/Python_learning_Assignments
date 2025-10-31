import json
data = '''{
    "name": "Chuck",
    "phone": {
        "type": "intl",
        "number": "+1 734 303 4456"},
    "email": {
        "hide": "yes"}
}'''

info = json.loads(data)
print('Name:', info["name"])
print('Hide:', info["email"]["hide"])

# The code above demonstrates how to parse a JSON string in Python using the json module.
# It loads the JSON data into a Python dictionary and accesses specific fields within that dictionary.
