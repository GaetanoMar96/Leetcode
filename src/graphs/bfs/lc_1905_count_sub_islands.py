from queue import deque
class Solution:
    def countSubIslands(self, grid1: list[list[int]], grid2: list[list[int]]) -> int:
        m, n = len(grid1), len(grid1[0])
        def bfs(start):
            directions = [(-1,0),(0,1),(1,0),(0,-1)]
            q = deque([start])
            while q:
                r, c = q.popleft()
                grid1[r][c] = 2
                size = len(q)
                for _ in range(size):
                    for d in directions:
                        rd, cd = d
                        if 0 <= r + rd < m and 0 <= c + cd < n: 
                            if grid1[r+rd][c+cd] == 1:
                                q.append((r+rd, c+cd))
        
        def bfs2(start):
            directions = [(-1,0),(0,1),(1,0),(0,-1)]
            q = deque([start])
            sub = True
            while q:
                r, c = q.popleft()
                
                if grid1[r][c] != 2: #no islands
                    sub = False
                for d in directions:
                    rd, cd = d
                    if 0 <= r + rd < m and 0 <= c + cd < n: 
                        if grid2[r+rd][c+cd] == 1:
                            grid2[r+rd][c+cd] = 2
                            q.append((r+rd, c+cd))
            return sub
        
        for i in range(m):
            for j in range(n):
                if grid1[i][j] == 1:
                    bfs((i,j))
        
        count = 0

        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    if (bfs2((i,j))):
                        count += 1
        return count

