class Solution:
    def findMin(self, nums) -> int:
        #Naive Method - O(N) solution
        '''
        return min(nums)
        '''

        #Better Method - Custom Binary Search Algorithm - O(logN) solution
        minVal = nums[0]
        left, right = 0, len(nums)-1
        while left <= right:
            if nums[left] < nums[right]:
                minVal = min(minVal, nums[left])
            mid = (left+right)//2
            minVal = min(minVal, nums[mid])
            if nums[mid] >= nums[left]:
                left = mid+1
            else:
                right = mid-1
        return minVal

if __name__ == "__main__":
    nums = [3,4,5,1,2]
    print(Solution().findMin(nums))