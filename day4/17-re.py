# Demonstrating the methods of the re module

import re

s = 'EUR500 USD500'

r = re.match('(USD|EUR)(\d+)', s)
print(r.groups())

results = re.findall('(USD|EUR)(\d+)', s)
print(results)

if re.match('^\d(?:EUR|USD)\d+$', '3USD500'):
    print('ok')

r = re.findall('(?:USD|EUR)(\d+)', s)
print(r)

r = re.findall('((USD|(EUR|CHF))(\d+))', s)
print(r)
