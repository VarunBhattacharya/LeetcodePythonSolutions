'''
You are given an integer array nums and two integers minK and maxK.

A fixed-bound subarray of nums is a subarray that satisfies the following conditions:

    The minimum value in the subarray is equal to minK.
    The maximum value in the subarray is equal to maxK.

Return the number of fixed-bound subarrays.

A subarray is a contiguous part of an array.

Example 1:
Input: nums = [1,3,5,2,7,5], minK = 1, maxK = 5
Output: 2
Explanation: The fixed-bound subarrays are [1,3,5] and [1,3,5,2].
'''

class Solution:
    def countSubarrays(self, nums, minK: int, maxK: int) -> int:
        #Approach 1: Sliding Window - Time Complexity - O(N) and Space Complexity - O(1)
        subArrayCount = 0
        startPos = 0
        minFound = maxFound = False
        for i in range(len(nums)):
            if nums[i] < minK or nums[i] > maxK:
                minFound = maxFound = False
                startPos = i + 1
            if nums[i] == minK:
                minFound = True
                minStart = i
            if nums[i] == maxK:
                maxFound = True
                maxStart = i
            if minFound and maxFound:
                subArrayCount += min(minStart, maxStart) - startPos + 1
        return subArrayCount


if __name__ == "__main__":
    nums = [1,3,5,2,7,5]
    minK = 1
    maxK = 5
    print(Solution().countSubarrays(nums, minK, maxK))