# String methods

# We'll test it on this string:
s = "String_string"

# Make it uppercase
print(s.upper())

# Make the first letter capital
print(s.capitalize())

# Next more method calls:
print(s.upper().lower())
print(s)

# Count the number of substring appearence:
print(s.count('ing'))

# Check if the string ends or begins with a substring:
print(s.endswith('ing'))
print(s.startswith('ing'))

# Find an index of "i" from left or from right:
print(s.index('i'))
print(s.rindex('i'))

# Take the 3rd character (numbering starts with 0)
print(s[3])

# Different checks of the string content:
print(s.isalpha())
print(s.isidentifier())

# Simple formatting: centering in a given width, with optional filling:
print(s.center(80))
print(s.center(80, '*'))

# Align to the left or to the right:
print(s.ljust(80))
print(s.rjust(80))

# Change the case of letters:
print(s.swapcase())

# Get a length of a string:
print(len(s))
print(len(str(123)))

# Remove extra spaces:
print('          abc           '.strip())
print('          abc           '.lstrip())
print('          abc           '.rstrip())
