import heapq

class KthLargest:
    ### Min heap
    def __init__(self, k: int, nums: list[int]):
        self.nums = nums
        self.k = k
        heapq.heapify(self.nums)
        while len(self.nums) > k:
            heapq.heappop(self.nums)
        
    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        if self.k < len(self.nums):
            heapq.heappop(self.nums)
        return self.nums[0]
        