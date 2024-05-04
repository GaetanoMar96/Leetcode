class Stack:
    # LIFO data structure used to store data with the ability to remove them.
    # Push element on top of the stack, pop them always from top.

    def __init__(self) -> None:
        self.stack = []

    def push(self, val) -> None:
        self.stack.append(val)
    
    def pop(self) -> int:
        return self.stack.pop()

    def getPeek(self) -> int:
        if self.isEmpty():
            return -1
        return self.stack[-1]
    
    def isEmpty(self) -> bool:
        return not self.stack
    
    def getSize(self) -> int:
        return len(self.stack)
