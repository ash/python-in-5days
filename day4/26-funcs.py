# Some other built-in functions that were not covered yet.

print(all([True, True, False]))
print(any([True, True, False]))
print(ascii('Zürich'))
print(bin(123))

x = 3
def f():
    pass
y = f
print(callable(x))
print(callable(y))

l = list(range(100,110))
d = dict(enumerate(l))
print(d)

print(divmod(101, 3))
