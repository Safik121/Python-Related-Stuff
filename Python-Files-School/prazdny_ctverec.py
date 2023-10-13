def table_products(n):
    prvni_var = 1
    for c in range(n):
        for i in range(n):
            if c == n-1 or c == 0 or i == n-1 or i == 0:
                print("#", end=" ")
            else: 
                print(".", end=" ")
        print("")
table_products(5)
