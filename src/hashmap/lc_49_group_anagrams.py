from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = []
        hashmap = defaultdict(list)
        for st in strs:
            stsorted = ''.join(sorted(st))
            hashmap[stsorted].append(st)
        for key in hashmap:
            res.append(hashmap[key])
        return res