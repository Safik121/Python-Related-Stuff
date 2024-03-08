def unique_check(listx):
    mnozina = set()
    for i in listx:
        if not i in mnozina:
            mnozina.add(i)
        else:
            return False
    return True

print(unique_check([9, 1, 5, 6, 9, 3]))
