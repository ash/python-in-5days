# Demonstrating how you can use the new formatting syntax to print the values from a dictionary

data = {
    'name':'John', 
    'amount':50000.33,
    'acc':'INND23333'
}

print(data)
template = 'Dear {name}, please transfer €{amount} to my bank account {acc}'
# format(name='John', amount=50000.33, acc='INND23333')

# Notice the ** flattenning stars:
print(template.format(**data))
