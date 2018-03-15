class Person:
    # docstring
    '''This is a class to represent a person with a name and age.'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show(self):
        print('My name is %s, I am %i years old.' % (self.name, self.age))

# print(help(Person))

p = Person('John', 20)
print(p.__dict__)
