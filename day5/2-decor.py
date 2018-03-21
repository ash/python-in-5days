# Using decorator to measure time

import time

def time_measure(f):
    t0 = time.time()
    f()
    t = time.time()
    return t - t0

@time_measure
def slow_f():
    time.sleep(2)

print(slow_f
