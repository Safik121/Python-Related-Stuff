from random import randint

def game(n):
    out = ""
    for _ in range(n):
        x = randint(1, 4)
        for i in range(x):
            if i%2==0:
                out = "Má mě ráda"
            else:
                out = "Nemá mě ráda"
    return out

print(game(5))
