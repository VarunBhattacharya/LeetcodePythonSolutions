class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        #Naive Method
        '''
        if n == 1: return True
        for i in range(n//2+1):
            if pow(2,i) == n:
                return True
        return False
        '''
        #Better Method - Time Complexity - O(logN), Space Complexity - O(1)
        '''
        if n <= 0:
            return False
        while n%2 == 0:
            n /= 2
        return n == 1
        '''

        #Better Method - Time and Space Complexity - O(1)
        if n <= 0:
            return False
        return n & (n-1) == 0

if __name__ == "__main__":
    s = Solution()
    print(s.isPowerOfTwo(16))