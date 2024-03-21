class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points = sorted(points, key=lambda x: x[0])
        prev = points[0]
        for i in range(1, len(points)):
            curr = points[i]
            if curr[0] <= prev[1]:
                curr = [prev[0], min(prev[1], curr[1])]
                points[i-1]= []
                points[i] = curr
            prev = curr
        return len([i for i in points if i != []])