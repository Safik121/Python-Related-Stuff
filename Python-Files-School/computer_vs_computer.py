import random

def computer_vs_computer(limit):
    number_to_guess = random.randint(1, limit)
    low = 1
    high = limit
    attempts = 0

    print(f"Počítač 1 si myslí číslo mezi 1 a {limit}. Počítač 2 se pokusí ho uhodnout.")

    while low <= high:
        attempts += 1
        guess = (low + high) // 2
        print(f"Počítač 2 hádá: {guess}")

        if guess == number_to_guess:
            print(f"Počítač 2 uhodl číslo {guess} po {attempts} pokusech.")
            return
        elif guess < number_to_guess:
            print("Počítač 1 říká: Moje číslo je větší.")
            low = guess + 1
        else:
            print("Počítač 1 říká: Moje číslo je menší.")
            high = guess - 1


computer_vs_computer(100)
