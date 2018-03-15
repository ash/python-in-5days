# Redefining operators for working with classes.
# In this program, we define the behaviour of the following operation:
# x1 + x2,
# where both x1 and x2 are objects of the X class
class X:
    def __init__(self, value):
        self.value = value
    # def __add__(this, that):
    #     return X(this.value + that.value)

    # Use the "magic" names to redefined "+"
    def __add__(self, other):
        return X(self.value + other.value)
    # Or to defined the rules of object stringification
    def __str__(self):
        return str(self.value)

x1 = X(5)
print(x1.value)

x2 = X(6)
x3 = x1 + x2    # --> x1.__add__(x2)
print(x3.value)

print('==%s==' % x3)

# a = 5
# b = 6
# c = a + b
