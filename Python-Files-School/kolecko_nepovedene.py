def circle(r):
    plocha = r*2+1
    for delka in range(plocha):
        print("")
        for sirka in range(plocha):
            if delka == 0 or delka == plocha - 1:
                print(".", end=" ")
            elif sirka == 0 or sirka == plocha - 1:
                print(".", end = " ")
            else:
                if delka == 1 and sirka == 0 or delka == 1 and sirka == 1 or delka == 1 and sirka == 2 or delka == 1 and sirka == plocha - 1 or delka == 1 and sirka == plocha-2 or delka == 1 and sirka == plocha - 3:
                    print(".", end = " ")
                elif delka == 2 and sirka == 0 or delka == 2 and sirka == 1 or delka == 2 and sirka == plocha - 1 or delka == 2 and sirka == plocha-2:
                    print(".", end = " ")
                elif delka == 3 and sirka == 0 or delka == 3 and sirka == plocha - 1:
                    print(".", end = " ")

                elif delka == plocha - 2 and sirka == 0 or delka == plocha - 2 and sirka == 1 or delka == plocha - 2 and sirka == 2 or delka == plocha - 2 and sirka == plocha - 1 or delka == plocha - 2 and sirka == plocha - 2 or delka == plocha - 2 and sirka == plocha - 3:
                    print(".", end = " ")
                elif delka == plocha - 3 and sirka == 0 or delka == plocha - 3 and sirka == 1 or delka == plocha - 3 and sirka == plocha - 1 or delka == plocha - 3 and sirka == plocha - 2:
                    print(".", end = " ")
                elif delka == plocha - 4 and sirka == 0 or delka == plocha - 4 and sirka == plocha - 1:
                    print(".", end = " ")
                else:
                    print("x", end = " ")

circle(5)
