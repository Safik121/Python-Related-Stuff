def lcm(a, b):
    for i in range(1, a * b + 1):
        if i % a == 0 and i % b == 0:
            print(i, end=" ")
            return


lcm(3, 9)
