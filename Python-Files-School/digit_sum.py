import math

def digit_sum(n):
    x = 0
    strN = str(n)
    for i in range(len(strN)):
        docasne = int((strN)[i])
        x += docasne
    print(x)

digit_sum(270)
