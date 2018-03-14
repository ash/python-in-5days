# Allow arbitrary number of arguments.

def f(a, *L):
    print(type(L))
    print(L)
    print(min(L))

# 2 and 5 will go to the list L:
f(4, 2, 5)
