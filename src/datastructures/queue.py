class Queue:
    # FIFO data structure used to store data with the ability to remove them.
    # Enqueue element on the rear of the stack, deque from front.

    def __init__(self) -> None:
        self.queue = []

    def enqueue(self, val) -> None:
        self.queue.insert(0, val)
    
    def dequeue(self) -> int:
        return self.queue.pop()

    def getPeek(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[-1]
    
    def isEmpty(self) -> bool:
        return not self.queue
    
    def getSize(self) -> int:
        return len(self.queue)
    
class QueueWithStacks:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        if not self.s1:
            self.s1.append(x)
            return
        #remove all from s1 pushing in s2
        while self.s1:
            self.s2.append(self.s1.pop())
        self.s1.append(x)
        while self.s2:
            self.s1.append(self.s2.pop())

    def pop(self) -> int:
        if not self.empty():
            return self.s1.pop()
        return -1

    def peek(self) -> int:
        if not self.empty():
            return self.s1[-1]
        return -1
        
    def empty(self) -> bool:
        return len(self.s1) == 0