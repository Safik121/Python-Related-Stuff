def strange_filter(text):
    text = text.lower()
    if len(text)<=2:
        return 0

    start = text[:2]
    for i in range(len(text)-2):
        x=i+2
        if ord(text[x-1])-96 + ord(text[x-2])-96 != ord(text[x])-96:
            start += text[x]
    print(start)

strange_filter("ABCDEIGHO")
