class Solution:
    def maxLength(self, arr: list[str]) -> int:
        self.max = 0
        used = [False] * len(arr)
        def hasUniqueChars(s):
            return len(set(s)) == len(s)
        
        def backtrack(i, comb):
            if i >= len(arr):
                return

            for j in range(i, len(arr)):
                if not used[j]:
                    comb.append(arr[j])
                    s = ''.join(comb)
                    if hasUniqueChars(s) and len(s) > self.max:
                        self.max = len(s)
                    used[j] = True
                    backtrack(j+1, comb)
                    comb.pop()
                    used[j] = False
        
        backtrack(0, [])
        return self.max