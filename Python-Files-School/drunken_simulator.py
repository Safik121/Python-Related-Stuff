from random import randint

def drunken_simulator(size,steps):
    x = 0
    m = int(size/2)
    while x < steps:
        if randint(1,2) == 1:
            m -= 1
        else:
            m += 1
        if m == 0:
            return("Došel domů!")
        elif m == size:
            return("Došel do hospody!")
        x+=1
    return("nedošel")

print(drunken_simulator(10, 100)) 
