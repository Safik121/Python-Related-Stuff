import math

class Circle:
    
    def __init__(self, center: float, radius: float) -> None:
        self.center = center
        self.radius = radius

    def get_perimeter(self) -> float:
        return (2*self.radius*math.pi)

    def get_area(self) -> float:
        return (math.pi*self.radius**2)

    def __str__(self) -> str:
        return "Circle at " + str(self.center) + " with radius of " + str(self.radius)


circle = Circle((20, 20), 10)
print(circle.get_perimeter())
print(circle.get_area())
