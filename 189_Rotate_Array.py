class Solution:
    def rotate(self, nums, k: int):
        """
        Do not return anything, modify nums in-place instead.
        """
        #Approach 1: Modifiy array in-place - Time Complexity - O(N) and Space Complexity - O(1)
        '''
        k = k % len(nums)
        nums[:] = nums[len(nums)-k:] + nums[:len(nums)-k]
        '''

        #Approach 2: Modifiy array in-place - Time Complexity - O(N) and Space Complexity - O(1)
        def reversal(start, end):
            left = start
            right = end
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left, right = left + 1, right - 1
        
        k = k % len(nums)
        reversal(0, len(nums)-1)
        reversal(0, k - 1)
        reversal(k, len(nums)-1)

if __name__ == '__main__':
    s = Solution()
    nums = [1,2,3,4,5,6,7]
    k = 3
    s.rotate(nums, k)
    print(nums)