def vigenere(text, klic):
    c = 0
    final_text = ""
    text = text.lower()
    for i in range(len(text)):
        if c > len(klic)-1:
            c = 0
        if (ord(text[i])+ord(klic[c])) > ord("z"):
            final_text += chr(ord(text[i])+ord(klic[c])-97)
        else:
            final_text += chr(ord(text[i]) + ord(klic[c]))

        c += 1
    return final_text.upper()

print(vigenere("pampeliska", "klic"))
