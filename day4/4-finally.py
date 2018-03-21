# The difference between the 'finally' block and the code
# after the 'try' block is that the 'finally' block is always
# called, while the code after the 'try' can be not executed
# if an exception wasn't caught.


try:
    #print(1/0)
    n = [1, 2, 3]
    print(n[100])
except ZeroDivisionError:
    print('Division by 0')
finally:
    print('Finally')

print('ok done')
