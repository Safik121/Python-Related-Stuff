def convert_2_to_10(n):
    x = []
    c = 0
    for index, b in enumerate(n[::-1]):
        x.append((int(b), index))

    for cislo in x:
        if cislo[0] == 1:
            c += pow(2, cislo[1])
    return c



print(convert_2_to_10("11"))
