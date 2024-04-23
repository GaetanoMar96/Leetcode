from queue import deque
class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        deadends = set(deadends)
        if '0000' in deadends:
            return -1
 
        res = 0
        q = deque()
        q.append('0000')
        visited = set()
        while q:
            for _ in range(len(q)):
                current = q.popleft()
                if current == target:
                    return res
                if current in visited or current in deadends:
                    continue
                visited.add(current)
                
                #increase by 1 each item of the current lock
                for i in range(len(current)):
                    currlist = list(current)
                    if currlist[i] == '9':
                        currlist[i] = '0'
                    else:
                        currlist[i] = str(int(currlist[i]) + 1)
                    q.append(''.join(currlist))
                #decrease by 1 each item of the current lock
                for i in range(len(current)):
                    currlist = list(current)
                    if currlist[i] == '0':
                        currlist[i] = '9'
                    else:
                        currlist[i] = str(int(currlist[i]) - 1)
                    q.append(''.join(currlist))
            res += 1
       
        return -1