from heap import heapq
from collections import Counter
from queue import deque
class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        count = Counter(tasks)
        heap = [-c for c in count.values()] # store letters occ
        heapq.heapify(heap) # create max heap
        time = 0
        q = deque() # queue to store the occ and when the letter will be available after time + idle
        while heap or q:
            time += 1
            if not heap:
                time = q[0][1] 
            else:
                count = 1 + heapq.heappop(heap)
                if count != 0:
                    q.append((count, time + n))
            if q and q[0][1] == time:
                heapq.heappush(heap, q.popleft()[0])

        return time