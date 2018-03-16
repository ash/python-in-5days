# Illustrating comprehensions

import math

# x = 0
# while x < 5:    
#     print("%g\t%g" % (x, math.sin(x)))
#     x += 0.1

# list comprehensions
data = [ math.sin(x/10) for x in range(0, 50) ]
print(data)

# list comprehension
squares = [ x ** 2 for x in range(10) ]
print(squares)

# list comprehension with an 'if' condition
squares = [ x ** 2 for x in range(10) if x % 2 ]
print(squares)
