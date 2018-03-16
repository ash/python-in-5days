# File objects are effectively streams. You can read from it in text mode, for example (which happens by default)


with open('text.txt', 'rt') as f:
    print(type(f))
    #print(f.encoding)
    data = f.read(3)
    print(data)

# TextIOWrapper <- TextIOBase <- IOBase
