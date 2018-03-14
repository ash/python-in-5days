# Quoting strings: single or double quotes are equivalent.
# Choose the one that makes it easy to add quotes inside a string:
s1 = 'single " quote'
s2 = "double ' quotes"

# Escpaing characters with a backslash:
s3 = 'escape \' continue'
print(s3)

# More escaped symbols:
# \n = newline
# \t = tab
# \r = line feed
# \b = bell

# Unicode is OK:
city = 'Zürich'
print(city)

# You can force an encoding if needed:
print(city.encode(encoding='Latin-1'))

# To sort, transform Straßse to strasse:
s = 'Straße'
print(s.casefold())
print(s)

# Create a strings explicitly:
s = str(123)
print(type(s))

# There are also other 'string' types:
# bytes()
# bytearray()

# This is how you concatenate strings:
big_string = "first part " "second part"
big_string = "first part " + "second part"
print(big_string)

# String repetion using *
string1 = "Hello!"
print(string1 * 10)
print(10 * string1)

# When printing a string, make sure all parts are strings:
print('123' + str(456))
print(int('123') + 456)
