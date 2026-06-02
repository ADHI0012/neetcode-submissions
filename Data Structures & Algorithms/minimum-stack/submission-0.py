class MinStack:

    def __init__(self):
        self.stack = []
        self.minEl = float('inf')
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val < self.minEl:
            self.minEl = val
        

    def pop(self) -> None:
        removed = self.stack.pop()
        if removed == self.minEl:
            self.minEl = min(self.stack) if self.stack else float('inf')
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minEl
        
