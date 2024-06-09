class Node:
    def __init__(self, key:int, val: int, prev=None, next=None):
        self.key = key
        self.value = val
        self.prev = prev
        self.next = next

class LRUCache:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {} # key node
        self.left, self.right = Node(-1,-1), Node(-1,-1)
        self.left.next, self.right.prev = self.right, self.left
        
    def insert(self, node): #insert node
        prev, right = self.right.prev, self.right
        prev.next, node.next = node, right
        node.prev, right.prev = prev, node

    def remove(self, node): #delete node 
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        
        node = self.map[key] 
        self.remove(node)
        self.insert(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.map[key].value = value
            self.remove(self.map[key])
            self.insert(self.map[key])
            return
        #insert if key exceeds remove first node
        node = Node(key, value)
        self.insert(node)
        self.map[key] = node
        if len(self.map.keys()) > self.capacity:
            node = self.left.next
            self.remove(node)
            del self.map[node.key]