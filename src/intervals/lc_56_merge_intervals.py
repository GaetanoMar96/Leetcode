class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals = sorted(intervals, key = lambda x: x[0])
        res = []
        temp = intervals[0]
        for i in range(1, len(intervals)):
            b = intervals[i]
            if temp[1] >= b[0]:
                temp[1] = max(b[1], temp[1])
            else:
                res.append(temp)
                temp = b
        res.append(temp)
        return res
                