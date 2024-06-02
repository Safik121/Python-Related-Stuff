from typing import List, Tuple


def min_max(numbers: List[int]) -> Tuple[int, int]:
    def recursive_min_max(low: int, high: int) -> Tuple[int, int]:
        if low == high:
            return numbers[low], numbers[low]
        elif high == low + 1:
            return (min(numbers[low], numbers[high]), max(numbers[low], numbers[high]))
        else:
            mid = (low + high) // 2
            left_min, left_max = recursive_min_max(low, mid)
            right_min, right_max = recursive_min_max(mid + 1, high)
            return (min(left_min, right_min), max(left_max, right_max))

    return recursive_min_max(0, len(numbers) - 1)

print(min_max([8, 4, 3, 5, 9, 2, 1, 7, 6]))
