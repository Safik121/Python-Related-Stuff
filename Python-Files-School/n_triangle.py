def triangle(n):
    trianglevar = []
    for i in range(n):
        pole = []
        for c in range(i+1):
            pole.append(1)
        trianglevar.append(pole)
    return trianglevar

print(triangle(3))
