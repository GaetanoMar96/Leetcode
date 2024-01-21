from queue import heapq
from collections import defaultdict

class Graph:

    def __init__(self, n: int, edges: list[list[int]]):
        self.size = n
        self.adj = defaultdict(list)
        for edge in edges: 
            u, v, cost = edge
            self.adj[u].append((v, cost))
           
        
    def addEdge(self, edge: list[int]) -> None:
        u, v, cost = edge
        self.adj[u].append((v, cost))

    def shortestPath(self, node1: int, node2: int) -> int:
        pq = []
        heapq.heappush(pq, (0, node1))
        visited = set()
        path = [float('inf')] * self.size
        path[node1] = 0
        while pq:
            curr_cost, curr_node = heapq.heappop(pq)
            if curr_node == node2:
                return curr_cost
            if curr_node in visited:
                continue
            visited.add(curr_node)
            for dest_node, dest_cost in self.adj[curr_node]:
                tot_cost = dest_cost + curr_cost
                if tot_cost < path[dest_node]:
                    path[dest_node] = tot_cost
                    heapq.heappush(pq, (tot_cost, dest_node))
        return -1
        