import xml.etree.ElementTree as ET
data = '''<person>
    <name>Ahmed</name>
    <phone type="intl">+92-300-8224057</phone>
    <email hide="yes"/>
</person>'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Phone Type:', tree.find('phone').get('type'))
print('Phone Number:', tree.find('phone').text)
print('Attr:', tree.find('email').get('hide'))

# The code above parses an XML string and extracts specific information from it.
# The code uses the xml.etree.ElementTree module to parse the XML data.
# It retrieves the text content of the <name> and <phone> elements,
# and the value of the 'hide' attribute from the <email> element.

input = '''<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>John</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Jane</name>
        </user>
    </users>
</stuff>'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print('User count:', len(lst))
for item in lst:
    print('Name:', item.find('name').text)
    print('ID:', item.find('id').text)
    print('Attribute x:', item.get('x'))

# The code above parses another XML string containing user information.
# It counts the number of <user> elements and extracts the <name>, <id>,
# and the 'x' attribute for each user.
