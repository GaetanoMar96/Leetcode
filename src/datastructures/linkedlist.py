class Node:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next

class LinkedList:

    def __init__(self):
        self.head = None
        self.length = 0

    def get(self, index: int) -> int:
        if index >= self.length or not self.head:
            return -1
        curr = 0
        temp = self.head
        while temp:
            if curr == index:
                return temp.val
            temp = temp.next
            curr += 1
        return -1

    def addAtHead(self, val: int) -> None:
        node = Node(val)
        node.next = self.head
        self.head = node
        self.length += 1

    def addAtTail(self, val: int) -> None:
        if not self.head:
            self.addAtHead(val=val)
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        node = Node(val)
        temp.next = node
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length:
            return
        if index == self.length:
            self.addAtTail(val=val)
            return
        if index <= 0 or not self.head:
            self.addAtHead(val=val)
            return
        curr = 0
        temp = self.head
        while temp:
            if curr == index - 1:
                node = Node(val)
                node.next = temp.next
                temp.next = node
                self.length += 1
                return
            temp = temp.next
            curr += 1

    def deleteHead(self):
        if not self.head:
            return
        self.head = self.head.next
        self.length -= 1

    def deleteTail(self):
        if not self.head:
            return 
        if not self.head.next:
            self.deleteHead()
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None
        self.length -= 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.length or index < 0:
            return
        if index == 0 or not self.head:
            self.deleteHead()
            return
        curr = 0
        temp = self.head
        while temp:
            if curr == index - 1:
                temp.next = temp.next.next
                self.length -= 1
                return
            temp = temp.next
            curr += 1

