class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        wordDict = set(wordDict)
        memo = {}
        
        def dp(s, res):
            if s in memo:
                return memo[s]
            if s == '' or s in wordDict:
                return True

            for i in range(len(s)):
                res += s[i]
                if res in wordDict:
                    memo[s] = dp(s[i+1:], '')
                    if memo[s]:
                        return True
            
            return False
        return dp(s, '')