from collections import Counter

class Solution:
    def singleNumber(self, nums) -> int:
        #Approach 1: Time Complexity - O(N) and Space Complexity - O(N)
        '''
        hashCnt = Counter(nums)
        for key, val in hashCnt.items():
            if val == 1:
                return key
        return 0
        '''
        #Approach 2: Time Complexity - O(N) and Space Complexity - O(1)
        return 2 * sum(set(nums)) - sum(nums)



if __name__ == "__main__":
    s = Solution()
    print(s.singleNumber([2,2,1]))
    print(s.singleNumber([4,1,2,1,2]))
    print(s.singleNumber([1]))