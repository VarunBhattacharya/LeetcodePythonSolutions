class Solution:
    def shipWithinDays(self, weights, days: int) -> int:
        #Approach 1: Binary Search - Time Complexity - O(N*logM) and Space Complexity - O(1)
        left, right = max(weights), sum(weights)
        res = right

        def canShipHold(cap):
            ships, currCap = 1, cap
            for w in weights:
                if currCap - w < 0:
                    ships += 1
                    currCap = cap
                currCap -= w
            return ships <= days
        
        #binary search
        while left <= right:
            midCap = (left + right) // 2
            if canShipHold(midCap):
                res = min(midCap, res)
                right = midCap - 1
            else:
                left = midCap + 1
        return res

if __name__ == '__main__':
    weights = [1,2,3,4,5,6,7,8,9,10]
    days = 5
    print(Solution().shipWithinDays(weights, days))