# Data type: dictionary

# A dictionary is a collection of key-value pairs:
d = {'France': 'Paris', 'UK': 'London'}

# You access values via keys:
print(d['France'])


# This is how you can imitate the same behavior with pure lists:
countries = ['France', 'UK']
capitals = ['Paris', 'London']
print(capitals[countries.index('France')])


# Repeating a key replaces the value:
e = {'France': 'Paris', 'UK': 'London', 'France': 'Zürich'}
e['France'] = 'Rome'
print(e['France'])

