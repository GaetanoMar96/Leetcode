from collections import defaultdict
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        counts = defaultdict(int)
        for ch in s:
            counts[ch] += 1
        steps = 0
        for ch in t:
            if ch in counts and counts[ch] > 0:
                counts[ch] -= 1
        
        for key in counts:
            steps += counts[key]
        return steps