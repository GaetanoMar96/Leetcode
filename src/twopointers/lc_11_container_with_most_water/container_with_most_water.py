class Solution:
    def maxArea(self, height: list[int]) -> int:
        l, r = 0, len(height) - 1
        area = 0
        y = 0
        x = r - l
        while l <= r:
            if height[l] < height[r]:
                y = height[l]
                l += 1
            else:
                y = height[r]
                r -= 1
            
            area = max(area, y * x)
            x = r - l 

        return area