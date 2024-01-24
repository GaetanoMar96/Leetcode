type TreeNode struct {
	Val int
	Left *TreeNode
	Right *TreeNode
}
	
func pruneTree(root *TreeNode) *TreeNode {
	if root == nil {
		return nil
	}
	if root.Val == 0 && root.Left == nil && root.Right == nil {
		return nil
	}
	node := new(TreeNode)
	node.Val = root.Val
	node.Left = pruneTree(root.Left, target)
	node.Right = pruneTree(root.Right, target)
	if node.Left == nil && node.Right == nil && node.Val == 0 {
		return nil
	}
	return node
}