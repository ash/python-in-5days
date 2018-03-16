# Catch an exception if there is no file on disk.
try:
    with open('non-existing.txt') as f:
    data = f.read()
    print(data)
except FileNotFoundError:
    print('not found')

print('ok done')
