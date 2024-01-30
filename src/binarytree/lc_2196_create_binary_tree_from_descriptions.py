from treeNode import TreeNode
from collections import defaultdict
class Solution:
    def createBinaryTree(self, descriptions: list[list[int]]) -> TreeNode:
        nodes = defaultdict(list)
        def reconstruct(val):
            if val not in nodes:
                return TreeNode(val)
            node = TreeNode(val)
            listnodes = nodes[val]
            for v, d in listnodes:
                if d == 1:
                    node.left = reconstruct(v)
                else:
                    node.right = reconstruct(v)
            return node

        parents = set()
        childs = set()
        for description in descriptions:
            parent, child, direction = description
            parents.add(parent)
            childs.add(child)
            if child in parents:
                parents.remove(child)
            if parent in childs and parent in parents:
                parents.remove(parent)
            nodes[parent].append((child, direction))

        rootval = list(parents)[0]
        return reconstruct(rootval)
    
