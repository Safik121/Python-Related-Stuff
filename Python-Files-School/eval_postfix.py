import math

def evaluate_postfix(str):
    output = []
    cislo = str.split()

    for i in cislo:
        if is_int(i):
            output.append(int(i))
        else:
            if len(output) < 2:
                raise ValueError("nuh uh")

            operand2 = output.pop()
            operand1 = output.pop()

            if i == "+":
                output.append(operand1 + operand2)
            elif i == "-":
                output.append(operand1 - operand2)
            elif i == "*":
                output.append(operand1 * operand2)
            elif i == "/":
                output.append(operand1 / operand2)
            elif i == "^":
                output.append(operand1 ** operand2)
            else:
                raise ValueError("nuh uh")

    if len(output) != 1:
        raise ValueError("nuh uh")

    return int(output[0])

def is_int(number):
    try:
        int(number)
        return True
    except ValueError:
        return False

print(evaluate_postfix("15 7 1 1 + - / 3 * 2 1 1 + + -"))
