def zavorky_check(s):
    stack = []
    opening_brackets = "([{"
    closing_brackets = ")]}"
    
    for char in s:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack or opening_brackets.index(stack.pop()) != closing_brackets.index(char):
                return False
    return not stack

print(zavorky_check("()")) 
print(zavorky_check("()[]{}"))   
print(zavorky_check("(]"))        
print(zavorky_check("([)]"))     
