import math

def prime(n):
    delitele = []
    for x in range(1,n+1):
        if (n%x==0):
            delitele.append(x)
    if len(delitele) == 2:
        print(True)
    else:
        print(False)
prime(11)
