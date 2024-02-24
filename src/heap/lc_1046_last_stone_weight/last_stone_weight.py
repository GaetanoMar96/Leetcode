import heapq
class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        heap = []
        heapq.heapify(heap)
        for stone in stones:
            heapq.heappush(heap, -stone)
        
        while len(heap) > 1:
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)
            if x != y:
                heapq.heappush(heap, x -y)
            else:
                if not heap:
                    return 0
            
        if not heap:
            return 0
        return -heap[0]
        
