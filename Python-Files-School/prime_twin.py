def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if(n%i==0):
            return False
    return True

def prime_twins(n):
    count = 0
    num = 2
    while count < n:
        if is_prime(num) and is_prime(num+2):
            print(num, "-", num+2)
            count += 1
        num += 1
        
prime_twins(5)
