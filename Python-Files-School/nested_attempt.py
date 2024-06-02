from turtle import Turtle, Screen

def draw_square(t: Turtle, length: float) -> None:
    for _ in range(4):
        t.forward(length)
        t.right(90)

def nested_squares(t: Turtle, depth: int, length: float = 180.0) -> None:
    if depth == 0:
        return
    draw_square(t, length)

    t.penup()
    t.forward(length / 10)
    t.right(90)
    t.forward(length / 10)
    t.left(90)
    t.pendown()
    nested_squares(t, depth - 1, length * 0.8)

screen = Screen()
julie = Turtle()
julie.speed(10)

nested_squares(julie, 8)

screen.exitonclick()
