class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        #Approach 1: Time Complexity - O(N) and Space Complexity - O(1)
        '''
        cntZero = 1
        i = 0
        while i <  len(nums):
            if nums[i] == 0:
                cntZero += 1
                nums.pop(i)
            i += 1
        for i in range(cntZero-1):
            nums.append(0)
        return nums
        '''
    
        #Approach 2: Time Complexity - O(N) and Space Complexity - O(1)
        cntZero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[cntZero], nums[i] = nums[i], nums[cntZero]
                cntZero += 1
        return nums



if __name__ == "__main__":
    s = Solution()
    print(s.moveZeroes([0,1,0,3,12]))