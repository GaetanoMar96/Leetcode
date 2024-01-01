from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        occ = defaultdict(int)
        l = 0
        window = 0
        for r in range(len(s)):
            occ[s[r]] += 1
            while occ[s[r]] > 1:
                occ[s[l]] -= 1
                if occ[s[l]] == 0:
                    del occ[s[l]]
                l += 1
            window = max(window, len(occ))
        return window