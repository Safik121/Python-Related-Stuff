def diamant(n):
    for i in range(n*2+1):
        for j in range(n*2+1):
            if i <= n:
                if j < n - i or j > n + i:
                    print(" ", end=" ")
                else:
                    print("#", end=" ")
            else:
                if j < i - n or j > 3 * n - i:
                    print(" ", end = " ")
                else:
                    print("#", end=" ")
        print("")
diamant(9)
