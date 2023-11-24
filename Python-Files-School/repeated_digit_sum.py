import math

def digit_sum(n):
    x = 0
    strN = str(n)
    for i in range(len(strN)):
        docasne = int((strN)[i])
        x += docasne
    if len(str(x)) > 1:
        digit_sum(x)
    else:
        print(x)

digit_sum(99989788879879)
