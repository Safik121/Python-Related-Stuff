def prime_less_than(limit):
    for x in range(2, limit+1):
        boolin = True
        for i in range(2, x):
            if(x%i==0):
                boolin = False
        if(boolin):
            print(x, end=" ")
prime_less_than(100)
