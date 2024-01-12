from random import randint


def dice_freq(count):
    results = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}

    for i in range(count):
        x = randint(1, 6)
        y = randint(1, 6)
        results[x+y] += 1

    for a, c in results.items():
        print(f"Číslo {a}: {c}x")


dice_freq(1000)
