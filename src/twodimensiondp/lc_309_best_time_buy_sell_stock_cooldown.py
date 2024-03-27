class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        memo = {}
        def dp(i, stock):
            if i >= len(prices):
                return 0
            if (i,stock) in memo:
                return memo[(i,stock)]
            
            res = 0
            if stock:
                #make profit or not
                res = max(prices[i] + dp(i+2, False), dp(i+1, True))
            else:
                #buy stock or not
                res = max(-prices[i] + dp(i+1, True), dp(i+1, False))
            memo[(i,stock)] = res
            return res
        return dp(0, False)