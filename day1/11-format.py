# Different variants of how you can use formatting strings
# to make a value look as you want:

n = 1/3
print(n)

# Floating point with two digits after the decimal point
s = 'my number is %.2f' % n
print(s)

# A new versoin of formatting strings, supports both numerical indices and names:
s = 'my numbers ar {name} and {0}'.format(20, name=10)
print(s)


# With the new format, you don't have to repeat the values if you need more than once:
s1 = 'my number is %i, i repeat: %i' % (3, 3)
print(s1)

s2 = 'my number is {0}, i repeat: {0}'.format(3)
print(s2)
