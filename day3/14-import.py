# Instead of
# from math import pi, cos
# import everthing
from math import *

print(ceil(cos(pi)))

# Be careful not to hide imported names
def ceil(x):
    print('my ceil')

print(math.ceil(cos(pi)))
