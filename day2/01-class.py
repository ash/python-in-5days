# Creating a class

# Use the 'class' keyword and give the class a name
class Person:
    # From this point, you are in a namespaced of the class, and can type any valid Python code.
    # To set the initial state of an object, use a constructor, which is a method called __init__.
    # The first parameter of any class method have to be the 'self' variable (can be called differently).
    def __init__(self, name, age):
        # 'name' and 'age' are data attributes of the object
        self.name = name
        self.age = age
    # Now, the methods of the class. These are like regular functions but with 'self' as the first parameter.
    def show(self):
        print('My name is %s, I am %i years old.' % (self.name, self.age))
    def clone_somebody(self, other):
        self.age = other.age
        self.name = other.name


# Instantiating (=creating an instance) is like creating a variable of on of the built-in types.
# int_var = int(0)
p1 = Person('John', 20)
p2 = Person('Jessica', 19)

print(type(p1)

# Call class methods on the objects
p1.show()
p2.show()

# p1.clone_somebody(p2)
# p1.show()

print('Name =', p1.name)

# You can also acces attributes directly
p2.age += 1
p2.show()
