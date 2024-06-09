from collections import defaultdict
from heap import heapq

class Solution:
    def shortestPath(self, n: int, edges: list[list[int]], src: int) -> dict[int, int]:
        paths = {}
        for i in range(n):
            paths[i] = float('inf')

        adj = defaultdict(list)
        for u,v,w in edges:
            adj[u].append((w, v))
        
        pq = []
        pq.append((0, src))
        visited = set()
        while pq:
            for _ in range(len(pq)):
                w, v = heapq.heappop(pq)
                if v in visited:
                    continue
                visited.add(v)
                paths[v] = w
                if v in adj:
                    for wn, n in adj[v]:
                        distance = w + wn
                        if paths[n] > distance:
                            heapq.heappush(pq, (distance, n))
        for key in paths:
            if paths[key] == float('inf'):
                paths[key] = -1
        return paths