class Solution:
    def singleNonDuplicate(self, nums) -> int:
        #Naive Approach: Two Pointer - Time Complexity - O(N) and Space Complexity - O(1)
        '''
        prev = 0
        curr = 1
        while curr < len(nums):
            if nums[prev] != nums[curr]:
                return nums[prev]
            prev += 2
            curr += 2
        return nums[prev]
        '''

        #Approach 2: Binary Search - Time Complexity - O(log N) and Space Complexity - O(1)
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if mid % 2 == 1:
                mid -= 1
            if nums[mid] == nums[mid + 1]:
                left = mid + 2
            else:
                right = mid
        return nums[left]

if __name__ == '__main__':
    s = Solution()
    print(s.singleNonDuplicate([1,1,2,3,3,4,4,8,8]))
    print(s.singleNonDuplicate([1, 1, 2]))