def table_products(n):
    max_delka = 2 * n - 1

    for i in range(n):
        pocet_krizku = 2 * i + 1
        mezery = (max_delka - pocet_krizku) // 2

        for j in range(mezery):
            print(" ", end=" ")

        for k in range(pocet_krizku):
            print("#", end=" ")

        print("")

table_products(5)
