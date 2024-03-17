
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def canAttendMeetings(self, intervals: list[Interval]) -> bool:
        if not intervals:
            return True
        intervals = sorted(intervals, key= lambda x: x.start)
        curr = intervals[0]
        for i in range(1, len(intervals)):
            next = intervals[i]
            if curr.end > next.start:
                return False
            curr = next
        return True