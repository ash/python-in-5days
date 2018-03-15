class C:
    # You can also keep some data on the level of the class, not objects.
    # This variable is the same for each instance of this class
    a = 42

    def __init__(self, value):
        # This time, self.a belongs to the object.
        self.a = value
        
    def show(self):
        print(self.__dict__)
        print(self.a)
        print(C.a)
    
    def modify(self, new_value):
        C.a = new_value
    
c = C(1)
# You are modifying the class attribute, not the object attribute
c.modify(55)
c.show()

d = C(3)
# So you will see 55 here, too.
d.show()