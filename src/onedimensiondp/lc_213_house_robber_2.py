class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        if sum(nums) == 0:
            return 0
        memo1 = [0] * (len(nums) - 1)
        memo2 = [0] * (len(nums) - 1)
        def dp(i, nums, memo):
            if i >= len(nums):
                return 0
            
            if memo[i] != 0:
                return memo[i]
            
            res = max(nums[i] + dp(i+2, nums, memo), dp(i+1, nums, memo))
            memo[i] = res
            return res
        #2 dps
        temp1 = nums[0:-1]
        temp2 = nums[1:]
        
        return max(dp(0, temp1, memo1), dp(0, temp2, memo2))