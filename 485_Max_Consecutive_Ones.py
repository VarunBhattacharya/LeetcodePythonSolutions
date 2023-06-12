class Solution:
    def findMaxConsecutiveOnes(self, nums) -> int:
        #Approach 1: Sliding Window - Time Complexity - O(N) and Space Complexity - O(1)
        '''
        maxSum = 0
        pnt1, pnt2 = 0, 0

        while pnt1 < pnt2 and pnt2 < len(nums):
            if nums[pnt2] == 1:
                tempCnt += 1
            else:
                pnt1 = pnt2 + 1
            pnt2 += 1
        return maxSum
        '''

        #Approach 2: Sliding Window - Time Complexity - O(N) and Space Complexity - O(1)
        maxCnt = 0
        pnt1, pnt2 = 0, 0
        
        while pnt2 < len(nums):
            if nums[pnt2] == 1:
                pnt2 += 1
            else:
                maxCnt = max(maxCnt, pnt2 - pnt1)
                pnt1 = pnt2 + 1
                pnt2 += 1
        maxCnt = max(maxCnt, pnt2 - pnt1)
        return maxCnt

if __name__ == "__main__":
    nums = [1,1,0,0,1,1,1]
    print(Solution().findMaxConsecutiveOnes(nums))