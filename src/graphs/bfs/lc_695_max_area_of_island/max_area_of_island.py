from queue import deque
class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        def bfs(i,j):
            q = deque([(i,j)])
            directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
            area = 1
            grid[i][j] = 2
            while q:
                r, c = q.popleft()
                for direction in directions:
                    rx, cy = r + direction[0], c + direction[1]
                    if 0 <= rx < len(grid) and 0 <= cy < len(grid[0]) and grid[rx][cy] == 1:
                        q.append((rx, cy)) 
                        grid[rx][cy] = 2   
                        area += 1
    
            return area


        area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    area = max(area, bfs(i,j))
        return area