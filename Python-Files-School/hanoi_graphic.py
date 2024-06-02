def vykresli_veze(veze, pocet_kotoucu):
    max_vyska = pocet_kotoucu
    sloupce = {'A': [], 'B': [], 'C': []}

    for tyc in veze:
        sloupce[tyc] = [" " * (pocet_kotoucu * 2 - 1)] * (max_vyska - len(veze[tyc])) + [
            "#" * (2 * kotouc - 1) for kotouc in reversed(veze[tyc])
        ]

    for i in range(max_vyska):
        for tyc in 'ABC':
            if len(sloupce[tyc]) > i:
                print(f"{sloupce[tyc][i].center(pocet_kotoucu * 2)}", end=' ')
            else:
                print(" " * (pocet_kotoucu * 2), end=' ')
        print()

    print("  " + "-----  " * 3)
    print("   A      B      C  \n")


def hanoi(pocet: int, zdroj: str, cil: str, pomocna: str, veze, pocet_kotoucu) -> None:
    if pocet == 1:
        print(f"{zdroj} -> {cil}")
        veze[cil].append(veze[zdroj].pop())
        vykresli_veze(veze, pocet_kotoucu)
        return
    hanoi(pocet - 1, zdroj, pomocna, cil, veze, pocet_kotoucu)
    print(f"{zdroj} -> {cil}")
    veze[cil].append(veze[zdroj].pop())
    vykresli_veze(veze, pocet_kotoucu)


    hanoi(pocet - 1, pomocna, cil, zdroj, veze, pocet_kotoucu)

pocet_kotoucu = 3
veze = {'A': list(range(pocet_kotoucu, 0, -1)), 'B': [], 'C': []}
vykresli_veze(veze, pocet_kotoucu)
hanoi(pocet_kotoucu, 'A', 'C', 'B', veze, pocet_kotoucu)
