# Using modules of the standard library
# Either import the whole module or list the names that you need:

import math

def f():
    # It is also possible to import a module so that the names are visible locally only
    from math import pi
    print(math.pi/2)
    print(pi)

print(2*math.pi)
f()