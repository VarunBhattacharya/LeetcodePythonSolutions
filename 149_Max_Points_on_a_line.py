'''
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, 
return the maximum number of points that lie on the same straight line.
'''
import collections
class Solution:
    def maxPoints(self, points) -> int:
        #Better  Approach - Using Hash Table - Time Complexity: O(N^2) and Space Complexity: O(N)
        maxPoints = 1
        for i in range(len(points)):
            p1 = points[i]
            hashCounter = collections.defaultdict(int)
            for j in range(i+1, len(points)):
                p2 = points[j]
                if p2[0] == p1[0]: #for vertical line parallel to y-axis
                    slope = float('inf')
                else:
                    slope = (p2[1] - p1[1]) / (p2[0] - p1[0])
                hashCounter[slope] += 1
                maxPoints = max(maxPoints, hashCounter[slope]+1)
        return maxPoints


if __name__ == "__main__":
    points = [[1,1],[2,2],[3,3]]
    print(Solution().maxPoints(points))