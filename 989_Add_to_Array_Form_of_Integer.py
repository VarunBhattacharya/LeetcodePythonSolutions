class Solution:
    def addToArrayForm(self, num, k: int):
        #Naive Approach - Time Complexity - O(N) and Space Complexity - O(1)
        nums = int(''.join([str(i) for i in num]))
        res = list(str(nums+k))
        return [int(x) for x in res]

if __name__ == '__main__':
    s = Solution()
    print(s.addToArrayForm([1,2,0,0],34))