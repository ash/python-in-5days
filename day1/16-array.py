# Reverse sortring by providing a 'reverse' named parameter:
a = [3, 5, 6, 1, 3, 7, 8, 9, 10, 1]
a.sort(reverse=True)
print(a)

# This will sort a list so that capital names go the the beginning:
s = ['alpha', 'Beta', 'gamma', 'Delta']
s.sort()
print(s)

# To use alphabetic sorting, add a sorting function, so you will have alpha, Beta, etc. instaed
s.sort(key=str.lower)
print(s)

# Make a list empty
s.clear()
print(s)