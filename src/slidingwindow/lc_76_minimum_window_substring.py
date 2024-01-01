from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        maps, mapt = defaultdict(int), defaultdict(int)
        def getMapt():
            for ch in t:
                mapt[ch] += 1
        def compareMaps():
            if len(mapt) != len(maps):
                return False
            for k in maps:
                if k not in mapt or maps[k] < mapt[k]:
                    return False
            return True 
        
        getMapt()
        l = 0
        windowst = ''
        valid = s + '_'
        for r in range(len(s)):
            if s[r] in mapt:
                maps[s[r]] += 1
            
            windowst += s[r]
            while compareMaps():
                if len(windowst) <= len(valid):
                    valid = windowst
                ch = s[l] 
                if ch in maps:
                    maps[ch] -= 1
                l += 1
                windowst = windowst[1:]
        
        if valid == s + '_':
            return ''
   
        return valid