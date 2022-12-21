from itertools import combinations


class Solution:
    def maxSubArray(self, nums) -> int:
        # Naive Method -- working only for positive integers - taking only combinations which is wrong
        '''
        def findSumOfArr(nums):
            maxSum = 0
            for i in range(len(nums)):
                maxSum = max(maxSum, sum(nums[i]))
            return maxSum

        maxValSum = 0
        for i in range(1, len(nums)+1):
            tempList = list(combinations(nums,i))
            print(tempList)
            maxValSum = max(maxValSum, findSumOfArr(tempList))
            print(maxValSum)
            tempList = []
        return maxValSum
        '''

        # Better way of writing naive Method - taking only combinations which is wrong
        '''
        combList = []
        for i in range(1, len(nums)+1):
            combList.append(list(combinations(nums, i)))
        maxValSum = 0
        for i in range(len(nums)):
            for j in range(len(combList[i])):
                maxValSum = max(maxValSum, sum(combList[i][j]))
        return maxValSum
        '''

        # Kandane's Algorithm
        maxSum = nums[0]
        curSum = 0
        for i in nums:
            if curSum < 0:
                curSum = 0
            curSum += i
            maxSum = max(curSum, maxSum)
        return maxSum


if __name__ == '__main__':
    s = Solution()
    print(s.maxSubArray([5, 4, -1, 7, 8]))