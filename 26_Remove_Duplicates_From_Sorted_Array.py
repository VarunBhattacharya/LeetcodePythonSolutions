class Solution:
    def removeDuplicates(self, nums) -> int:
        #Approach 1: Time Complexity - O(N) and Space Complexity - O(1)
        if len(nums) == 0:
            return 0
        cnt = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[cnt]:
                cnt += 1
                nums[cnt] = nums[i]
        return cnt + 1

        #Approach 2: Time Complexity - O(N) and Space Complexity - O(N)
        '''
        nums[:] = sorted(set(nums))
        return len(nums)
        '''

if __name__ == "__main__":
    nums = [1,1,2]
    print(Solution().removeDuplicates(nums))
    print(nums)