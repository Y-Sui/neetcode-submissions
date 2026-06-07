class MinStack:

    def __init__(self):
        # use two stack to store
        # one is main stack, one is min_stack
        # 为了实现getMin是O(1)时间复杂度，空间换时间，重新构建一个stack专门用来存放main stack的最小值，长度和main stack保持一致
        self.data_stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.data_stack.append(val)

        if not self.min_stack:
            self.min_stack.append(val)

        else:
            val_min = min(val, self.min_stack[-1])
            self.min_stack.append(val_min)

    def pop(self) -> None:
        self.data_stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.data_stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
        
