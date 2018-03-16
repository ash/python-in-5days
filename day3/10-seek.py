# Read from an arbitrary position.

f = open('data.txt')
f.seek(4)
print(f.tell())
print(f.read())

print(f.fileno())
