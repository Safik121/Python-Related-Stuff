def suda_cisla(n):
    for x in range(0, n*2+1):
        if x%2 != 0 or x==0:
            print()
        else:
            print(x, end="")


suda_cisla(15)
