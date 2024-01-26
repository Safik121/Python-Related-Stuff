def plaindrome_val(text):
    text2 = ""

    for i in range(len(text)-1, -1, -1):
        text2 += text[i]
    if text2.lower() == text.lower():
        return("Je to palindrom")
    else:
        return("Není palindrom")

print(plaindrome_val("XDX"))
