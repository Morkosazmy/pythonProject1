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