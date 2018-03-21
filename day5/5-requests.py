# Using an external 'requests' library, which provides us with a simple interface
# to fetch data from remote resources.

import requests

resp = requests.get('http://google.com')

if resp.status_code == 200:
    print(resp.content) 
    print(resp.headers)
    print(resp.encoding)
    resp.json()

