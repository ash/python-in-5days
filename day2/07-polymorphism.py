# A classical example of demonstrating polymorphism.
# The three shapes, Circle, Square, and Triangle, are all children
# of the Shape class.
class Shape:
    def draw(self):
        print('Drawing a generic shape.')

class Cirle(Shape):
    # Each method defines its own 'draw' method
    def draw(self):
        print('Drawing a circle.')

class Square(Shape):
    def draw(self):
        print('Drawing a square.')

class Triangle(Shape):
    def draw(self):
        print('Drawing a triangle.')

class Escher(Shape):
    pass

# Now we create a universal list that keeps a few objects of different types.
storage = []
storage.append(Cirle())
storage.append(Cirle())
storage.append(Square())
storage.append(Triangle())
storage.append(Square())

# There is no 'draw' method in this class, so the base class will draw it.
storage.append(Escher())

for obj in storage:
    # print(type(obj))
    # On each iteration, obj points to instances of different classes.
    # On each of them, you can cal the 'draw' method.
    obj.draw()
