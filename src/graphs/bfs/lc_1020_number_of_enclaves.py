from queue import deque
class Solution:
    def numEnclaves(self, grid: list[list[int]]) -> int:
        self.m, self.n = len(grid), len(grid[0])
        self.directions = [(-1,0), (0,-1), (1,0), (0,1)]
        def bfs(r, c):
            q = deque([(r, c)])
            res = 0
            visited = False
            while q:
                for _ in range(len(q)):
                    x, y = q.popleft()
                    if grid[x][y] == 1:
                        res += 1
                        grid[x][y] = 2
                        if x == 0 or x == self.m - 1: #border
                            visited = True
                        if y == 0 or y == self.n - 1: #border
                            visited = True
                        #chech directions
                        if 0 <= x < self.m and 0 <= y + 1 < self.n and grid[x][y+1] == 1:
                            q.append((x, y+1))
                        if 0 <= x + 1 < self.m and 0 <= y < self.n and grid[x+1][y] == 1:
                            q.append((x+1, y))
                        if 0 <= x - 1 < self.m and 0 <= y < self.n and grid[x-1][y] == 1:
                            q.append((x-1, y))
                        if 0 <= x < self.m and 0 <= y - 1 < self.n and grid[x][y-1] == 1:
                            q.append((x, y-1))
            if visited:
                return 0
            return res

        #check boundaries and if 1 start bfs
        res = 0
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 1:
                    res += bfs(i,j)
        return res