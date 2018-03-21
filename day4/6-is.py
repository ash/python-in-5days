# Comparing == and 'is'. The 'is' keyword checks if its operands point to the _same_ object,
# while == only compares the two values.

x = 10
y = x

x = [1, 2, 3]
y = []
y.append(1)
y.append(2)
y.append(3)

print(x == y)
print(x is y)
