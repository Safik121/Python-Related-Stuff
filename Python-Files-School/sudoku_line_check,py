def sudoku_line_check(lajna):
    correct_list = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
    if len(lajna) != 9:
        return False
        
    for num in lajna:
        correct_list[num] += 1
    return all(count == 1 for count in correct_list.values())

print(sudoku_line_check([1,2,3,4,5,6,7,8]))
