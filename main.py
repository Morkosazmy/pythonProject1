#@Property ( getter "@property", setter "@x.setter", deleter "@x.deleter" )
from pprint import pprint
from shutil import which


class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height
        # the ' _ ' refers to the attributes are protected and shall only be used within the class itself

    @property
    def width(self):
        return f"{self._width:.1f} cm"

    @property
    def height(self):
        return f"{self._height:.1f} cm"

    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be greater then zero !")

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Height must be greater than zero")

    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted")

    @height.deleter
    def height(self):
        del self._height
        print("Height has been deleted")

rectangle = Rectangle(3, 4)

print(rectangle.width)
print(rectangle.height)

rectangle.width = 5
rectangle.height = 6

pprint('')

print(rectangle.width)
print(rectangle.height)

del rectangle.width
del rectangle.height