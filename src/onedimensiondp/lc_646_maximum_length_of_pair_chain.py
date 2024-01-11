# SOL 1
class Solution:
    def findLongestChain(self, pairs: list[list[int]]) -> int:
        pairs = sorted(pairs, key = lambda x:x[0])
        memo = {}
        def dp(i):
            if i >= len(pairs):
                return 0
            if i in memo:
                return memo[i]
            
            res = dp(i+1) 
            chain = 0
            for j in range(i+1, len(pairs)):
                if pairs[j][0] > pairs[i][1]:
                    chain = dp(j)
                    break
            memo[i] = max(res, chain + 1)
            return memo[i]
        return dp(0)
# SOL 2
class Solution:
    def findLongestChain(self, pairs: list[list[int]]) -> int:
        pairs = sorted(pairs, key=lambda x: x[0])
        dp = [1] * len(pairs)
        
        for i in range(len(pairs)):
            for j in range(i):
                if  pairs[j][1] < pairs[i][0]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return dp[-1]