class Solution:
    def maximumGap(self, nums) -> int:
        #Naive Method - O(NlogN)
        if len(nums) < 2:
            return 0
        nums.sort()
        maxDiff = 0
        for i in range(len(nums)-1):
            maxDiff =  max(maxDiff, abs(nums[i+1]-nums[i]))
        return maxDiff

if __name__ == '__main__':
    s = Solution()
    print(s.maximumGap([3,6,9,1]))