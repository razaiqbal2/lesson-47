from math import pi

class Polygon:
    def area(self):
        pass  


class Rectangle(Polygon):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Triangle(Polygon):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


class Circle(Polygon):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * (self.radius ** 2)


def main():
    rectangle = Rectangle(5, 10)
    triangle = Triangle(6, 8)
    circle = Circle(7)

    
    print("Area of Rectangle: ", rectangle.area())
    print("Area of Triangle: ", triangle.area())
    print("Area of Circle: ", circle.area())

if __name__ == "__main__":
    main()
