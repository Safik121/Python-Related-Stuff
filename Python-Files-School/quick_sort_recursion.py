from typing import List

def partition(array: List[int], low: int, high: int) -> int:
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1

def quick_sort_in_place(array: List[int], low: int, high: int) -> None:
    if low < high:
        pi = partition(array, low, high)
        quick_sort_in_place(array, low, pi - 1)
        quick_sort_in_place(array, pi + 1, high)

def quick_sort(array: List[int]) -> List[int]:
    array_copy = array[:]
    quick_sort_in_place(array_copy, 0, len(array_copy) - 1)
    return array_copy

print(quick_sort([2, 7, 8, 1, 4, 5, 9, 3, 6]))
