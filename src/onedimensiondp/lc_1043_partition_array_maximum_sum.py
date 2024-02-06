class Solution:
    def maxSumAfterPartitioning(self, arr: list[int], k: int) -> int:
        memo = [-1] * len(arr)
        def dp(i):
            if i >= len(arr):
                return 0
            if memo[i] != -1:
                return memo[i]
            res = 0
            curr = 0
            for j in range(i, i + k):
                if j >= len(arr):
                    break
                curr = max(curr, arr[j])
                size = j - i + 1
                res = max(res, curr * size + dp(j+1))
            memo[i] = res
            return res
        return dp(0)