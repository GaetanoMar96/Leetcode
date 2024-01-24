from treeNode import TreeNode
from collections import defaultdict
class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        path = defaultdict(int)
        self.count = 0
        def dfs(root):
            if not root:
                return
            path[root.val]+=1
            if not root.left and not root.right:
                if checkPaths(): 
                    self.count += 1
                path[root.val]-=1
                return
            
            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)
            path[root.val]-=1
            
        def checkPaths():
            odd = 0
            for key in path:
                if path[key] % 2 != 0:
                    odd += 1
                    if odd > 1:
                        return False
            return True
        dfs(root)
        return self.count