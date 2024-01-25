from treeNode import TreeNode
class Solution:
    def delNodes(self, root: TreeNode, to_delete: list[int]) -> list[TreeNode]:
        res = [] #store all the nodes to be returned
        #time complexity O(N)
        #space complexity O(H + N)
        to_delete = set(to_delete) 
        def dfs(node, is_root):
            if not node:
                return None
            if node.val in to_delete:
                dfs(node.left, True)
                dfs(node.right, True)
                return None
            if is_root:
                res.append(node)
            node.left = dfs(node.left, False)
            node.right = dfs(node.right, False)
            return node

        dfs(root, True)
        return res