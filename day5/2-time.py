# Using decorator, which executes a function.

import time

def time_measure(f):
    t0 = time.time()
    # Here, the f function is called:
    f()
    t = time.time()
    return t - t0


@time_measure
def slow_f():
    time.sleep(2)

# Notice that a name of slow_f is passed, not that a funciton is called here
print(slow_f)
