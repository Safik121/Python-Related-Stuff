import math

class Circle:
    def __init__(self, x: float, y: float, radius: float, color: str) -> None:
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

def test_circle() -> None:
    circle = Circle(4, 5, 10, 'green')
