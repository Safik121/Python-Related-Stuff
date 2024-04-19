def triangle(n):
    trianglevar = []
    for i in range(n):
        pole = [1] * (i + 1)
        for c in range(1, i):
            pole[c] = trianglevar[i - 1][c - 1] + trianglevar[i - 1][c]
        trianglevar.append(pole)
    return trianglevar

print(triangle(1))
