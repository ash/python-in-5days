# Data type: tuple [read: toopl]

# A tuple is a list enclosed on ( )
t = (1, 2, 3, 2)

# How to swap values:
a = 10
b = 20

# Using temporary variable
t = a
a = b
b = t


# Using tuples
# Note: in this case, there are no parentheses but these are still tuples:
a, b = b, a

print(a, b)

# Or just assign more than one value at a time:
c, d = 4, 6
print(c, d)

# How many 2s are there in a tuple?
print(t.count(2))