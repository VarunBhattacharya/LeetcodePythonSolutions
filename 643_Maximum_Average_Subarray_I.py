class Solution:
    def findMaxAverage(self, nums, k: int) -> float:
        #Approach 1: Sliding Window - Time Complexity - O(N) and Space Complexity - O(1)
        if len(nums) == 0:
            return
        pnt1, pnt2 = 0, k - 1
        currentSum = sum(nums[pnt1:pnt2+1])
        maxSum = currentSum
        while pnt2 < len(nums) - 1:
            pnt1 += 1
            pnt2 += 1
            currentSum = currentSum - nums[pnt1-1] + nums[pnt2]
            maxSum = max(maxSum, currentSum)
        return maxSum / k

if __name__ == '__main__':
    nums = [1,12,-5,-6,50,3]
    k = 4
    print(Solution().findMaxAverage(nums,k))