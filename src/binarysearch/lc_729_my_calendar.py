from sortedcontainers import SortedList
import bisect

class MyCalendar:

    def __init__(self):
        #keep elements in sorted order
        self.calendar = SortedList(key=lambda x: x[0])
        
    def book(self, start: int, end: int) -> bool: 
        idx = bisect.bisect_right(self.calendar, [start, end])
        
        if (idx > 0 and self.calendar[idx-1][1] > start) or (idx < len(self.calendar) and self.calendar[idx][0] < end):
            return False
                
        self.calendar.add([start, end])
        return True