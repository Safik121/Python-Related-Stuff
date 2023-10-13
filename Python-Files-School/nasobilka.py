def table_products(n):
    prvni_var = 1
    druha_var = 0

    print("     ", end="")
    for i in range(n):
        print(prvni_var+i, end=" ")
    print("")
    print("     ", end="")
    for o in range(n):
        print("-", end=" ")
    print("")
    for p in range(1+druha_var, (n+1)*prvni_var, prvni_var):
        print(p, " / ", end="")
        for s in range(1+druha_var, (n+1)*prvni_var, prvni_var):
            print(s, end=" ")
        print("")
        druha_var+=1
        prvni_var+=1
table_products(5)
