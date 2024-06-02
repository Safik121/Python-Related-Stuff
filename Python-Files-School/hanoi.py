def hanoi(pocet: int, zdroj: str, cil: str, pomocna: str) -> None:
    if pocet == 1:
        print(f"{zdroj} -> {cil}")
        return
    hanoi(pocet - 1, zdroj, pomocna, cil)
    print(f"{zdroj} -> {cil}")
    hanoi(pocet - 1, pomocna, cil, zdroj)

hanoi(3, 'A', 'C', 'B')
