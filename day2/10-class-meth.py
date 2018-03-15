# This example demonstrate different method of passing an object to the method of the class.
class Y:
    def __init__(self, value):
        self.value = value

    def inc_value(self):
        self.value += 1

y = Y(42)
# invocant
y.inc_value()
# vs. inc_value(y)
print(y.value)


Y.inc_value(y)
print(y.value)

# y.inc_value()
# Y.inc_value(y)

# s = 'abc'
# Y.inc_value(s)