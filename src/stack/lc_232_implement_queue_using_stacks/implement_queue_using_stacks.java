import java.util.*;
class MyQueue {

    Deque<Integer> front;

    public MyQueue() {
        front = new LinkedList<>();
    }
    
    public void push(int x) {
        front.addLast(x);
    }
    
    public int pop() {
        return front.removeFirst();
    }
    
    public int peek() {
        return front.peek();
    }
    
    public boolean empty() {
        return front.isEmpty();
        
    }
}
