from functools import cache
class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        @cache
        def dp(i, row):
            if row == 0:
                return matrix[0][i]
            
            temp1 = float('inf')
            temp2 = float('inf')
            if i - 1 >= 0:
                temp1 = dp(i-1, row-1)
            if i + 1 < len(matrix):
                temp2 = dp(i+1, row-1)
            res = min(min(dp(i, row-1), temp1), temp2) + matrix[row][i]
            return res
        res = float('inf')
        for i in range(len(matrix)):
            res = min(res, dp(i, len(matrix) - 1))
        return res