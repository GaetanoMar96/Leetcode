class MaxHeap:
    # bynary heap representation using a queue
    def __init__(self) -> None:
        self.q = [None] #0 index unused
        self.size = 0
    
    def push(self, val: int) -> None:
        self.q.append(val)
        #swim to adjust parent if its value < child value
        self.size += 1
        self.swim()
    
    def swim(self) -> None:
        k = self.size
        #parent is at position k // 2
        while k > 1 and self.q[k//2] < self.q[k]:
            #swap parent value with child value
            self.q[k//2], self.q[k] = self.q[k], self.q[k//2]
            #go to parent
            k = k // 2
        print(self.q)

    def pop(self) -> int:
        #remove maximum element which is at index 0
        parent = self.q[1]
        self.q[1] = self.q[-1] #replace max element with last elemnt
        self.q.pop() #remove last element
        self.size -= 1
        self.sink(1) #adjust heap
        print(self.q)
        return parent

    def sink(self, k): 
        #k is the index of parent index 1
        # children of a node at position k in heap are at position k*2 and k*2 + 1
        while 2*k <= self.size: #if the parent is at k // 2, the child is at k * 2
            j = 2*k #left child
            if j < self.size and self.q[j] < self.q[j+1]: #if right child is larger then left move j
                j += 1 #move to right child 2*k + 1
            if not self.q[k] < self.q[j]: # if parent is greater than child stop
                break
            self.q[k], self.q[j] = self.q[j], self.q[k] #swap parent and right child (largest one)
            k = j

heap = MaxHeap()
heap.push(1)
heap.push(5)
heap.push(3)
heap.push(4)
rem = heap.pop()
print(rem)