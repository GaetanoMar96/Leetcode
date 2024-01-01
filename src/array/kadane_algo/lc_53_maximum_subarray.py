class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        curr, best = 0, 0
        if max(nums) < 0:
            return max(nums)
        for num in nums:
            curr = max(num, curr + num)
            best = max(best, curr)
        return best