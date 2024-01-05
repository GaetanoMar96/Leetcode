class Solution:
    def climbStairs(self, n: int) -> int:
        def rec(n, memo):
            if n in memo:
                return memo[n]
            memo[n] = rec(n-1,memo) + rec(n-2,memo)
            return memo[n]
        memo = {}
        memo[0] = 1
        memo[1] = 1
        return rec(n, memo)