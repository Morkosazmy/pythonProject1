from abc import ABC, abstractmethod
import math
class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled
    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")

class Circle(Shape):
    def __init__(self, color,is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius
    def describe(self):
        print(f"It is a {self.color} circle with an area of {math.pi * pow(self.radius,2):.2f} cm^2")
        super().describe()

class Square(Shape):
    def __init__(self, color,is_filled, width):
        super().__init__(color, is_filled)
        self.width = width
    def describe(self):
        print(f"It is a {self.color} square with an area of {self.width * self.width:.2f} cm^2")
        super().describe()
        
class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height
    def describe(self):
        print(f"It is a {self.color} Triangle with an area of {self.width * self.height:.2f} cm^2")
        super().describe()

class Rectangle(Shape):
    def __init__(self, color, is_filled, width, length):
        super().__init__(color, is_filled)
        self.width = width
        self.length = length
    def describe(self):
        print(f"It is a {self.color} Rectangle with an area of {self.width * self.length:.2f} cm^2")
        super().describe()