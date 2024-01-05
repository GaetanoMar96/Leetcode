class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        start = triangle[-1]
        for i in range(len(triangle) - 2, -1, -1):
            temp = triangle[i]
            for j in range(len(temp)):
                temp[j] = min(start[j] + temp[j], start[j+1] + temp[j])
            
            start = temp
        return start[0]