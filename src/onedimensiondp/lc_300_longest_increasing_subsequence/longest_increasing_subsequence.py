class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        dp = [1] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            curr = nums[i] 
            for j in range(i+1, len(nums)):
                if curr < nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)