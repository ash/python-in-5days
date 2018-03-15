# Demonstrating how to build a hierarchy. You have a base (or super-) class:
class Ape:
    def __init__(self, age):
        self.age = age
    def show(self):
        print('This ape is %i years old.' % self.age)

# And a child (sub-) class. 
class Person(Ape):
    def __init__(self, name, age):
        # Now a constructor of the base class is called to set the age
        super().__init__(age)
        # Then you continue building your object
        self.name = name

    # This method will replace 'show' from 'Ape' for the 'Person' class        
    def show(self):
        print('My name is %s, I am %i years old.' % (self.name, self.age))

a = Ape(5)
a.show()

p = Person('John', 20)
p.show()

# 'age' is there together with 'name'
#print(p.__dict__) 
