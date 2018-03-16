def myfunc():
    print('I am myfunc() im mymodule.py')

def s(a, b):
    return a + b

if __name__ == '__main__':
    if s(3, 4) == 7:
        print('OK')
    else:
        print('Not OK')
