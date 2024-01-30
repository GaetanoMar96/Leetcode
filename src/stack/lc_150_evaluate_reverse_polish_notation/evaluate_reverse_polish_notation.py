class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        operators = {'+', '-', '*', '/'}
        for token in tokens:
            if token in operators:
                b = stack.pop()
                a = stack.pop()
                match token:
                    case '+':
                        c = a + b
                    case '-':
                        c = a - b
                    case '*':
                        c = a * b
                    case '/':    
                        c = int(a / b)
                stack.append(c)       
            else:
                stack.append(int(token))
                
        return stack[-1]