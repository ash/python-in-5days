# Using urllib built-in library to fetch pages from internet.

import urllib.request

f = urllib.request.urlopen('http://google.com')
print(f.read(100))
