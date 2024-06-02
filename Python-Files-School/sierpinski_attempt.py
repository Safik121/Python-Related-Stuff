from turtle import Turtle

julie = Turtle()
julie.speed(10000000)

def sierpinski_triangle(depth: int, length: float = 180.0) -> None:
    if depth == 0:
        for _ in range(3):
            julie.forward(length)
            julie.left(120)
    else:
        sierpinski_triangle(depth - 1, length / 2) 
        julie.forward(length)
        sierpinski_triangle(depth - 1, length / 2) 
        julie.left(120)
        julie.forward(length)
        julie.right(120)
        sierpinski_triangle(depth - 1, length / 2) 
        julie.left(120)
        julie.forward(length)
        julie.left(120)

julie.penup()
julie.goto(-180, -150)
julie.pendown()

sierpinski_triangle(4)
