class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        while len(self.s1) > 1:
            self.s2.append(self.s1.pop())
        
        t = self.s1.pop()
        while self.s2:
            self.s1.append(self.s2.pop())
        return t

    def peek(self) -> int:
        while len(self.s1) > 1:
            self.s2.append(self.s1.pop())
        
        t = self.s1[0]
        while self.s2:
            self.s1.append(self.s2.pop())
        return t

    def empty(self) -> bool:
        return len(self.s1) == 0
