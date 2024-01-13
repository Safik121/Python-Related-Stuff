def flatten(lists):
    b = []
    for i in range(len(lists)):
        for x in lists[i]:
            b.append(x)
    print(b)


flatten([[1,2,3],[4,5,6],[7,8,9]])
