class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

def distance(point1: Point, point2: Point) -> float:
    vector2 = (point1.x - point2.x, point1.y - point2.y)
    magnitude = math.sqrt(vector2[0]**2 + vector2[1]**2)
    return magnitude

print(distance(Point(1, 2), Point(3, 5)))
