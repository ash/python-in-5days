# Data type: lists
# Use square brackets and comma to enclose and separate numbers:
a = [1, 2, 3]
print(a)

# Lists can contain mixed-type data:
a = ['one', 'two', 3]
print(a)

# Create an empty list:
empt = []
print(type(empt))
print(len(a))
print(len(empt))

# Create a list based on an iterable item (a single string in this example):
l = list('a')
#l = ['a']

# Indexing elements:
print(a[1])

# Cast a range to a list
a = list(range(10))
print(a)
print(a[3])

# You index a list in the same manner you work with strings:
s = "abcdefg"
print(s[3]) 
#s[3] = 'x'   

# Modifying an item:
a[5] = 99
print(a)

print(a[3:5])

# Lists are not acually copied, so b = a makes an alias:
print(a)
b = a
b[6] = 77
print(a)

# Use [:] to copy the values:
c = a[:]
c[7] = 88
print(a)

