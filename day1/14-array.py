# More on lists:

a = list(range(10))
print(a)

# Reverse reverses in-place
a.reverse()
print(a)

# Find an index of the element '4'
print(a.index(4))

# Remove the last element and return it:
last = a.pop()
print(last)
print(a)

# Remove and return the 3rd element:
print(a.pop(3))
print(a)

