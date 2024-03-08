from random import randint

def hot_potato(names, n):
    hraci = names
    while len(hraci) > 1:
        for i in range(n):
            random_num = randint(0, len(hraci)-1)
        print(hraci[random_num], " je venku")
        hraci.pop(random_num)
    print(hraci[0], " je vítěz")

hot_potato(['Marek', 'Petr', 'Josef', 'Adam', 'Maya'], 7)
