def freq_analysis(s):
    frequency = {}
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

dummy = "Monty Python and Monty Python all over here"

print(freq_analysis(dummy))
