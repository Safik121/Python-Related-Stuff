from turtle import Turtle

julie = Turtle()
julie.speed(1000000000000000000000000000000)

def hilbert_curve(t: Turtle, depth: int, angle: int, length: int) -> None:
    if depth == 0:
        return
    t.right(angle)
    hilbert_curve(t, depth - 1, -angle, length)
    t.forward(length)
    t.left(angle)
    hilbert_curve(t, depth - 1, angle, length)
    t.forward(length)
    hilbert_curve(t, depth - 1, angle, length)
    t.left(angle)
    t.forward(length)
    hilbert_curve(t, depth - 1, -angle, length)
    t.right(angle)

def hilbert(depth: int = 4, right: bool = True, length: int = 10) -> None:
    if right:
        hilbert_curve(julie, depth, 90, length)
    else:
        hilbert_curve(julie, depth, -90, length)

julie.penup()
julie.goto(-180, -180)
julie.pendown()

hilbert()

