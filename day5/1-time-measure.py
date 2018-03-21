# How to measure time of the execution of a function

import time

def slow_f():
    time.sleep(2)

t0 = time.time()

slow_f()

t = time.time()
print(t - t0)