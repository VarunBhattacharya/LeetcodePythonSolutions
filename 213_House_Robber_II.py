'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of 
money stashed. All houses at this place are arranged in a "circle". That means the first house is the neighbor 
of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact 
the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money 
you can rob tonight without alerting the police.

Example 1:
Input: nums = [2,3,2]
Output: 3
'''

class Solution:
    def rob(self, nums) -> int:
        #Naive Approach: Dynamic Programming - Time Complexity - O(N) and Space Complexity - O(1)
        def robHouse(nums):
            prev1 = 0
            prev2 = 0
            for i in range(len(nums)):
                temp = prev1
                prev1 = max(nums[i]+prev2, prev1)
                prev2 = temp
            return prev1
        
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        return max(robHouse(nums[1:]), robHouse(nums[:-1]))
    
if __name__ == "__main__":
    nums = [2,3,2]
    print(Solution().rob(nums))