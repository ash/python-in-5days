# Using a function to generate values using list comprehension.

def f(x):
    print('Calling f(%i)' % x)
    return x ** 2

mylist = [ f(x) for x in range(30) ]
#print(mylist)
print(mylist[1])
