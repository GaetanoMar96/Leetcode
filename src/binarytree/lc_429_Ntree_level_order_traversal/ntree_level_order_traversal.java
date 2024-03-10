import java.util.*;
class Solution {

    List<List<Integer>> res = new ArrayList<>();

    public List<List<Integer>> levelOrder(Node root) {
        if (root == null) {
            return res;
        }
        bfs(root);
        return res;
    }

    public void bfs(Node root) {
        Deque<Node> dequeue = new LinkedList<>();
        List<Integer> level = new ArrayList<>();
        dequeue.addLast(root);
        while(!dequeue.isEmpty()) {
            int length = dequeue.size();
            for (int i = 0; i < length; i++) {
                Node node = dequeue.removeFirst();
                level.add(node.val);
                if (node.children != null) {
                    for(Node child : node.children) {
                        dequeue.addLast(child);
                    }
                }
            }
            if (level.size() > 0) {
                res.add(level);
                level = new ArrayList<>();
            }
        }
    }

    static class Node {
        int val;
        List<Node> children;
        Node(int val, List<Node> children) {
            this.val = val;
            this.children = children;
        }
    }
}