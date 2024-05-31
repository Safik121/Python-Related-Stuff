def sequence(n):
    if n == 0:
        return 5
    
    return 2 * sequence(n - 1) - 1

print(sequence(0))
print(sequence(1))
print(sequence(2))
print(sequence(3))
