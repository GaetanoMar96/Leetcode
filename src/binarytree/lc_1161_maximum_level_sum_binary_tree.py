from treeNode import TreeNode
from queue import deque
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        q = deque([root])
        level = 1
        levelsum = 0
        res = -100000
        reslevel = 1
        while q: 
            for _ in range(len(q)):
                node = q.popleft()
                levelsum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if levelsum > res:
                res = levelsum
                reslevel = level
            levelsum = 0
            level += 1
        return reslevel