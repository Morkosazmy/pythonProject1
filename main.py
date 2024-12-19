"""
from http.client import CannotSendRequest

import Shapes
from Shapes import Circle, Square, Triangle, Rectangle

circle = Circle("Red", True, 5)
square = Square("Blue", True, 4)
triangle = Triangle("Violet", False, 6, 5)
rectangle = Rectangle("Green",True,3,4)

circle.describe()
square.describe()
triangle.describe()
rectangle.describe()

"""
from abc import ABC, abstractmethod

class Shape:

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self,side):
        self.side = side

    def area(self):
        return self.side ** 2

class Triangle(Shape):
    def __init__(self,base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height * 0.5

class Pizza(Circle):
    def __init__(self, topping, radius):
        super().__init__(radius)
        self.topping = topping


Shapes = [Circle(4), Square(5), Triangle(6,7), Pizza("Pepperoni", 4)]

for shape in Shapes:
    print(f"Area of shape = {shape.area()}cm²")