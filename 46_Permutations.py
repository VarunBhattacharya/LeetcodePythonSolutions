import itertools
class Solution:
    def permute(self, nums):
        #Method 1 - itertools.permutations - Time Complexity: O(n*n!) and Space Complexity: O(n*n!)
        '''
        return list(itertools.permutations(nums))
        '''

        #Method 2 - Recursive - Time Complexity: O(n*n!) and Space Complexity: O(n*n!)
        '''
        if len(nums) == 1:
            return [nums]
        res = []
        for i in range(len(nums)):
            for j in self.permute(nums[:i] + nums[i+1:]):
                res.append([nums[i]] + j)
        return res
        '''

        #Method 3 - Iterative - Time Complexity: O(n*n!) and Space Complexity: O(n*n!)
        '''
        res = [[]]
        for i in nums:
            res = [j[:k] + [i] + j[k:] for j in res for k in range(len(j)+1)]
        return res
        '''

        #Method 4 - Backtracking - Time Complexity: O(n*n!) and Space Complexity: O(n*n!)
        res = []
        def backtrack(nums, tmp):
            if not nums:
                res.append(tmp)
            for i in range(len(nums)):
                backtrack(nums[:i] + nums[i+1:], tmp + [nums[i]])
        backtrack(nums, [])
        return res


if __name__ == '__main__':
    nums = [1,2,3]
    print(Solution().permute(nums))