# Catching different type of exceptions.
# Each 'except' branch gets a name of the exception.
# The last 'except' will catch all unknown exceptions.
# If there were no exceptions, then the 'else' clause will be executed.
# In either case, the 'finally' block is run.
# The difference between the code in 'finally' and the code after the whole 'try' construct
# is that in the cause of an uncaught exception, the program terminates, and the code after
# 'try' is not run. While the code in 'finally' will be executed.

a = [1, 2, 3]
s = 'a string'

try:
    # 1/2
    s.reverse()
    print(10/0)
    print(a[100])
except ZeroDivisionError:
    print('ZeroDivisionError happened')
except IndexError:
    print('IndexError happened')
except:
    print('Some other exception')
else:
    print('There were no exceptions')
finally:
    print('The "Finally" block')

print('OK done')
