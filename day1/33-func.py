# A function with two parameters:
def s(a, b):
    return a + b

# Using position parameters:
print(s(3, 4))

# Using named parameters (in any order):
print(s(a=3, b=4))
print(s(b=4, a=3))

# Positionals should always be first in the list of arguments:
print(s(3, b=4))
#print(s(b=3, 4))
