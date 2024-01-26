def rubbish_injector(text, rubbish):
    result = ""
    for i in range(len(text)-1):
        result += text[i] + rubbish
    result += text[-1]
    print(result)

rubbish_injector("AHOJ", "X")
