# Printing all the characters that match the \d regex. 
# It is ways beyond the regular 0-9 from the ASCII table.

import re

for i in range(32, 10_000):
    ch = chr(i)
    # Use the re.ASCII flag to limit the \d to 0-9 only
    if re.match('\d', ch, re.ASCII):
        print(ch, end='')
print('')

for i in range(32, 10_000):
    ch = chr(i)
    if re.match('[$.0-9A-Za-z[]', ch, re.ASCII):
        print(ch, end='')
print('')

for i in range(32, 256):
    ch = chr(i)
    if re.match('[^a-zA-Z]', ch):
        print(ch, end='')
print('')
