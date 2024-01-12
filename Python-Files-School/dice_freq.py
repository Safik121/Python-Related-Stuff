from random import randint


def dice_freq(count):
    results = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

    for i in range(count):
        x = randint(1, 6)
        results[x] += 1

    for a, c in results.items():
        print(f"Číslo {a}: {c}x")


dice_freq(1000)
