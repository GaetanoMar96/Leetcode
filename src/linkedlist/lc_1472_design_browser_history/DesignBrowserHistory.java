class Node {
    public String url;
    public Node prev;
    public Node next;
    Node(String url, Node prev, Node next) {
        this.url = url;
        this.prev = prev;
        this.next = next;
    }
}
class BrowserHistory {

    Node head;
    Node curr;

    public BrowserHistory(String homepage) {
        this.head = new Node(homepage, null, null);
        this.curr = head;    
    }
    
    public void visit(String url) {
        Node node = new Node(url, null, null);
        this.curr.next = node;
        node.prev = this.curr;
        this.curr = this.curr.next;
    }
    
    public String back(int steps) {
        while(this.curr.prev != null) {
            this.curr = this.curr.prev;
            steps -= 1;
            if (steps == 0)
                break;
        }
        return this.curr.url;
    }
    
    public String forward(int steps) {
        while(this.curr.next != null) {
            this.curr = this.curr.next;
            steps -= 1;
            if (steps == 0)
                break;
        }
        return this.curr.url;
    }
}