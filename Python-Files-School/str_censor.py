def censor(text):
    result = ""
    for i in range(len(text)):
        if i%2 != 0:
            result+="X"
        else:
            result+=text[i]
    print(result)

censor("Jmenuji se, Albrecht")
