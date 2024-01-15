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
            return(True)
        elif m == size:
            return(False)
        x+=1
    return(False)

def drunken_analysis(size, steps, count):
    final_c = 0
    for i in range(count):
        if drunken_simulator(size, steps):
            final_c+=1
    procenta = (final_c/count)*100
    return ("Opilec dojde domů za ",  count, " pokusů na ", procenta, "%" )

print(drunken_analysis(10, 100, 100)) 
