class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        memo = {}
        MOD = 10**9 + 7
        def dp(i, j, moves):
            if moves > maxMove:
                return 0
            if (i,j,moves) in memo:
                return memo[(i,j, moves)]
            if i < 0 or j < 0 or i >= m or j >= n:
                return 1 #valid path
            res = (
                dp(i-1, j, moves + 1) +
                dp(i+1, j, moves + 1) +
                dp(i, j-1, moves + 1) +
                dp(i, j+1, moves + 1)
            ) 
            memo[(i,j, moves)] = res % MOD
            return memo[(i,j, moves)]
        return dp(startRow, startColumn, 0)