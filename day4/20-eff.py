# Comparing speed of building a list using .append
# vs. using a list comprehension.

import time

N = 10000000
t0 = time.time()
a = []
for i in range(N):
    a.append(i ** 2)
t = time.time()
print(t - t0)

t0 = time.time()
a = [i ** 2 for i in range(N)]
t = time.time()
print(t - t0)
