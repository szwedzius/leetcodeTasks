class MinStack:

    def __init__(self):
        self.stack = []
        self.minVals = []
    def push(self, val: int) -> None:
        self.stack.append(val)
        if val < self.minVals[len(self.minVals)-1]:
            self.minVals.append(val)
    def pop(self) -> None:
        curr_val = self.stack.pop()
        if curr_val == self.minVals[len(self.minVals)-1]:
            self.minVals.pop()
    def top(self) -> int:
        return self.stack[len(self.stack)-1]
    def getMin(self) -> int:
        return self.minVals[len(self.minVals)-1]