MORSE_CODE = {
    "A": ".-",      "B": "-...",    "C": "-.-.",    "D": "-..",
    "E": ".",       "F": "..-.",    "G": "--.",     "H": "....",
    "I": "..",      "J": ".---",    "K": "-.-",     "L": ".-..",
    "M": "--",      "N": "-.",      "O": "---",     "P": ".--.",
    "Q": "--.-",    "R": ".-.",     "S": "...",     "T": "-",
    "U": "..-",     "V": "...-",    "W": ".--",     "X": "-..-",
    "Y": "-.--",    "Z": "--..",    "1": ".----",   "2": "..---",
    "3": "...--",   "4": "....-",   "5": ".....",   "6": "-....",
    "7": "--...",   "8": "---..",   "9": "----.",   "0": "-----",
}

def encode(txt):
    output = ""
    for char in txt:
        output += MORSE_CODE[char] + ' '
    return output

def decode(code):
    morse_to_char = {value: key for key, value in MORSE_CODE.items()}
    code_words = code.split() 
    decoded_text = ""
    for word in code_words:
        if word in morse_to_char:
            decoded_text += morse_to_char[word]
        else:
            decoded_text += ' '
    return decoded_text

print(encode("SOS"))
print(decode("... --- ..."))
