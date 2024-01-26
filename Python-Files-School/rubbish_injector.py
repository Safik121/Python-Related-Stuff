def rubbish_injector(text, rubbish):
    result = ""
    for i in text:
        result += i+rubbish
    print(result)

rubbish_injector("AHOJ", "X")
