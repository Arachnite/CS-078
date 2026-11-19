
# Brandon Jun // COMSC 078 // Sequences

import math
from datetime import datetime

class GeometricObject:

    def __init__(self, color, filled):

        self.color = str(color)
        self.filled = bool(filled)
        self.dateCreated = datetime.now()

    def getColor(self):

        return self.color

    def setColor(self, color):

        self.color = color

    def getFilled(self):

        return self.filled

    def setFilled(self, filled):

        self.filled = filled

    def getDateCreated(self):

        return self.dateCreated

    def __str__(self):

        returnString = f"A circle was created on {self.dateCreated}\n"
        returnString += f"Color of circle is {self.color}\n"
        returnString += f"Filled: {self.filled}\n"

        return returnString

class Circle(GeometricObject):

    def __init__(self, color, filled, radius):

        super().__init__(color, filled)
        self.radius = float(radius)

    def getRadius(self):

        return self.radius

    def setRadius(self, radius):

        self.radius = radius

    def getArea(self):

        return math.pi * (self.radius ** 2)

    def getPerimeter(self):

        return 2 * math.pi * self.radius

    def __str__(self):

        returnString = super().__str__()
        returnString += f"The radius is {self.radius}\n"
        returnString += f"The area of circle is {self.getArea()}\n"
        returnString += f"The perimeter of circle is {self.getPerimeter()}\n"

        return returnString

class Rectangle(GeometricObject):

    def __init__(self, color, filled, width, height):

        super().__init__(color, filled)
        self.width = float(width)
        self.height = float(height)

    def getWidth(self):

        return self.width

    def setWidth(self, width):

        self.width = width

    def getHeight(self):

        return self.height

    def setHeight(self, height):

        self.height = height

    def getArea(self):

        return self.width * self.height

    def getPerimeter(self):

        return 2 * self.width + 2 * self.height

    def __str__(self):

        returnString = super().__str__()
        returnString += f"The width is {self.width}\n"
        returnString += f"The height is {self.height}\n"
        returnString += f"The area is {self.getArea()}\n"
        returnString += f"The perimeter is {self.getPerimeter()}\n"

        return returnString

def main():
    radius = float(input("Enter the radius of your circle: "))
    circle = Circle("blue", True, radius)
    rectangle = Rectangle("red", False, 4.0, 2.0)

    print(circle)
    print(rectangle)

main()
