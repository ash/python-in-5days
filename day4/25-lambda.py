# Demonstrating lambda functions (can be replaced with list comprehensions)

data = list(range(10))

# def f(x):
#     return x**2

#converted_data = map(f(x), data)
converted_data = map(lambda x: x**2, data)
print(list(converted_data))
