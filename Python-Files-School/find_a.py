def find_a(text):
    low_text = text.lower()
    result = 0
    for i in low_text:
        if i == "a":
            result+=1
    print(result)

find_a("Liska Adelka")
