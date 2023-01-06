class Solution:
    def minimumAverageDifference(self, nums) -> int:
        #Naive Solution - O(N^2) solution
        '''
        diffArr = []

        if len(nums) == 0:
            return

        if nums == [0]:
            return 0

        for i in range(len(nums)-1):
            secondHalf = int(sum(nums[i+1:])/len(nums[i+1:]))
            firstHalf = int(sum(nums[:i+1])/len(nums[:i+1]))
            tempDiff = int(round(abs(firstHalf - secondHalf)))
            diffArr.append(tempDiff)
        diffArr.append(int(sum(nums[:len(nums)-1])/len(nums[:len(nums)-1])))
        return diffArr.index(min(diffArr))
        '''

        #Better Solution - O(N) solution
        total = sum(nums)
        mn, idx = float("inf"), -1
        prefix = 0
        for i, x in enumerate(nums):
            prefix += x
            a = prefix//(i+1)
            b = (total-prefix)//(len(nums)-(i+1)) if i+1 < len(nums) else 0
            diff = abs(a-b)
            if diff < mn:
                mn, idx = diff, i
        return idx

if __name__ == "__main__":
    nums = [2,5,3,9,5,3]
    print(Solution().minimumAverageDifference(nums))