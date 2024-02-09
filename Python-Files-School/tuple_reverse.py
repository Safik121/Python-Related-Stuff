import math

def tuple_reverse(text, klic):
    c = []
    x = (math.ceil(len(text) / 3))
    str_empty = ""
    idk = 0
    dk = klic
    for i in range(x):
        for l in range(dk - 1, idk - 1, -1):
            if 0 <= l < len(text):
                str_empty += text[l]
        idk += 3
        dk += 3
    return str_empty

print(tuple_reverse("HESLOJETAJEMNO", 3))
