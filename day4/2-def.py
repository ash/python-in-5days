# Demonstrating how you can call a class method not only via 
# an instance but also via the class name, passing the 
# instance as a first parameter.

def f(x):
    print('f(%i)' % x)

class C:
    def f(self, x):
        print('C.f(self, %i)' % x)

f(5)
c = C()
c.f(5)

C.f(c, 5)
