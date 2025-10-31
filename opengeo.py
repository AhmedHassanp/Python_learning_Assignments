import urllib.request, urllib.parse
import http, json, ssl

serviceurl = 'https://py4e-data.dr-chuck.net/opengeo?'

while True:
    #address = input('Enter location: ')
    #address = "Ann Arbor, MI"
    #address = "South Federal University"
    address = "University of West Florida"
    if len(address) < 1: break

    address = address.strip()
    parms = dict()
    parms['q'] = address

    url = serviceurl + urllib.parse.urlencode(parms)
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ssl.create_default_context())
    data = uh.read().decode()
    #print(data)
    
    print('Retrieved', len(data), 'characters', data[:20].replace('\n', ' '))

    try:
        js = json.loads(data)
    except:
        js = None
    
    if not js or 'features' not in js:
        print('==== Download Error ====')
        print(data)
        break

    if len(js['features']) == 0:
        print('==== Object not found ====')
        print(data)
        break

    #lat = js['features'][0]['properties']['lat']
    #lon = js['features'][0]['properties']['lon']
    pluscode = js['features'][0]['properties']['plus_code']

    #print('lat', lat, 'lon', lon)
    print('Plus code', pluscode)
    #location = js['features'][0]['properties']['formatted']
    #print(location)
    break