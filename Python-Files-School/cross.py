def cross(n):
    for i in range(n*2-1):
        for x in range(n*2-1):
            if i == x or i == n*2-(x+2):
                print("x", end="")
            else:
                print(" ", end = "")
        print("")
cross(11)
