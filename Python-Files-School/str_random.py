from random import randint

def random_string(length, chars):
    result = ""
    for i in range(length):
        nahodicka = randint(0, len(chars)-1)
        result += chars[nahodicka]
    return result

print(random_string(10, "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"))
