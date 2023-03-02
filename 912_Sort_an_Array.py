class Solution:
    def sortArray(self, nums):
        #Approach 1: Using built-in (Tim Sort) - Time Complexity - O(NlogN) and Space Complexity - O(N)
        '''
        nums.sort()
        return nums
        # return sorted(nums)
        '''

        #Approach 2 - Tim Sort - Time Complexity - O(NlogN) and Space Complexity - O(N) - TLE
        '''
        def insertion_sort(nums, left, right):
            for i in range(left + 1, right + 1):
                key_item = nums[i]
                j = i - 1
                while j >= left and nums[j] > key_item:
                    nums[j + 1] = nums[j]
                    j -= 1
                nums[j + 1] = key_item
            return nums
        
        def merge_sort(nums, left, right):
            if right - left < 32:
                return insertion_sort(nums, left, right)
            mid = (left + right) // 2
            first_half = merge_sort(nums, left, mid)
            second_half = merge_sort(nums, mid + 1, right)
            return merge(first_half, second_half)
        
        def merge(first_half, second_half):
            if not first_half:
                return second_half
            if not second_half:
                return first_half
            if first_half[0] < second_half[0]:
                return [first_half[0]] + merge(first_half[1:], second_half)
            return [second_half[0]] + merge(first_half, second_half[1:])

        min_run = 32
        n = len(nums)
        for i in range(0, n, min_run):
            insertion_sort(nums, i, min((i + min_run - 1), n - 1))
        size = min_run
        while size < n:
            for start in range(0, n, size * 2):
                mid = start + size - 1
                end = min((start + size * 2 - 1), (n-1))
                merged_numsay = merge(nums[start:mid+1], nums[mid+1:end+1])
                nums[start:start + len(merged_numsay)] = merged_numsay
            size *= 2
        return nums
        '''

        #Approach 3 - Merge Sort - Time Complexity - O(NlogN) and Space Complexity - O(N)
        def merge(left, right):
            result = []
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            result += left[i:]
            result += right[j:]
            return result
        
        def merge_sort(nums):
            if len(nums) <= 1:
                return nums
            mid = len(nums) // 2
            left = merge_sort(nums[:mid])
            right = merge_sort(nums[mid:])
            return merge(left, right)
        
        return merge_sort(nums)

if __name__ == "__main__":
    sol = Solution()
    print(sol.sortArray([5,2,3,1]))