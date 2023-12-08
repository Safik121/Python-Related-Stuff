def primt_c(limit):
    num = 2
    count = 0

    while True:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            print(num, end=" ")
            count += 1
            if count == limit:
                break
        num += 1

primt_c(2)

