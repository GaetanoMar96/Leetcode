from treeNode import TreeNode

class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        
        def dfs(node):
            if not node:
                return None

            if node.val == target and not node.left and not node.right:
                return None
            
            root = TreeNode(node.val)
            root.left = dfs(node.left)
            root.right = dfs(node.right)
            if not root.right and not root.left and root.val == target:
                return None
            return root
        return dfs(root)