# Powerful slicing:
# [x:y:n]
# x and y are the first and the oen-to-last indices; n is a step (stride)

s = "abcdefg"

print(s[0:2])
print(s[3:5])

print(s[:2])
print(s[3:])

# Make a copy of a string
print(s[:])

print(s[0:7:2])
print(s[::2])

# Each of the numbers can be negative:
print(s[-1])
print(s[0:-2])
print(s[0:-2:2])

print(s[::-1])
print(s[::-2])
