class TreeNode:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

class BST:
    def __init__(self) -> None:
        self.root = None

    def insertNode(self, val: int) -> None: 
        def dfs(node: TreeNode):
            if val > node.val:
                if not node.right:
                    node.right = TreeNode(val)
                    return
                dfs(node.right)
            else:
                if not node.left:
                    node.left = TreeNode(val)
                    return
                dfs(node.left)

        if not self.root:
            self.root = TreeNode(val)
            return
        node = self.root
        dfs(node)

    def deleteNode(self, val: int) -> None: 
        #TODO
        pass
