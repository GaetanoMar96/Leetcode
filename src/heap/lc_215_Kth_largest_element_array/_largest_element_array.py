import heapq # priority queue
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heap = []
        heapq.heapify(heap)
        for n in nums:
            heapq.heappush(heap, -n)
        for _ in range(k):
            item = heapq.heappop(heap)
        return -item