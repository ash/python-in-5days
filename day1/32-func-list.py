# Modifying a list inside a function. The list will be changed after you return from it.

def f(x):    
    x[1] = 77

x = [1, 2, 3]

# Use [:] to prevent an array from being modified:
print(f(x[:]))
print(x)
