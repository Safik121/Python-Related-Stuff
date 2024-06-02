def computer_guess(limit):
    low = 1
    high = limit
    attempts = 0

    print(f"Přemýšlím o čísle mezi 1 a {limit}. Počítač se pokusí ho uhodnout.")

    while low <= high:
        attempts += 1
        guess = (low + high) // 2
        print(f"Počítač hádá: {guess}")
        feedback = input("Je číslo (V)ětší, (M)enší, nebo (S)právné? ").lower()

        if feedback == 's':
            print(f"Počítač uhodl číslo {guess} po {attempts} pokusech.")
            return
        elif feedback == 'v':
            low = guess + 1
        elif feedback == 'm':
            high = guess - 1
        else:
            print("Neplatná odpověď. Zadejte 'V' pro větší, 'M' pro menší nebo 'S' pro správné.")

computer_guess(100)
