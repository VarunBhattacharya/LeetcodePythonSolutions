import math

class Solution:
    def increasingTriplet(self, nums) -> bool:
        #Naive Approach: Time Complexity - O(N^3) and Space Complexity - O(1)
        '''
        if len(nums) < 3:
            return False
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if (nums[j] > nums[i]) and (nums[k] > nums[i]):
                        return True
        return False
        '''

        #Better Approach: Time Complexity - O(N^2) and Space Complexity - O(N)
        '''
        if len(nums) < 3:
            return False
        hashMap = {}
        for i in range(len(nums)):
            hashMap[i] = []
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    hashMap[i].append(nums[j])
        for key in hashMap:
            if len(hashMap[key]) > 1:
                return True
        return False
        '''

        #Better Approach: Time Complexity - O(N) and Space Complexity - O(1)
        val1, val2 = math.inf, math.inf
        if len(nums) < 3:
            return False
        for num in nums:
            if num <= val1:
                val1 = num
            elif num <= val2:
                val2 = num
            else:
                return True
        return False

if __name__ == "__main__":
    s = Solution()
    print(s.increasingTriplet([1,2,3,4,5]))
    print(s.increasingTriplet([2,1,5,0,4,6]))