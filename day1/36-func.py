# Allow "keyword arguments"

def f(**x):
    print(type(x))
    print(x['a'])

# x will be a dictionary but you avoid typing a lot of punctuation to create a dictionary
f(a="alpha", b='beta')
