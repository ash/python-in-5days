# Exceptions.

print('Start')

status = 'unknown'

# If an exception happens inside the 'try' block, 
# it can be caught in the 'except' block.
try:
    print(1)
    print(10/0)
    print(2)
    status = 'done'
except:
    print('Exception happened')
    status = 'error'

# The program can safely continue here.
print('OK done')
print(status)
