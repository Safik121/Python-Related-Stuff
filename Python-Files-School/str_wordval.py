def word_value(text):
    result = 0
    for i in text.lower():
        result+=ord(i)-96
    print(result)

word_value("AHOJ")
