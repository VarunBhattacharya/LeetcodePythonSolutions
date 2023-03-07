class Solution:
    def minimumTime(self, time, totalTrips: int) -> int:
        #Naive Approach: Binary Search Time Complexity - O(logN) and Space Complexity - O(1)
        if len(time) == 1:
            return time[0] * totalTrips
        
        left, right = 0, pow(10,15)

        while left < right:
            mid = (left + right) // 2

            res = 0
            for i in time:
                res += mid // i

            if res >= totalTrips:
                right = mid
            
            else:
                left = mid + 1
            
        return left

if __name__ == '__main__':
    s = Solution()
    print(s.minimumTime([1,2,3], 5))