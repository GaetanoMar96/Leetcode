class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        minc = [0] * len(cost)
        minc[-1] = cost[-1]
        minc[-2] = cost[-2]

        for i in range(len(cost) - 3, -1, -1):
            minc[i] = min(minc[i+1], minc[i+2]) + cost[i]
        
        return min(minc[0], minc[1])