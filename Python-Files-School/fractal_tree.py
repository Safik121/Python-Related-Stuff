from turtle import Turtle

julie = Turtle()
julie.speed(10)
julie.left(90)

def tree(length: float) -> None:
    if length < 5:  
        return
    else:
        julie.forward(length)
        julie.left(30)
        tree(length * 0.7)
        julie.right(60)
        tree(length * 0.7)
        julie.left(30)
        julie.backward(length)

tree(90)
