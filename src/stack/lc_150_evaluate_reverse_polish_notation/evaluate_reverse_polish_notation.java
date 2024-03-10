import java.util.Stack;

class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> stack = new Stack<>();
        int v1;
        int v2;
        for(int i = 0; i < tokens.length; i++) {
            switch(tokens[i]) {
                case "+":
                    v2 = stack.pop();
                    v1 = stack.pop();
                    stack.push(v1 + v2);
                    break;
                case "-":
                    v2 = stack.pop();
                    v1 = stack.pop();
                    stack.push(v1- v2);
                    break;
                case "*":
                    v2 = stack.pop();
                    v1 = stack.pop();
                    stack.push(v1 * v2);
                    break;
                case "/":
                    v2 = stack.pop();
                    v1 = stack.pop();
                    stack.push(v1 / v2);
                    break;
                default:
                    stack.push(Integer.parseInt(tokens[i]));                
            }
        }
        return stack.peek();
    }
}