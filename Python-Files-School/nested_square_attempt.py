def draw_nested_square(num_squares):
    size = num_squares * 10 + 1
    square = [[' ' for _ in range(size)] for _ in range(size)]

    for i in range(size):
        for j in range(size):
            if i == 0 or i == size - 1 or j == 0 or j == size - 1:
                square[i][j] = '*'

    for k in range(5, size, 10):
        for i in range(k // 2, size - k // 2):
            for j in range(k // 2, size - k // 2):
                if i == k // 2 or i == size - k // 2 - 1 or j == k // 2 or j == size - k // 2 - 1:
                    square[i][j] = '*'

    return '\n'.join([''.join(row) for row in square])


num_squares = 3  
nested_square = draw_nested_square(num_squares)
print(nested_square)
