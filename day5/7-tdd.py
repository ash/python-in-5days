# Demonstrating the TDD approach. With it, you first start with tests and then
# fill the body of the function being tested.

def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)

#print(fact(5))

print(fact(1) == 1)
print(fact(2) == 2)
print(fact(5) == 120)
