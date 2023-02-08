class Solution:
    def jump(self, nums) -> int:
        #Approach 1 - Dynamic Programming - Time Complexity - O(N^2) and Space Complexity - O(1)
        '''
        minJump = [float('inf')] * len(nums)
        minJump[0] = 0
        for i in range(1, len(nums)):
            for j in range(i):
                if j + nums[j] >= i:
                    minJump[i] = min(minJump[i], minJump[j] + 1)
        return minJump[-1]
        '''

        #Approach 2 - Greedy Approach - Time Complexity - O(N) and Space Complexity - O(1)
        minJump = 0
        left = right = 0
        while right < len(nums) - 1:
            farPos = 0
            for i in range(left, right+1):
                farPos = max(farPos, i + nums[i])
            left = right + 1
            right = farPos
            minJump += 1
        return minJump


if __name__ == '__main__':
    s = Solution()
    print(s.jump([2,3,1,1,4]))
    print(s.jump([2,3,0,1,4]))