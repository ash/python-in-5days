# Fetching a page using the prepared Request object

import urllib.request

req = urllib.request.Request('https://google.com')

f = urllib.request.urlopen(req)
print(f.read(100))
