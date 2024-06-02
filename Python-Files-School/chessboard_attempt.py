def draw_chessboard(n, m):
    chessboard = ''
    for i in range(n):
        for j in range(m):
            if (i + j) % 2 == 0:
                chessboard += '##'
            else:
                chessboard += '  '
        chessboard += '\n'
    return chessboard
print(draw_chessboard(4, 8))
