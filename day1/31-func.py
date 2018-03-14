# Modifying a variable inside a function. It is not changed after you return. 
def f(x):    
    x = 4
    return x * 2

x = 3
print(f(x))
print(x)
