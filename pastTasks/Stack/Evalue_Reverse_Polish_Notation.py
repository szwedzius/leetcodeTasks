def evalRPN(self, tokens: list[str]) -> int:
    stack = []
    symbols = ["+","-","*","/"]
    for x in tokens:
        if x not in symbols:
            stack.append(int(x))
            continue
        first = stack.pop()
        second = stack.pop()
        if x == "+":
            stack.append(second+first)
        elif x == "-":
            stack.append(second-first)
        elif x == "*":
            stack.append(second*first)
        else:
            stack.append(int(second/first))
    return stack.pop()

print(evalRPN("",["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))