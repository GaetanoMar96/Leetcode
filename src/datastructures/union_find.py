class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, node):
        if self.parent[node] == node:
            return node
        
        while self.parent[node] != node:
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]
        return self.parent[node]

    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)
        if root1 == root2:
            return 0
        if self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
            self.rank[root1] += self.rank[root2]
        else:
            self.parent[root1] = root2
            self.rank[root2] += self.rank[root1]
        return 1