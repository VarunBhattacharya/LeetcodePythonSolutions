class Solution:
    def pivotIndex(self, nums) -> int:
        #Approach 1: Prefix Sum - Time Complexity - O(N) and Space Complexity - O(1)
        totSum = sum(nums)
        prevSum = 0
        for i in range(len(nums)):
            forwardSum = totSum - nums[i] - prevSum
            if prevSum == forwardSum:
                return i
            prevSum += nums[i]
        return -1

if __name__ == "__main__":
    nums = [1,7,3,6,5,6]
    print(Solution().pivotIndex(nums))