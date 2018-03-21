# Comparing the speed of using 'in' and the implicit loop

import random
import time

bigdata = [random.randint(0, 100_000) for _ in range(1_000_000)]

n = 55
t0 = time.time()
r = n in bigdata
t = time.time()
print(r)
print(t - t0)

r = False
t0 = time.time()
for x in bigdata:
    if n == x:
        r = True
        break
t = time.time()
print(t - t0)
print(r)
