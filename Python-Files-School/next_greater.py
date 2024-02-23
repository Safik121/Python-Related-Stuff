def next_greater(lst):
    maxnum = len(lst)
    output = []
    for i in range(maxnum):
        if(i == maxnum-1 or lst[i]>lst[i+1]):
            x = i+1
            while x > i and x < maxnum:
                if (lst[i]<lst[x]):
                    carr = (lst[i], lst[x])
                    output.append(carr)
                    break
                else:
                    x+=1
            else:
                carr = (lst[i], "None")
                output.append(carr)
        else:
            carr = (lst[i], lst[i+1])
            output.append(carr)
    return output


print(next_greater([13,7,6,12]))
