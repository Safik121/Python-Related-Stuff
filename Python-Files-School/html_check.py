def zavorky_check(s):
    stack = []
    opening_brackets = "<"
    closing_brackets = ">"

    for char in s:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack or opening_brackets.index(stack.pop()) != closing_brackets.index(char):
                return False
    return not stack

def go_trough(start, txt):
    output = ""
    while start < len(txt) and txt[start] not in "<>":
        output += txt[start]
        start += 1
    return output, start

def html_check(text):
    first_appearance = []
    if not zavorky_check(text):
        return False
    else:
        index = 0
        while index < len(text):
            char = text[index]
            if char == "<":
                index += 1
                if index < len(text) and text[index] == "/":
                    index += 1
                    html_token, new_index = go_trough(index, text)
                    if not first_appearance or first_appearance.pop() != html_token:
                        return False
                else:
                    html_token, new_index = go_trough(index, text)
                    if html_token not in first_appearance:
                        first_appearance.append(html_token)
                    elif html_token in first_appearance and first_appearance.pop() != html_token:
                        return False
                index = new_index
            index += 1
            #print(index)
    return not first_appearance

print(html_check("<ik><b></b></ik>"))
print(html_check("</ik><b></b></ik>"))
print(html_check("<h1><b></b></h1>"))
