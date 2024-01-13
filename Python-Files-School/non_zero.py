def nonzero_numbers(numbers):
    x = 1
    while 0 in numbers:
        numbers.remove(0)
    for i in numbers:
        x *= i
    print(x)

nonzero_numbers([0, 2, 3, 0, 0, 3])
nonzero_numbers([0, 0, 0])
