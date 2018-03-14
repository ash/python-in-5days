# An attempt to modify a dictionary from within a function

def f(x):
    print(type(x))
    print(x['a'])
    x['a'] = 'gamma'

# A dictionary will be changed:
d = {'a':"alpha", 'b':'beta'}
f(d)
print(d)
