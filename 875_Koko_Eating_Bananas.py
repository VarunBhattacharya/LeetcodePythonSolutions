import math

class Solution:
    def minEatingSpeed(self, piles, h: int) -> int:
        #Approach  1: Binary Search - Time Complexity - O(NlogN) and Space Complexity - O(1)
        start, end = 1, max(piles)
        res = end

        while start <= end:
            mid = (start + end) // 2
            hours = 0
            for i in piles:
                hours += math.ceil(i/mid)
            if hours <= h:
                res = min(res,mid)
                end = mid - 1
            else:
                start = mid + 1
        
        return res


if __name__ == '__main__':
    piles = [3,6,7,11]
    h = 8
    print(Solution().minEatingSpeed(piles, h))