class Solution:
    def searchInsert(self, nums, target: int) -> int:
        #Approach 1: Binary Search - Time Complexity - O(logN) and Space Complexity - O(1)
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid
            if nums[mid] < target:
                left = mid + 1
        return right

if __name__ == '__main__':
    nums = [1,3,5,6]
    target = 5
    print(Solution().searchInsert(nums, target))