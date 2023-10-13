def table_products(n):
    prvni_var = 1
    for c in range(1, n+1):
        for i in range(1, n+1):
            if c%2 == 0:
                if i%2 == 0:
                    print("#", end=" ")
                else:
                    print(".", end=" ")
            else:
                if i%2 == 0:
                    print(".", end=" ")
                else:
                    print("#", end=" ")
        print("")

table_products(8)
