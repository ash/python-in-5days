# List comprehension vs. generator.

data1 = [x**2 for x in range(10)]
print(data1[0])
print(data1[1])
print(data1[2])


data2 = (x**2 for x in range(10))
print(data2.next())
print(data2.next())
print(data2.next())
