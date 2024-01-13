def double_all(numbers):
    for i in range(len(numbers)):
        numbers[i] *= 2
    print(numbers)

def create_doubled(numbers):
    b = []
    for i in numbers:
        b.append(i * 2)
    print(b)
    print(numbers)

double_all([1, 2, 3, 4, 5])
create_doubled([1, 2, 3, 4, 5])
