from random import randint, random

def tramvaj(w, n, count):
    a = [0, 0]
    
    for i in range(count):
        q = randint(0, n)
        if n - q > w:
            a[1] += 1
        else:
            a[0] += 1
    
    r = (a[0] / count) * 100
    rr = (a[1] / count) * 100

    print(f"Přijede pozdě: {r:.2f}%")
    print(f"Přijede v čas: {rr:.2f}%")


tramvaj(4, 5, 100)
