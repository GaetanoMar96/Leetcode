from collections import defaultdict
from queue import deque
class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        adj = defaultdict(list)
        if not edges:
            return [0]
        
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)

        leaves = deque()
        for key in adj:
            if len(adj[key]) == 1: #leaf node has only 1 connection
                leaves.append(key)
        while n > 2: #the root and the node attached to it
            n -= len(leaves)
            for _ in range(len(leaves)):
                leaf = leaves.popleft()
                neighbor = adj[leaf][0] #interested in the only element connected to leaf
                adj[neighbor].remove(leaf) #remove leaf from neigh
                if len(adj[neighbor]) == 1: #again a leaf node
                    leaves.append(neighbor)

        return list(leaves)
