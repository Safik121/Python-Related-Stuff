def insert_sort(a):
    for i in range(1, len(a)):
        value = a[i]
        j = i - 1
        while j >= 0 and a[j] > value:
            a[j + 1] = a[j]
            a[j] = value
            j -= 1
    return a


a = [5, 2, 4, 6, 1, 3]
print(insert_sort(a))
