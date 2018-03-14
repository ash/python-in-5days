# An implementation of a factorial function using a global storage:

factorials = {}

def f(n):
    if factorials.get(n):
        return factorials[n]

    if n < 2:
        return 1
    r = f(n - 1) * n
    factorials[n] = r
    return r

print(f(100))
print(f(200))
