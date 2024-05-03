from math import pi

class Triangle:
    def __init__(self, side1, side2, side3) -> None:
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    
    def get_perimeter(self):
        return self.side1 + self.side2 + self.side3

    def __str__(self):
        return f"Triangle with sides: {self.side1}, {self.side2}, {self.side3}"

class Square:
    def __init__(self, center, side_length: float) -> None:
        self.center = center
        self.side_length = side_length

    def get_perimeter(self):
        return 4 * self.side_length

    def __str__(self):
        return f"Square with center: {self.center} and side length: {self.side_length}"

class Circle:
    def __init__(self, center, radius: float) -> None:
        self.center = center
        self.radius = radius
    
    def get_perimeter(self):
        return 2 * pi * self.radius

    def __str__(self):
        return f"Circle with center: {self.center} and radius: {self.radius}"

square1 = Square((10, 20), 100)
square2 = Square((0 ,0), 15)
circle = Circle((-130, -130), 100)

for shape in [square1, square2, circle]:
    print(shape)
    print("perimeter:" , shape.get_perimeter())
