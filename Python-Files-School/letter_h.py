import math

def h_letter(n):
    for i in range(n):
        for j in range(n):
            if j == 0 or j == n-1 or i == math.floor(n/2):
                print("#", end = " ")
            else:
                print(" ", end=" ")
        print("")

h_letter(9)
