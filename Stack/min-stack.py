class MinStack:
    def __init__(self):
        self.stack = []
        self.minstack = []
    # @param x, an integer
    # @return an integer

    def push(self, x):
        self.stack.append(x)

        if len(self.minstack) == 0:
            self.minstack.append(x)
        else:
            current_min = self.minstack[-1]
            self.minstack.append(min(current_min, x))

        return x

    # @return nothing

    def pop(self):
        if len(self.stack) == 0:
            return -1

        self.stack.pop()
        self.minstack.pop()

    # @return an integer

    def top(self):
        if len(self.stack) == 0:
            return -1

        return self.stack[-1]

    # @return an integer

    def getMin(self):
        if len(self.stack) == 0:
            return -1
        return self.minstack[-1]
