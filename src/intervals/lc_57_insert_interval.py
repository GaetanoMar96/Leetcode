class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        intervals.append(newInterval)
        intervals = sorted(intervals, key= lambda x: x[0])
        curr = intervals[0]
        for i in range(1, len(intervals)):
            next = intervals[i]
            if next[0] <= curr[1] or next[1] <= curr[0]:
                next = [curr[0], max(next[1], curr[1])]
                intervals[i] = next
                intervals[i-1]=[]
            curr = next
        res = [inter for inter in intervals if inter != []]
        return res

            