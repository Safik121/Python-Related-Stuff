from random import randint


def turn():
    count = 0
    while True:
        x = randint(1, 6)
        if x % 2 != 0:
            count += 1
            break
        else:
            count += 1
    return count


print(turn(), turn(), turn())
