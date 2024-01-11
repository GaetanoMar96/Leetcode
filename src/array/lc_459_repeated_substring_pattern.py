class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        #brute force
        if len(s) == 1:
            return False
        prefix =  ''
        length = len(s) // 2 if len(s) % 2 == 0 else len(s) // 2 + 1
        for i in range(length):
            prefix += s[i]
            if prefix * (len(s) // len(prefix)) == s:
                return True
        return False