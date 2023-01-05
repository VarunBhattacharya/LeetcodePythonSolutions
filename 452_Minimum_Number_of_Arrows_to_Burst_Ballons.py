class Solution:
    def findMinArrowShots(self, points) -> int:
        if not points:
            return 0
        points.sort()
        intersectPoints = 1
        prev = points[0]
        for start, end in points[1:]:
            if start > prev[1]: #no overlap
                intersectPoints += 1
                prev = [start,end]
            else: #overlap
                prev[1] = min(prev[1], end)
        return intersectPoints

if __name__ == '__main__':
    points = [[10,16],[2,8],[1,6],[7,12]]
    print(Solution().findMinArrowShots(points))