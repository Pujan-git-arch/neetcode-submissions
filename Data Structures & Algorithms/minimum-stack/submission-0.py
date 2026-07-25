from collections import deque

class MinStack:

    def __init__(self):
        self.stack = deque()
        self.minStack = deque()

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.minStack:
            self.minStack.append(val)
        else:
            self.minStack.append(min(val, self.minStack[-1]))

    def pop(self) -> int:
        if self.stack:
            self.minStack.pop()
            return self.stack.pop()
        raise IndexError("Stack is empty")

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        raise IndexError("Stack is empty")

    def getMin(self) -> int:
        if self.minStack:
            return self.minStack[-1]
        raise IndexError("Stack is empty")

    def isempty(self):
        return len(self.stack) == 0