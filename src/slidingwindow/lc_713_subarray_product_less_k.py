class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        if k <= 1:
            return 0
        l = 0
        currprod = 1
        res = 0
        for r in range(len(nums)):
            currprod *= nums[r]
            while l < len(nums) and currprod >= k:
                currprod = currprod // nums[l]
                l += 1
        
            res += r - l + 1 #current window size, all subarrays inside window
     
        return res