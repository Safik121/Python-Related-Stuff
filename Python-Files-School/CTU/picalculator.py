#TBD
def leibnizPi(x) -> float:
    c = 1
    vysledek = 4/c
    for i in range(1, x):
        c += 2
        if x%2 == 1:
            vysledek += 4/c
        else:
            vysledek -= 4/c
    return float(vysledek)

def nilakanthaPi(x) -> float:
    c = 0
    vysledek = 3
    for i in range(1, x):
        c+=2
        roznasobeni = 1
        for i in range(c, c+3):
            roznasobeni *= i
        if x%2 == 1:
            vysledek -= (4/roznasobeni)
        elif x%2 == 0:
            vysledek += (4/roznasobeni)
    return float(vysledek)


#print(leibnizPi(2))
print(nilakanthaPi(3))
