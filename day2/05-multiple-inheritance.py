# The C class is a child of both B1 and B2.
# In this case, the 'whoami' method, which you call on C,
# will be transferred to the method of B1 or B2 depending 
# on the order of base classes, so
# class C(B1, B2) and 
# class C(B2, B1)
# work differently.

# The term for this topic: "method resolution order", MRO

class B1:
    def whoami(self):
        print('B1')

class B2:
    def whoami(self):
        print('B2')

#class C(B2, B1):
class C(B1, B2):
    pass

b1 = B1()
b2 = B2()
b1.whoami()
b2.whoami()

c = C()
c.whoami()