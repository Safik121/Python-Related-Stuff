def gcd(a, b):
    x = max(a, b)
    for i in range(x+1, 0, -1):
        if a % i == 0 and b % i == 0:
            return i


print(gcd(42, 21))
