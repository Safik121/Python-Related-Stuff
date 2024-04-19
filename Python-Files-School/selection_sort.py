import math
import sys

def select_sort(arr):
    output = []
    while arr:
        lowest = min(arr)
        arr.remove(lowest)
        output.append(lowest)
    return output


print(select_sort([7, 8, 6, 1, 45, 12, 3, 17]))
