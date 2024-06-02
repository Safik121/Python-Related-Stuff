from turtle import Turtle

julie = Turtle()
julie.speed(10)
julie.penup()
julie.setposition(-180, -180)
julie.pendown()


def empty_square(length: float) -> None:
    for _ in range(4):
        julie.forward(length)
        julie.left(90)

def filled_square(length: float) -> None:
    julie.begin_fill()
    for _ in range(4):
        julie.forward(length)
        julie.left(90)
    julie.end_fill()

def sierpinski_carpet(depth: int, length: float) -> None:
    if depth == 0:
        filled_square(length)
    else:
        for _ in range(3):
            for _ in range(3):
                if _ == 1 and _ == 1:
                    julie.penup()
                    julie.forward(length // 3)
                    julie.left(90)
                    julie.forward(length // 3)
                    julie.right(90)
                    julie.pendown()
                else:
                    sierpinski_carpet(depth - 1, length // 3)
                    julie.penup()
                    julie.forward(length // 3)
                    julie.pendown()
            julie.penup()
            julie.backward(length)
            julie.right(90)
            julie.forward(length // 3)
            julie.left(90)
            julie.pendown()

def fractal_cookie(depth: int, length: float) -> None:
    empty_square(length)
    sierpinski_carpet(depth, length)

fractal_cookie(3, 360)
