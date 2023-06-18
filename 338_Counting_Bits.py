class Solution:
    def countBits(self, n: int):
        #Approach 1: Time Complexity - O(N) and Space Complexity - O(1)
        '''
        res = []
        for i in range(n+1):
            res.append(bin(i)[2:].count('1'))
        return res
        '''
        #Approach 2: DP and Bit Manipulation - Time Complexity - O(N) and Space Complexity - O(1)
        res = [0] * (n+1)
        for i in range(1, n+1):
            res[i] = res[i & (i-1)] + 1
        return res

    
if __name__ == "__main__":
    s = Solution()
    print(s.countBits(5))