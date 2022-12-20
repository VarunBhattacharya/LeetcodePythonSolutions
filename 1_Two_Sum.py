class Solution:
    def twoSum(self, nums, target: int):
        #O(n^2) solution
        '''
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        return
        '''
        #O(n) solution
        prevMap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return

if __name__ == '__main__':
    nums = [2,7,11,15]
    target = 9
    print(Solution().twoSum(nums,target))