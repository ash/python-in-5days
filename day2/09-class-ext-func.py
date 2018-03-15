# Having an increment operation as an 'external' function (not the member of the class):
class X:
    def __init__(self, value):
        self.value = value

def inc_value(self):
    self.value += 1

x = X(42)
inc_value(x)
# vs. x.inc_value()
print(x.value)

# The same, but now inc_value is in the class
class Y:
    def __init__(self, value):
        self.value = value

    def inc_value(self):
        self.value += 1

# The difference between the two approaches is how you pass x to the function (or method).
y = Y(42)
# invocant
y.inc_value()
# vs. inc_value(y)
print(y.value)

