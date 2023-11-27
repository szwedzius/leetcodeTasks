def dailyTemperatures(self, temperatures: list[int]):
    stack = []
    result = [0] * len(temperatures)

    for x in range(0,len(temperatures)):
        while len(stack) > 0 and stack[len(stack)-1][1] < temperatures[x]:
            curr_val = stack.pop()
            result[curr_val[0]] = x - curr_val[0]

        stack.append((x,temperatures[x]))

    print(result)


dailyTemperatures(0,[73,74,75,71,69,72,76,73])