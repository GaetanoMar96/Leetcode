class HashMap:

    def __init__(self, size: int):
        self.size = size
        self.hashmap = [[] for _ in range(size) ]

    def put(self, key: int, value: int) -> None:
        code = self.getHash(key)
        slot = self.hashmap[code]
        for i, (k,_) in enumerate(slot):
            if k == key:
                slot[i] = (key, value)
                return
        slot.append((key, value))

    def get(self, key: int) -> int:
        code = self.getHash(key)
        slot = self.hashmap[code]
        for i, (k,v) in enumerate(slot):
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        code = self.getHash(key)
        slot = self.hashmap[code]
        for i, (k,_) in enumerate(slot):
            if k == key:
                del slot[i]
                break

    def getHash(self, key):
        #compute hash function % size to get an index in the range 0 - len(array) - 1
        return hash(key) % self.size