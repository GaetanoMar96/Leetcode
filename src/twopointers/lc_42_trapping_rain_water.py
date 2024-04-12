class Solution:
    def trap(self, height: list[int]) -> int:
        length = len(height)
        l, r = 0, length - 1
        maxleft, maxright = height[l], height[r]
        res = 0
        #always get the minimum between maxleft and maxright
        while l < r:
            if maxleft < maxright:
                l += 1
                maxleft = max(maxleft, height[l])
                res += maxleft - height[l]
            else:
                r -= 1
                maxright = max(maxright, height[r])
                res += maxright - height[r]
        return res