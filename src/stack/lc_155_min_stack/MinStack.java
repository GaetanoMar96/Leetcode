package stack.lc_155_min_stack;

import java.util.*;

public class MinStack {
    
    Stack<Integer> stack;
    PriorityQueue<Integer> pq;

    public MinStack() {
        stack = new Stack<>();
        pq = new PriorityQueue<>();    
    }
    
    public void push(int val) {
        stack.push(val);
        pq.add(val);
    }
    
    public void pop() {
        Integer val = stack.pop();
        pq.remove(val);
    }
    
    public int top() {
        return stack.peek();
    }
    
    public int getMin() {
        return pq.peek();
    }
}
