class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        self.l = len(candidates)
        res = []
        def bt(comb):
            if sum(comb) > target:
                return
            if sum(comb) == target and sorted(comb) not in res:
                res.append(sorted(comb).copy())
                return

            for j in range(self.l):
                comb.append(candidates[j])
                bt(comb)
                comb.pop()
        bt([])
        return res