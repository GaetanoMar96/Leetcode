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

    def deleteNode(self, node: TreeNode, target: int) -> TreeNode: 
        def findMinimum(node):
            while node.left:
                node = node.left
            return node
        
        if not node:
            return None
        
        if node.val == target:
            #case 1: no children -> return None
            if not node.left and not node.right:
                node = None
            #case 2: both children, get minimum from the right
            elif node.left and node.right:
                far_left = findMinimum(node)
                node.val = far_left.val
                node.right = self.deleteNode(node.right, far_left.val)
            #case 3 1 child -> child become the root
            else: 
                if node.left:
                    node = node.left
                else:
                    node = node.right
        elif target > node.val:
            node.right = self.deleteNode(node.right, target)
        else:
            node.left = self.deleteNode(node.left, target)
        return node
