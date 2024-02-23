def freq_analysis(s):
    words = s.split()
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency

dummy = "Monty Python and Monty Python all over here"

print(freq_analysis(dummy))
