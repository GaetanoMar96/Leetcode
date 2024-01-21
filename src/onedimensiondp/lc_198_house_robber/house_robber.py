class Solution:
    def rob(self, nums: list[int]) -> int:
        memo = [-1] * len(nums)
        def dp(i):
            if i >= len(nums):
                return 0
            if memo[i] != -1:
                return memo[i]
            res = dp(i+1) #next hpuse
            curr = nums[i] + dp(i+2) #curr + next
            memo[i] = max(res, curr)
            return memo[i] 
        return dp(0)