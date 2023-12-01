def kth_prime(limit):
    num = 2
    count = 0

    while True:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            count += 1
            if count == limit:
                print(num)
                break
        num += 1

kth_prime(100)
