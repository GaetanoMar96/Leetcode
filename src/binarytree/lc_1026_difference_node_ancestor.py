from treeNode import TreeNode

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.max = 0
        def findNodes(root, ancestor):
            self.max = max(abs(root.val - ancestor), self.max)
            if root.left:
                findNodes(root.left, ancestor)
            if root.right:
                findNodes(root.right, ancestor)
        
        def dfs(node):
            if not node:
                return
            
            findNodes(node, node.val)
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
        dfs(root)
        return self.max