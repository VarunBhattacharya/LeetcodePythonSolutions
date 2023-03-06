'''
You are given an integer array nums. You want to maximize the number of points you get by performing 
the following operation any number of times:

Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must delete every 
element equal to nums[i] - 1 and every element equal to nums[i] + 1.

Return the maximum number of points you can earn by applying the above operation some number of times.

Example 1:
Input: nums = [3,4,2]
Output: 6
Explanation: You can perform the following operations:
- Delete 4 to earn 4 points. Consequently, 3 is also deleted. nums = [2].
- Delete 2 to earn 2 points. nums = [].
You earn a total of 6 points.
'''

class Solution:
    def deleteAndEarn(self, nums) -> int:
        #Naive Approach: Time Complexity - O(N^2) and Space Complexity - O(N) --> Wrong Answer for [3,1]
        '''
        if len(nums) == 1:
            return nums[0]
        maxSum = 0
        for i in range(len(nums)):
            sum = 0
            for j in range(len(nums)):
                if nums[j] == nums[i] - 1 or nums[j] == nums[i] + 1:
                    sum += nums[j]
            if sum > maxSum:
                maxSum = sum
        return maxSum
        '''
    
        #Approach 2: Time Complexity - O(N^2) and Space Complexity - O(N)
        '''
        nums.sort()
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = nums[i]
            for j in range(i-1, -1, -1):
                if nums[i] - nums[j] > 1:
                    dp[i] = max(dp[i], dp[j] + nums[i])
        return max(dp)
        '''

        #Optimized Approach: Time Complexity - O(N) and Space Complexity - O(N)
        if not nums:
            return 0
        max_num = max(nums)
        dp = [0] * (max_num + 1)
        for num in nums:
            dp[num] += num
        for i in range(2, len(dp)):
            dp[i] = max(dp[i-1], dp[i-2] + dp[i])
        return dp[-1]
    

if __name__ == "__main__":
    nums = [3,4,2]
    print(Solution().deleteAndEarn(nums))