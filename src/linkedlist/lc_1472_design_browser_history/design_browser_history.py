class Node:
    def __init__(self, val, next=None, prev=None) -> None:
        self.val = val
        self.next = next
        self.prev = prev


class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Node(homepage)
        self.curr = self.head

    def visit(self, url: str) -> None:
        temp = self.curr
        temp2 = Node(url, None, temp)
        temp.next = temp2
        self.curr = temp2

    def back(self, steps: int) -> str:
        temp = self.curr
        while temp.prev and steps > 0:
            temp = temp.prev
            steps -= 1
        self.curr = temp
        return temp.val

    def forward(self, steps: int) -> str:
        temp = self.curr
        while temp.next and steps > 0:
            temp = temp.next
            steps -= 1
        self.curr = temp
        return temp.val


