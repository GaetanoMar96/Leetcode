class Solution:
    def validateStackSequences(self, pushed: list[int], popped: list[int]) -> bool:
        stack = []
        if not pushed and not popped:
            return True
        if (not pushed and popped) or (pushed and not popped):
            return False

        while pushed:
            val = pushed.pop(0)
            if val == popped[0]:
                popped.pop(0)
                
                while popped and stack and popped[0] == stack[-1]:
                    popped.pop(0)
                    stack.pop()
            else:
                stack.append(val)
        
        while popped:
            if popped.pop(0) != stack.pop():
                return False
        return True
            