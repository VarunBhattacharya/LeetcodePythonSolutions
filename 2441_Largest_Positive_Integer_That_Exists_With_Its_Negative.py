from collections import Counter

class Solution:
    def findMaxK(self, nums) -> int:
        #Approach 1: Time Complexity - O(N) and Space Complexity - O(N)
        c = Counter(nums)
        
        maxVal = -1

        for key, cnt in c.items():
            tempVal = -key
            if tempVal in c.keys():
                maxVal = max(maxVal, abs(key))
        
        return maxVal

if __name__ == "__main__":
    print(Solution().findMaxK([3,2,-2,5,-3]))