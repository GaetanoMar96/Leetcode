class Solution:
    #Time complex O(n)
    #Space complex O(n)
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        length = len(temperatures)
        res = [0] * length
        stack = []
        for i in range(len(temperatures)): #last value is always 0
            temp = temperatures[i]
            if not stack:
                stack.append((temp, i)) #store value and index
                continue
            while stack:
                if temp <= stack[-1][0]: # continue storing
                    break
                tempPre, idxPre = stack.pop()
                res[idxPre] = i - idxPre

            stack.append((temp, i))
        return res