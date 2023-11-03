import math

def h_letter(n):
    for i in range(n):
        for j in range(n):
            if j == math.floor(n/2) and i > math.floor(n/2) or i == j and i < n//2+1:
                print("#", end = " ")
            else:
                print(" ", end=" ")
        print("")

h_letter(9)
