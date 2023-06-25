class Solution:
    def search(self, nums, target: int) -> int:
        #Approach 1: Binary Search - Time Complexity - O(logN) and Space Complexity - O(1)
        start = 0
        end = len(nums)-1

        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                start = mid + 1
            if nums[mid] > target:
                end = end - 1
        return -1

if __name__ == '__main__':
    nums = [-1,0,3,5,9,12]
    target = 9
    s = Solution()
    print(s.search(nums, target))