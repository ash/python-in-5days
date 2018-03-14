# More on dictionaries
d = {'France': 'Paris', 'UK': 'London'}

# You can check if the key is in a dictionary:
if 'Spain' in d:
    print(d['Spain'])

if 'France' in d:
    print(d['France'])
    
# Use the .get metod to avoid exceptions if the element was not found:
print(d.get('Spain'))
print(d.get('France'))

# Removing a key and the corresponding velue:
# del d['UK']
# print(d)

# Remove and return the given element:
# print(d.pop('UK'))
# print(d)

# Remove and return an arbitrary (whatever that means) element:
#print(d.popitem())

# This is how you can merge dictionaries:
d.update({'Germany': 'Berlin'})
print(d)

g = {'Germany': 'Bonn'}
d.update(g)
print(d)