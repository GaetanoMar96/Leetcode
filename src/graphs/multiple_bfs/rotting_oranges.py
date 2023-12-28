from collections import deque
class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        fresh = 0
        rotten = deque()
        def bfs(rotten, fresh, m, n):
            directions = [(-1,0),(0,-1),(1,0),(0,1)]
            minutes = 0
            while rotten:
                for _ in range(len(rotten)):
                    i, j = rotten.popleft()
                    for x, y in directions:
                        xi = x + i
                        yj = y + j
                        if 0 <= xi < m and 0 <= yj < n and grid[xi][yj] == 1:
                            rotten.append((xi, yj))
                            grid[xi][yj] = 2
                            fresh -= 1
                minutes += 1
            return minutes - 1 if fresh == 0 else -1
        
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    rotten.append((i,j))
                if grid[i][j] == 1:
                    fresh += 1
        if fresh == 0:
            return 0
        return bfs(rotten, fresh, m, n)