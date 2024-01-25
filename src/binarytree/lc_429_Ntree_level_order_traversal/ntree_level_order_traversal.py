from queue import deque

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def levelOrder(self, root: 'Node') -> list[list[int]]:
        def bfs():
            q = deque([root])
            res = []
            level = []
            while q:
                for _ in range(len(q)):
                    node = q.popleft()
                    level.append(node.val)
                    if node.children:
                        for child in node.children:
                            q.append(child)
                if level:
                    res.append(level)
                level = []
            return res
        return bfs() if root else []