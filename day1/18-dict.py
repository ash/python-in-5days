# An example of a dictionary with nested dictionaries:
countries = {
    'France' : {
        'capital' : 'Paris',
        'continent' : 'Europe',
        'cities': ['Paris', 'Lyon']
    },
    'UK' : {
        'capital' : 'London',
        'continent' : 'Europe',
    },
}

# Just chain the [] operation:
print(countries)
print(countries['France']['continent'])
print(countries['France']['cities'][1])
