# This is how you can use 'with' with your own classes.
# Define the __enter__ and __exit__ methods, which Python will call for you when entering to the 'with' block and exiting from it.

class W:
    def __init__(self):
        pass
    def __enter__(self):
        print('__enter__')
    def __exit__(self, a2, a3, a4):
        print('__exit__')
    def info(self):
        print(1/0)
        print('at info()')

w = W()
with w:
    # w.__enter__()
    w.info() # with exception
    # w.__exit__()

print('ok done')
