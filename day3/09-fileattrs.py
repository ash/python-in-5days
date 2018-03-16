# Demonstrating different attributes of the file object.

f = open('data.txt', 'rb')
print(f.closed)
f.close()
print(f.closed)
#f.read()

print(f.mode)
print(f.name)

