# An exampe of using a class data attribute as a counter
# that keeps track of the number of created objects.
class X:
    counter = 0

    def __init__(self):
        X.counter += 1
        # We also save the number in the object itself, so that later we can see its sequential number
        self.my_number = X.counter
        
    def howmany(self):
        print("There are %i objects of this type, and I am number %i" % (X.counter, self.my_number))

x = X()
y = X()
z = X()

y.howmany()
z.howmany()