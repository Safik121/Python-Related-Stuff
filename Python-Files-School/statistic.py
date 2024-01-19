from random import randint

def statistic(count, lower, upper):
    a = []
    s = 0
    for i in range(1, count + 1):
        x = randint(lower, upper)
        a.append(x)
        s += x
        print(x, end=" ")
        
    print("\n", min(a), end=" - Nejmenší číslo, ")
    print(max(a), end=" - Největší číslo, ")
    print(s/count, end=" - Průměr" )

print(statistic(10,1,100))
