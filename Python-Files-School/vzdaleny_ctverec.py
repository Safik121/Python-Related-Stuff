from random import randint, random
import math

def ctverec(size):
    A = [randint(0,size),randint(0,size)]
    B = [randint(0,size),randint(0,size)]
    vzdalenost = math.sqrt((A[0]-B[0])**2 + (A[1]-B[1])**2)
    print(vzdalenost)

ctverec(5)
