import bisect

class Solution:
    def jobScheduling(self, startTime: list[int], endTime: list[int], profit: list[int]) -> int:
        #brute force try every combinations of intervals which not overlap
        cache = {}
        intervals = []
        def dfs(i):
            if i >= len(intervals):
                return 0
            if i in cache:
                return cache[i]
            
            #do not include i interval
            res = dfs(i+1)
            #include i + next profit which does not overlap using bfs
            j = bisect.bisect_right(intervals, [intervals[i][1], -1, -1])        
            cache[i] = max(res, dfs(j) + intervals[i][2]) 
            return cache[i]
        
        for i in range(len(startTime)):
            start, end = startTime[i], endTime[i]
            intervals.append([start,end, profit[i]])
        intervals = sorted(intervals, key = lambda x: x[0])
        return dfs(0)