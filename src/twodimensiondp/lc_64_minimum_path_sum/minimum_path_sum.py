class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        memo = [[0 for _ in range(n)] for _ in range(m)]
        memo[-1][-1] = grid[-1][-1]
        for i in range(m-2, -1, -1):
            memo[i][-1] = grid[i][-1] + memo[i+1][-1]
        for i in range(n-2, -1, -1):
            memo[-1][i] = grid[-1][i] + memo[-1][i+1]
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                memo[i][j] = min(memo[i+1][j]+grid[i][j], memo[i][j+1]+grid[i][j])
        
        return memo[0][0]



         