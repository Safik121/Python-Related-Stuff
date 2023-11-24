import math

def factorial(n):
    c = 1
    i = 1
    while i <= n:
        c *= i
        i+= 1
    print(c)

factorial(5)
