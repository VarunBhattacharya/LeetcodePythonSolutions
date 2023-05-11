class Solution:
    def removeElement(self, nums, val: int) -> int:
        #Approach 1 - Time Complexity: O(N^2) and Space Complexity - O(1)
        '''
        while nums.__contains__(val): #while val in nums
            nums.remove(val) #left shift operation takes place every single run
        return len(nums)
        '''

        #Naive Approach - Time Complexity: O(N) and Space Complexity: O(1)
        cnt = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[cnt] = nums[i]
                cnt += 1
        return cnt

if __name__ == '__main__':
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    print(Solution().removeElement(nums, val))