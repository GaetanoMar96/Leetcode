from queue import deque
class Solution:
    def findFarmland(self, land: list[list[int]]) -> list[list[int]]:
        coord = []
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        def bfs(i,j):
            q = deque([(i,j)])
            land[i][j] = 2
            minx, maxx = i, i
            miny, maxy = j, j
            
            while q:
                for _ in range(len(q)):
                    x, y = q.popleft()
                    minx = min(minx, x)
                    maxx = max(maxx, x)
                    miny = min(miny, y)
                    maxy = max(maxy, y)
                    for r,c in directions:
                        x2 = x + r
                        y2 = y + c
                        if 0 <= x2 < len(land) and 0 <= y2 < len(land[0]) and land[x2][y2] == 1:
                            q.append((x2,y2))
                            land[x2][y2] = 2
            group = [minx, miny, maxx, maxy]
            coord.append(group)

        for i in range(len(land)):
            for j in range(len(land[0])):
                if land[i][j] == 1:
                    bfs(i,j)
                    
        return coord