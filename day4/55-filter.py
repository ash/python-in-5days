def f(x):
    return x % 2

data = list(range(10))
filtered_data = filter(f, data)
print(list(filtered_data))

filtered = [x for x in data if f(x)]
print(filtered)
