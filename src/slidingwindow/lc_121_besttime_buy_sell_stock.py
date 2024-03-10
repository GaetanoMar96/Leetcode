class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        res = 0
        curr = prices[0]
        for i in range(1, len(prices)):
            if curr > prices[i]:
                curr = prices[i]
                continue
            res = max(res, prices[i] - curr)
        return res