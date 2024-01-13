type TreeNode struct {
	Val int
	Left *TreeNode
	Right *TreeNode
}
	
func removeLeafNodes(root *TreeNode, target int) *TreeNode {
	if root == nil {
		return nil
	}
	if root.Val == target && root.Left == nil && root.Right == nil {
		return nil
	}
	node := new(TreeNode)
	node.Val = root.Val
	node.Left = removeLeafNodes(root.Left, target)
	node.Right = removeLeafNodes(root.Right, target)
	if node.Left == nil && node.Right == nil && node.Val == target {
		return nil
	}
	return node
}