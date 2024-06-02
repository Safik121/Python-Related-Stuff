import random

def guess_nmumber_human():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guess = None

    print("Myslím si číslo mezi 1 a 100. Zkuste ho uhodnout!")

    while guess != number_to_guess:
        guess = int(input("Zadejte svůj tip: "))
        attempts += 1

        if guess < number_to_guess:
            print("Moje číslo je větší.")
        elif guess > number_to_guess:
            print("Moje číslo je menší.")

    print(f"Gratulace! Uhodli jste číslo {number_to_guess} po {attempts} pokusech.")

guess_nmumber_human()

