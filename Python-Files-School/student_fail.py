from random import randint, random
def student(n,count):
    a = {
        "dá":0,
        "nedá":0
    }
    for i in range(count):
        lst=[0,0]
        for i in range(n):
            if randint(1,4) == 1:
                lst[1] += 1
            else:
                lst[0] += 1 
        if lst[1] >= n/2:
            a["dá"] += 1
        else:
            a["nedá"] += 1
    print(a)

student(10, 100)
