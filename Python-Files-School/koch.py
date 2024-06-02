from turtle import Turtle

julie = Turtle()
julie.speed(1000)
julie.setposition(-190, 0)

def koch(depth: int = 5, size: float = 380.0) -> None:
    if depth == 0:
        julie.forward(size)
    else:
        koch(depth - 1, size / 3)
        julie.left(60)
        koch(depth - 1, size / 3)
        julie.right(120)
        koch(depth - 1, size / 3)
        julie.left(60)
        koch(depth - 1, size / 3)

koch(5)
