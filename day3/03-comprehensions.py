# Other types of comprehensions.

# Set comprehension
myset = { x**3 for x in range(5) }
print(myset)

# Dict comprehension
mydict = { x : x**2 for x in range(5) }
print(mydict)

# A bit more complex dictionary comprehension
mydict = { "The square of %i is " % x : x**2 for x in range(5) }
print(mydict)

# Notice that there is no 'tuple comprehension' in this scheme