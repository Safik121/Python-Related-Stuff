def fibbonaci(n):
    a = 0
    b = 1
    for i in range(n):
        c = a + b
        a = b
        b = c
        print(b)


fibbonaci(10)
