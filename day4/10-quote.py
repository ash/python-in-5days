# Quoting long strings with tripple quotes

s = """Hello
World
!
"""
print(s)

# Using '''-quoted strings as docstrings.
def f(x):
    '''This function is for ...'''
    return x ** 2
print(help(f))
