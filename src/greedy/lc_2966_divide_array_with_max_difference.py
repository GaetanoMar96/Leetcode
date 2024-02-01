class Solution:
    def divideArray(self, nums: list[int], k: int) -> list[list[int]]:
        #Time complex O(nlogn)
        #Space complex O(n**2)
        nums.sort()
        res = []
        level = []
        while nums:
            num = nums.pop(0)
            if not level:
                level.append(num)
                continue
            if len(level) == 3:
                res.append(level)
                level = [num]
                continue
            if abs(level[-1] - num) <= k:
                level.append(num)
            else:
                res.append(level)
                level = []
        if level:
            res.append(level)
        #check if all sub arrays have len = 3 and diff < k
        for l in res:
            if len(l) != 3:
                return []
            if abs(l[-1] - l[0]) > k:
                return []
        return res