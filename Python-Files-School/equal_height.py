def equal_height(vez):
    while not check_height(vez):
        maxval = 0
        for i in vez:
            if(sum(i)>maxval):
                maxval = sum(i)
        for x in vez:
            if(sum(x) == maxval):
                del x[-1]
    return vez

def check_height(pole):
    if not pole:
        return True
    first_height = sum(pole[0])
    for tower in pole:
        if sum(tower) != first_height:
            return False
    return True

print(equal_height([[1,1,1,2,3],[2,3,4],[1,4,1,1]]))
