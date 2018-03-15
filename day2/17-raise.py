# You can also raise an exception yourself:
def f(n):
    print('I am f(%i)' % n)
    if n > 10:
        # Optionally, you can pass a message along:
        raise Exception('my message')
    else:
        print('Indexing an existing element')

f(2)
try:
    f(11)
# If you have a message, you can read it here via the 'e' variable.
# If you don't need it, you can omit the 'as e' part.
except Exception as e:
    print('oops: ' + str(e))
f(3)
