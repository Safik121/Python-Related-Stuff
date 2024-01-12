from random import randint, random

def coin_flip():
    x = random()
    if x < 0.85:
        return True
    else:
        return False


print(coin_flip())
