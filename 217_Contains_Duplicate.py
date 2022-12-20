class Solution:
    def containsDuplicate(self, nums) -> bool:
        #Better Force
        '''
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False
        '''
        
        #Better Solution
        hashSet = set()
        for i in nums:
            if i in hashSet:
                return True
            hashSet.add(i)
        return False

        #Better Solution
        '''
        return len(nums) != len(set(nums))
        '''

if __name__ == '__main__':
    nums = [1,2,3,1]
    print(Solution().containsDuplicate(nums))