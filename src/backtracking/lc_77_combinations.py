class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        self.l = n+1
        res = []
        used = [False] * (n + 1)
        def bt(i, comb):
            if len(comb) == k:
                res.append(comb.copy())

            for j in range(i, self.l):
                if not used[i]:
                    used[i] = True
                    comb.append(j)
                    bt(j+1, comb)
                    comb.pop()
                    used[i] = False
        bt(1, [])
        return res