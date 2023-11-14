def isValid(self, s: str):
    symbols = { "]": "[", ")":"(","}":"{"}
    stack = []
    for x in s:
        if x in symbols:
            if len(stack)==0:
                return False
            top_of_stack = stack.pop()
            if symbols[x] != top_of_stack:
                return False
        else:
            stack.append(x)
    return len(stack) == 0

print(isValid("","(]"))