from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        l, r = 0, 0
        res = 0
        for r in range(len(s)):
            count[s[r]] += 1 #increment value of key
            window = sum(count.values())
            
            if window - max(count.values()) <= k:
                res = max(res, window)  
                continue
            
            while window - max(count.values()) > k: #no valid window
                count[s[l]] -= 1
                window = sum(count.values())
                l += 1
                 
        return res




            
        