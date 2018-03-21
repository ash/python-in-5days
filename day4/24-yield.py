# Demonstrating the 'yield' keyword. You use it in place of the 'return' 
# keyword but can re-enter the function.

def counter():
    for i in range(1000):
        yield i

g = counter()
print(next(g))
print(next(g))
print(next(g))

# Creating a separate generator
g2 = counter()
print(next(g2))
print(next(g2))
print(next(g2))

print(next(g))
print(next(g))

print(next(g2))
