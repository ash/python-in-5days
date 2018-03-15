# In the previous example, we were raising a built-in exception.
# But you also can create your own exception class and derive it from 'Exception'.

class MyException(Exception):
    pass

def f():
    raise MyException('messge')

f()
