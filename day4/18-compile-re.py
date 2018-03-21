# Using a pre-compiled regex to speed the program up.

import re

r = re.compile(r'\d+')

for i in range(10):
    if r.match('123'):
        print('123')

    if not r.match('abc'):
        print('not abc')

print(re.findall(r'(.)(.)', 'abd'))
