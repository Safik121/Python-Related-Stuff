def super_power(base, exp):
    if exp == 0:
        return 1
    elif exp == 1:
        return base
    elif exp % 2 == 0:
        half_power = super_power(base, exp // 2)
        return half_power * half_power
    else:
        half_power = super_power(base, (exp - 1) // 2)
        return half_power * half_power * base

print(super_power(2, 7)) 
