# Using variables.

# Creating a new variable and assigning a value to it.

message = 'Hello, World!'
print(message)

# Assigning a new value to the save variable

message = 'Bye'
print(message)

# Variants of names that you can give to variables:

# Not really good unless you understand it (e.g. there is a formula that uses this notation).
# m 
# M

# You can add numbers, but not as the first symbol of a name.
# message1

# Different variants for when you need more than one word to describe a variable.
# Prefer the underscore_lowercase_names.
# anothermessage
# another_message
# anotherMessage
# AnotherMessage
# Another_Message

# In Python 3, you can even use Unicode names:
ZürichStraße = 123
print(ZürichStraße)

# OK but usually is a choice for somr private names
_secret_name

# Avoid double underscores, as it may clash with Python internal keywords.
# __xxx__

# Just not quite visible here.
another__message
