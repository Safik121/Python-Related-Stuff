import math

def divisor_count(n):
    delitele = []
    for x in range(1,n+1):
        if (n%x==0):
            delitele.append(x)
    print(len(delitele))
divisor_count(42)
