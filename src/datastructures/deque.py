class Deque:
    # Double ended queue data structure.
    # Has the abilities of a stack and of a queue.

    def __init__(self) -> None:
        self.deque = []

    def insert(self, val) -> None:
        self.deque.insert(0, val)
    
    def append(self, val) -> None:
        self.deque.append(val)
    
    def popLeft(self) -> int:
        return self.deque.pop(0)

    def popRight(self) -> int:
        return self.deque.pop()

    def getPeek(self) -> int:
        if self.isEmpty():
            return -1
        return self.deque[-1]
    
    def isEmpty(self) -> bool:
        return not self.deque
    
    def getSize(self) -> int:
        return len(self.deque)