class Solution:
    def rob(self, nums) -> int:
        #Naive Approach: Time Complexity - O(2^n) and Space Complexity - O(1)
        '''
        for i in range(len(nums)):
            if i == 0:
                nums[i] = nums[i]
            elif i == 1:
                nums[i] = max(nums[i], nums[i-1])
            else:
                nums[i] = max(nums[i]+nums[i-2], nums[i-1])
        return nums[-1]
        '''

        #Optimized Approach: Time Complexity - O(N) and Space Complexity - O(1)
        prev1 = 0
        prev2 = 0
        for i in range(len(nums)):
            temp = prev1
            prev1 = max(nums[i]+prev2, prev1)
            prev2 = temp
        return prev1
    

if __name__ == "__main__":
    nums = [1,2,3,1]
    # nums = [2,7,9,3,1]
    print(Solution().rob(nums))