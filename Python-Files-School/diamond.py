import turtle

diamant = turtle
diamant.speed(0)

def diafunkce(n, side):
    for c in range(n):
        for x in range(n):
            diamant.forward(50)
            diamant.right(side)
        diamant.right(side)


diafunkce(12, 30)
diamant.exitonclick()
