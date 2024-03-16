from treeNode import TreeNode
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def findPathFromRoot(node: TreeNode, curr_max: int):
            nonlocal count
            if not node:
                return
            if node.val >= curr_max:
                curr_max = node.val
                count += 1
            
            findPathFromRoot(node.left, curr_max)
            findPathFromRoot(node.right, curr_max)
            
        findPathFromRoot(root, root.val)
        return count