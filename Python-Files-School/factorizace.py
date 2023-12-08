def delitele(n):
    divisors = []
    for x in range(2, n):
        while n % x == 0:
            divisors.append(x)
            n //= x
    if n > 1:
        divisors.append(n)
    return divisors

def factorizace(n):
    divisors = delitele(n)
    for i in divisors:
        print(i, end = " ")

factorizace(1024)
