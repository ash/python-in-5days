# Intro to regular expressions

import re

# Task: match

s = 'EUR123457'
if re.match('1234', s):
    print('is 1234')

if re.search('1234', s):
    print('there is 1234')

# meta-character
if re.match('$1234.', s):
    print('using match; there is 1234')


s = 'EUR2'
if re.match(r'^EUR\d?$', s):
    print('EUR NN')


s = 'EUR224345435'
if re.match(r'^EUR\d+$', s):
    print('EUR NN+')

for s in ['E500', 'E500', 'C500']:
    if re.match(r'[EU]\d+$', s):
        print('Price %s in eur or usd' % s)

for s in ['EUR500', 'Usd500', 'CHF500']:
    if re.match(r'(EUR|USD)\d+$', s, re.IGNORECASE):
        print('Price %s in eur or usd' % s)


