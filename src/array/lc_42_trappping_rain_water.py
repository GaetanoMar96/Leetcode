class Solution:
    def trap(self, height: list[int]) -> int:
        length = len(height)
        maxleft = [0] * length
        maxright = [0] * length
        minleftright = [0] * length

        #first pass get all max at the left
        maxleft[0] = 0
        currmax = height[0]
        for i in range(1, length):
            maxleft[i] = currmax
            currmax = max(currmax, height[i])
        #second pass get all max at the right
        maxright[-1] = 0 
        currmax = height[-1]
        for i in range(length - 2, -1, -1):
            maxright[i] = currmax
            currmax = max(currmax, height[i])
        #third pass calculate the height takin min(L,R) - H if > 0   
        for i in range(length):
            res = min(maxleft[i], maxright[i]) - height[i]
            if res > 0:
                minleftright[i] = res
        return sum(minleftright)