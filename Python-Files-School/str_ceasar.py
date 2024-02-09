def ceasar(text, klic):
    maly_text = text.lower()
    final_text = ""
    for i in text:
        if ord(i)+klic > ord("z"):
            final_text += chr(ord(i)+klic-26)
        else:
            final_text += chr(ord(i)+klic)
    final_text = final_text.upper()
    return final_text


print(ceasar("zirafa", 3))
