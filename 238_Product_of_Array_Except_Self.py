class Solution:
    def productExceptSelf(self, nums):
        #Approach - 1
        '''
        def prod(nums):
            prodVal = 1
            for i in range(len(nums)):
                prodVal *= nums[i]
            return prodVal
        
        seen = []
        res = []
        for i in range(len(nums)):
            res.append(prod(nums[i+1:]) * prod(seen))
            seen.append(nums[i])
        return res
        '''

        #Better Method
        '''
        res = [1] * len(nums)
        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1]
        right = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= right
            right *= nums[i]
        return res
        '''

        #Better Method
        res = []
        prefixVal, postfixVal = 1, 1
        for i in range(len(nums)): #calculate the prefix value in first pass
            res.append(prefixVal)
            prefixVal *= nums[i]
        for i in range(len(nums)-1, -1, -1): #calculate the postfix value in back pass
            res[i] = res[i] * postfixVal
            postfixVal *= nums[i]
        return res


if __name__ == '__main__':
    nums = [1,2,3,4]
    print(Solution().productExceptSelf(nums))