'''
Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of 
nums.

A circular array means the end of the array connects to the beginning of the array. Formally, 
the next element of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].

A subarray may only include each element of the fixed buffer nums at most once. Formally, for a 
subarray nums[i], nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.


Example 1:
Input: nums = [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3.

Example 2:
Input: nums = [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10.
'''


class Solution:
    def maxSubarraySumCircular(self, nums) -> int:
        #Approach 1: Kandane Algorithm - Time Complexity - O(N) and Space Complexity - O(1)
        #Kandane Algorithm for Maximum Subarray Sum
        max_sum = nums[0]
        curr_sum = nums[0]
        for i in range(1, len(nums)):
            curr_sum = max(curr_sum + nums[i], nums[i])
            max_sum = max(max_sum, curr_sum)

        #Kandane Algorithm for Minimum Subarray Sum
        min_sum = nums[0]
        curr_sum = nums[0]
        for i in range(1, len(nums)):
            curr_sum = min(curr_sum + nums[i], nums[i])
            min_sum = min(min_sum, curr_sum)

        #If all the elements are negative, then return the maximum element
        if sum(nums) == min_sum:
            return max_sum
        
        #Else return the maximum of the two sums
        return max(max_sum, sum(nums) - min_sum)

if __name__ == '__main__':
    s = Solution()
    print(s.maxSubarraySumCircular([1,-2,3,-2]))
    print(s.maxSubarraySumCircular([5,-3,5]))