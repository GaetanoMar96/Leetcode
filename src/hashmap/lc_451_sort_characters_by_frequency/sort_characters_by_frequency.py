from collections import defaultdict
class Solution:
    def frequencySort(self, s: str) -> str:
        occ = defaultdict(int)
        for ch in s:
            occ[ch] += 1
        occ = dict(sorted(occ.items(), key = lambda x: x[1], reverse=True))
        res = ''
        for key in occ:
            res = res + (key * occ[key])
        return res