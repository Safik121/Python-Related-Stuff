def table_products(r):
    min_val = 0
    max_val = r*2
    for i in range(r*2+1):
        for c in range(r*2+1):
            if i == min_val:
                print(".", end=" ")
            elif c > min_val and c < max_val:
                print("x", end=" ")
            else:
                 print(".", end=" ")
        print("")

table_products(5)
