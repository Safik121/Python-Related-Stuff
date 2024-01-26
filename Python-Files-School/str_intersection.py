def string_intersection(left, right):
    amnt = min(len(left), len(right))
    leva = left.upper()
    prava = right.upper()
    result = ""
    for i in range(amnt):
        if leva[i] == prava[i]:
            result += prava[i]
    print(result)

string_intersection("Pes", "Kocka")
string_intersection("Zirafa", "Karafa")
