from random import *

def random_list(n,x=100):
    pole = []
    for i in range(n):
        pole.append(randint(1,x))
    return pole


def bubble_sort(pole):
    n = len(pole)
    for i in range(n):
        for j in range(0,n-i-1):
            if pole[j] > pole[j+1]:
                pole[j], pole[j+1] = pole[j+1],pole[j]
        print(pole)

x = random_list(5,65)
bubble_sort(x)
