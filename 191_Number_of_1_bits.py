class Solution:
    def hammingWeight(self, n: int) -> int:
        #String Manipulation - Wrong answer in Leetcode
        '''
        cnt1 = 0
        for i in str(n):
            if i == '1':
                cnt1 += 1
        return cnt1
        '''

        #Bit Manipulation - Using right shift operation and adding
        '''
        cnt1 = 0
        while n:
            cnt1 += n%2 #add all bits to cnt1
            n = n >> 1 #right shift of bit position
        return cnt1
        '''

        #Bit Manipulation - Removing zeroes from number and then adding 1
        cnt1 = 0
        while n:
            n = n & (n-1)
            cnt1 += 1
        return cnt1

if __name__ == "__main__":
    obj = Solution()
    print(obj.hammingWeight(00000000000000000000000000001011))