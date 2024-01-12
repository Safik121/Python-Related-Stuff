def convert_10_to_x(n, symbols):
    if symbols == "01":
        r = ""
        for x in range(n.bit_length() - 1, -1, -1):
            tmp = pow(2, x)
            if n >= tmp:
                n -= tmp
                r += "1"
            else:
                r += "0"
        print(r)
    elif symbols == "0123":
        r = ""
        while n > 0:
            r = str(n % 4) + r
            n = n // 4
        print(r)
    elif symbols == "0123456789":
        print(str(n))
    elif symbols == "0123456789ABCDEF":
        hex_characters = "0123456789ABCDEF"
        r = ""
        while n > 0:
            r = hex_characters[n % 16] + r
            n = n // 16
        print(r)


convert_10_to_x(468, "0123456789ABCDEF")
