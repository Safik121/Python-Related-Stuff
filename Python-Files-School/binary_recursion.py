def binary_search(value, numbers, left=0, right=None):
    if right is None:
        right = len(numbers) - 1

    if left > right:
        return False

    mid = (left + right) // 2

    if numbers[mid] == value:
        return True
    elif numbers[mid] < value:
        return binary_search(value, numbers, mid + 1, right)
    else:
        return binary_search(value, numbers, left, mid - 1)


print(binary_search(5, [1, 2, 5, 8]))
print(binary_search(4, [1, 2, 5, 8]))
