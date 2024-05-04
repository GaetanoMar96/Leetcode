class Node:
    def __init__(self, key, value, next=None) -> None:
        self.key = key
        self.value = value
        self.next = next

class HashMap:

    def __init__(self):
        self.head = Node(-1,-1)

    def put(self, key: int, value: int) -> None:
        temp = self.head
        while temp.next:
            if temp.key == key:
                temp.value = value
                break
            temp = temp.next
        node = Node(key, value)
        temp.next = node

    def get(self, key: int) -> int:
        temp = self.head
        while temp:
            if temp.key == key:
                return temp.value
            temp = temp.next
        return -1

    def remove(self, key: int) -> None:
        temp = self.head
        prev = temp
        while temp:
            if temp.key == key:
                prev.next = temp.next
                break
            prev = temp
            temp = temp.next
    
    def getHashCode(self):
        #TODO
        pass #for any positive key the hash code is key % array size M (to be prime)