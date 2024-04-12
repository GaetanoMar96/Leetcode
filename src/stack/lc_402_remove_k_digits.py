class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for head in num:
            while stack and head < stack[-1] and k > 0:
                stack.pop()
                k -= 1
            stack.append(head)
        
        stack = stack[:len(stack)-k] #get the actual length
        #remove leading 0
        while stack and stack[0] == '0':
            stack.pop(0)
        return ''.join(stack) if stack else '0'