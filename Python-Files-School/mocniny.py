def table_products(n):
    prvni_var = 1

    print("    ", end="")
    for i in range(n):
        print(prvni_var+i, end=" ")
    print("")
    print("    ", end="")
    for i in range(n):
        print("-", end=" ")
    print("")
    for i in range(1,n+1):
        print(i,"/ ",end="")
        for x in range(1,n+1):
            print(i**x,end=" ")
        print(" ")
table_products(5)
