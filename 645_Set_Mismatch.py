class Solution:
    def findErrorNums(self, nums):
        #Naive Approach - Wrong Solution
        '''
        hashMap = {}
        for i in range(len(nums)):
            hashMap[i] = nums[i]
        
        for ind, val in hashMap.items():
            if hashMap[ind] == hashMap[ind+1]:
                return [hashMap[ind], hashMap[ind]+1]
        return
        '''
        
        #Another Approach - Wrong Solution
        '''
        nums.sort()
        for i in range(len(nums)):
           if i+1 != nums[i]:
               return [nums[i], i+1]
        return
        '''

        #Better Way
        actualSum = sum([int(x) for x in range(len(nums)+1)])
        res = []
        for i in range(len(nums)):
            if nums.count(nums[i]) > 1:
                return [nums[i], actualSum-(sum(nums) - nums[i])]
        return 0

if __name__ == '__main__':
    sol = Solution()
    print(sol.findErrorNums([1,2,2,4]))