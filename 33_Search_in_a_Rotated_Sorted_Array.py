class Solution:
    def search(self, nums, target: int) -> int:
        #Naive Solution - O(N) solution
        '''
        return nums.index(target) if target in nums else -1
        '''

        #Better Solution - O(logN) solution
        '''
        numsClone = nums
        numsClone.sort()
        left, right = 0, len(nums)-1
        mid = 0
        while left <= right:
            mid = left + (right-left)//2
            if numsClone[mid] == target:
                return nums.index(target)
            elif target < numsClone[mid]:
                right = mid - 1
            elif target > numsClone[mid]:
                left = mid + 1
        return -1
        '''

        #Better Solution - Custom Binary Search Algorithm - O(logN) solution
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid

            #left sorted portion
            if nums[mid] >= nums[left]:
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
             
            #right sorted portion
            if nums[mid] <= nums[right]:
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1


if __name__ == "__main__":
    nums = [4,5,6,7,0,1,2]
    target = 0
    print(Solution().search(nums, target))