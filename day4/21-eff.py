# Optimising the program by directly accessing the name:
# Compare these three approaches:
# import math => math.sqrt()
# from math import sqrt => sqrt()
# import math => f = math.sqrt; f()

import time
import math

N = 10_000_000
t0 = time.time()
a = [math.sqrt(i) for i in range(N)]
t = time.time()
print(t - t0)

# t0 = time.time()

# t = time.time()
# print(t - t0)
