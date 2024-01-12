def convert_10_to_2(x):
    a=bin(x)
    print(a[2:])

convert_10_to_2(2)

def convert_10_to_2_v2(a):
    r = ""
    for x in range(a.bit_length() - 1, -1, -1):
        tmp = pow(2, x)
        if a >= tmp:
            a -= tmp
            r += "1"
        else:
            r += "0"
    return r

print(convert_10_to_2_v2(7))
