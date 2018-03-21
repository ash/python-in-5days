# List comprehension vs. generators (both uses the function f)

def f(x):
    print('f(%i)' % x)
    return x**2

data1 = [f(x) for x in range(10)]
print(data1[0])
print(data1[1])
print(data1[2])


data2 = (f(x) for x in range(10))
print(data2.next())
print(data2.next())
print(data2.next())
