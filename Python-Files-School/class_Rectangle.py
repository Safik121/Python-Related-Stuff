class Rectangle:
    def __init__(self, a: float, b: float) -> None:
        self.a = a
        self.b = b

def area(rectangle: Rectangle) -> float:
    rectangle = Rectangle(4, 3)
    return rectangle.a * rectangle.b

print(area(Rectangle))
