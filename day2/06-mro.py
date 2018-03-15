# A bit more on MRO, now we have another layer in the heirarchy,
# namely, B is a parent for both B1 and B.
class B:
    def whoami(self):
        print('B')

class B1(B):
    pass

class B2(B):
    def whoami(self):
        print('B2')

class C(B1, B2):
    pass

c = C()
c.whoami()
