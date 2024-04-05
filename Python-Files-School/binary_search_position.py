def binary_search_position(needle, haystack):
    left, right = 0, len(haystack) - 1

    while left <= right:
        mid = (left + right) // 2
        if haystack[mid] == needle:
            return mid
        elif haystack[mid] < needle:
            left = mid + 1
        else:
            right = mid - 1

    return -1

print(binary_search_position(5, [1, 2, 5, 8]))
