'''
You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.

Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.
'''


class Solution:
    def maxOperations(self, nums, k: int) -> int:
        #Approach 1: Two Pointer Approach - Time Complexity - O(N) and Space Complexity - O(1)
        nums.sort()
        pnt1, pnt2 = 0, len(nums)-1
        cnt = 0
        while pnt1 < pnt2:
            if nums[pnt1] + nums[pnt2] == k:
                cnt += 1
                pnt1 += 1
                pnt2 -= 1
            elif nums[pnt1] + nums[pnt2] > k:
                pnt2 -= 1
            else:
                pnt1 += 1
        return cnt


if __name__ == '__main__':
    nums = [1,2,3,4]
    k = 5
    print(Solution().maxOperations(nums,k))