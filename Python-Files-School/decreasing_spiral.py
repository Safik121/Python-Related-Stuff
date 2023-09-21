import turtle

spin = turtle
spin.speed(0)

def spinfce(n, angle, step):
        for q in range(n):
            spin.backward(n)
            spin.left(angle)
            n -= step


spinfce(100, 61, 1)
spin.exitonclick()
