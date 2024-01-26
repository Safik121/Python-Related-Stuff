def diff_a(left, right):
    leva = left.lower()
    prava = right.lower()
    result = {1: 0, 2: 0}
    for i in leva:
        if i == "a":
            result[1]+=1
    for i in prava:
        if i == "a":
            result[2]+=1

    if result[1] == result[2]:
        return("Počet a/A je stejný")
    elif result[1] < result[2]:
        return("Počet a/A je větší v pravém stringu")
    elif result[1] > result[2]:
        return("Počet a/A je větší v levém stringu")
print(diff_a("Pes", "Kocka"))
