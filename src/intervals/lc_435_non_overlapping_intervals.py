class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals = sorted(intervals, key= lambda x: x[0])
        prev = intervals[0][1]
        count = 0
        for start, end in intervals[1:]:
            if start >= prev: #no overlap
                prev = end
            else:
                mine = min(prev, end)
                count += 1
                prev = mine
        
        return count