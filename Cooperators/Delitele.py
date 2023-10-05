def divisors(n):
    for x in range(1,n+1,1):
        if (n%x==0):
            print(x)
divisors(14)
