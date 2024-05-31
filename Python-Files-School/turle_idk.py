import math
from random import randint

class Turtle:
    def __init__(self) -> None:
        self.x = randint(0, 500)
        self.y = randint(0, 500)
        self.direction = 0
        self.lines = []
        self.color = "black"

    def left(self, angle: float) -> None:
        self.direction -= angle

    def right(self, angle: float) -> None:
        self.direction += angle

    def forward(self, distance: float) -> None:
        nx = self.x + distance * math.cos(self.direction * math.pi / 180)
        ny = self.y + distance * math.sin(self.direction * math.pi / 180)

        self.lines.append((self.x, self.y, nx, ny, self.color))
        self.x, self.y = nx, ny

    def draw_polygon(self, sides: int, side_length: float) -> None:
        angle = 360 / sides
        for _ in range(sides):
            self.forward(side_length)
            self.left(angle)

    def get_lines_svg(self) -> str:
        svg = ""
        for x1, y1, x2, y2, color in self.lines:
            svg += f"""\t<line x1='{x1}' y1='{y1}' x2='{x2}' y2='{y2}'
                style='stroke: {color}; stroke-width:2' />\n"""
        return svg

    def save(self, filename: str) -> None:
        with open(filename, "w") as f:
            f.write('<svg width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" xmlns:xlink= "http://www.w3.org/1999/xlink">\n')
            f.write(self.get_lines_svg())
            f.write("\n</svg>")


turtle1 = Turtle()

turtle1.color = "blue"
turtle1.draw_polygon(3, 70)

turtle1.save("colored_shapes.svg")
