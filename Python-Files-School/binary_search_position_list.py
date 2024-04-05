def binary_search_position_list(needle, haystack):
    left_index, right_index = 0, len(haystack) - 1
    positions = []

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        if haystack[mid_index] == needle:
            positions.append(mid_index)
            left_neighbor = mid_index - 1
            while left_neighbor >= 0 and haystack[left_neighbor] == needle:
                positions.append(left_neighbor)
                left_neighbor -= 1
            right_neighbor = mid_index + 1
            while right_neighbor < len(haystack) and haystack[right_neighbor] == needle:
                positions.append(right_neighbor)
                right_neighbor += 1
            return sorted(positions)
        elif haystack[mid_index] < needle:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1
    return positions

print(binary_search_position_list(5, [1, 2, 3, 3, 5, 5, 8]))
