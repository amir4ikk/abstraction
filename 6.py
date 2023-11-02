import math

class Shape:
    def area(self):
        pass

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

triangle = Triangle(4, 5)
square = Square(3)
circle = Circle(2)

print("Area of Triangle:", triangle.area())
print("Area of Square:", square.area())
print("Area of Circle:", circle.area())
