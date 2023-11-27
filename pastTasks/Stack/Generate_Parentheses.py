def generateParenthesis(self, n: int) -> list[str]:
    leftStack = []
    rightStack = []
    for x in range(n):
        leftStack.append("(")
        rightStack.append(")")

    optionsDict = {"": [leftStack,rightStack]}
    for x in range(2*n):
        new_options_dict = {}
        for key in optionsDict.keys():
            current_left_stack = optionsDict[key][0]
            current_right_stack = optionsDict[key][1]
            if len(current_left_stack) == 0:
                newSol = key + current_right_stack.pop()
                new_options_dict[newSol] = [current_left_stack, current_right_stack]
            elif len(current_left_stack) == len(current_right_stack):
                newSol = key + current_left_stack.pop()
                new_options_dict[newSol] = [current_left_stack,current_right_stack]
            else:
                newSol1 = key + current_right_stack[len(current_right_stack)-1]
                newSol2 = key + current_left_stack[len(current_left_stack) - 1]
                new_options_dict[newSol1] = [current_left_stack,current_right_stack[:-1]]
                new_options_dict[newSol2] = [current_left_stack[:-1], current_right_stack]
        optionsDict = new_options_dict
    result = optionsDict.keys()
    return list(result)


print(generateParenthesis("",1))