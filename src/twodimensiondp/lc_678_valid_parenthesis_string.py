class Solution:
    def checkValidString(self, s: str) -> bool:
        memo = {}
        def dp(i, count):
            if i >= len(s) or count < 0:
                return count == 0
            if (i, count) in memo:
                return memo[(i,count)]
            res = False
            if s[i] == '(':
                res = dp(i+1, count+1)
            elif s[i] == ')':
                res = dp(i+1, count-1)
            else:
                res = (dp(i+1, count+1) or dp(i+1, count-1) or dp(i+1, count))
            memo[(i,count)] = res
            return res
        return dp(0, 0)