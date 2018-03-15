# Here, we want to add some information about person's education.
# Instead of keeping it in a dictionary or in separate attributes,
# we created a separate class Education, and then use an object of
# this type as one of the attributes of a Person.
class Education:
    def __init__(self, from_year, to_year, level):
        self.from_year = from_year
        self.to_year = to_year
        self.level = level
    def show(self):
        print("From %i to %i, at '%s'." % (self.from_year, self.to_year, self.level))

class Person:
    def __init__(self, name, age, education):
        self.age = age
        self.name = name
        self.education = education
        
    def show(self):        
        print('My name is %s, I am %i years old.' % (self.name, self.age))
        self.education.show()

p =  Person('John', 25, Education(2000, 2005, 'high'))
p.show()
#p.education.show()
# print(p.__dict__)