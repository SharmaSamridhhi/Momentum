def checkValidString(self, s: str) -> bool:
    parenthesis_stack = []
    star_stack = []

    for i, ch in enumerate(s):
        if ch == "(":
            parenthesis_stack.append(i)

        elif ch == "*":
            star_stack.append(i)

        else:
            if parenthesis_stack:
                parenthesis_stack.pop()
            elif star_stack:
                star_stack.pop()
            else:
                return False

    while parenthesis_stack and star_stack:
        if parenthesis_stack[-1] > star_stack[-1]:
            return False

        parenthesis_stack.pop()
        star_stack.pop()
        
    return len(parenthesis_stack) == 0