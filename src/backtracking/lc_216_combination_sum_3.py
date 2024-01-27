class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        res = []
        def bt(x, comb):
            if len(comb) == k and sum(comb) == n:
                res.append(comb.copy())
                return
            for i in range(x,10):
                if len(comb) < k:
                    comb.append(i)
                    bt(i+1, comb)
                    comb.pop()

        bt(1, [])
        return res