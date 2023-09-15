import turtle

# Ctverec pomoci funkce
t = turtle

def ctvercovia_funkcia(strana_a, direction, uhel):
    for i in range(4):
        t.forward(strana_a)
        direction(uhel)

ctvercovia_funkcia(100, t.right, 90)

# Pentagon pomoci funkce
def pentagonik_funkcia(strana, direkcia, uhel):
    for i in range(5):
        t.forward(strana)
        direkcia(uhel)

pentagonik_funkcia(100, t.left, 72)
t.exitonclick()
