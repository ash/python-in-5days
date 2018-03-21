# Comparing different approaches to have pre-computed lookup tabels
# vs. calculating the result at the time of a function call

import time

    #0               1          2          3
r2 = [[0, 0, 0, 0], [1, 1, 1, 1], [1, 2, 4, 8], [1, 3, 9, 27]]
r3 = [ 0, 0, 0, 0 ,  1, 1, 1, 1 ,  1, 2, 4, 8 ,  1, 3, 9, 27 ]

def f1(x, n):
    return x ** n

def f2(x, n):
    return r2[x][n]

def f3(x, n):
    return r3[n + 4 * x]

t0 = time.time()
for _ in range(1000_000):
    f1(3, 2)
t = time.time()
print(t - t0)

t0 = time.time()
for _ in range(1000_000):
    f2(3, 2)
t = time.time()
print(t - t0)


t0 = time.time()
for _ in range(1000_000):
    f3(3, 2)
t = time.time()
print(t - t0)

print(f2(2,3))
print(f3(2,3))