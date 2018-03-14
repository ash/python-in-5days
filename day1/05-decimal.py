# How to ensure precision

# These calculations most likely will not give 0.3
a = 0.1
b = 0.2
c = a + b
print(c)

# Use the "decimal" module
import decimal

# Create Decimal values (note: these are strings)
a = decimal.Decimal('0.1')
b = decimal.Decimal('0.2')
c = a + b
print(type(c))
print(c) # Now it is 0.3

d = a/b
print(d)
print(type(d))

e = 1.00/3
print(e)


e = decimal.Decimal('1.00')
f = decimal.Decimal('3')
g = e/f
print(type(g))
print(g)

# Support of arbitrary precision
x = decimal.Decimal('0.345678909876543456789098765434567898765456789876543')
print(x)

