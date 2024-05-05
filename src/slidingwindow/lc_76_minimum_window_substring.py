from collections import Counter, defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def areValuesEqual(smap, tmap):
            for key in tmap:
                if key not in smap or smap[key] < tmap[key]:
                    return False
            return True

        tmap = Counter(t)
        minwindow = ''
        currlen = float('inf')

        occs = defaultdict(int)
        l = 0

        for r in range(len(s)):
            occs[s[r]] += 1

            #compare keys
            while l <= len(s) and areValuesEqual(occs, tmap): #shrink while values are same
                if (r -l +1) < currlen:
                    minwindow = s[l:r+1]
                    currlen = r -l +1
                occs[s[l]] -= 1
                l += 1
              

        return minwindow
                