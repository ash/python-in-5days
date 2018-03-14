# Control flow with "if"

x = 10
y = 20

# Code blocks are indented:
if x < y:
    print('x < y')
    print('yes ok')
else:
    print('x >= y')

# Back to the main scope:
print('all done')

# Adding an else-if branch:
if x < 10:
    print(1)
elif x < 50:
    print(2)
else:
    print(3)

