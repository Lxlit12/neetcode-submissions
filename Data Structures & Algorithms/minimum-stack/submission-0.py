class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stk = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.min_stk :
            self.min_stk.append(val)
        elif self.min_stk[-1] < val:
            self.min_stk.append(self.min_stk[-1])
        else:
            self.min_stk.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stk.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stk[-1]
