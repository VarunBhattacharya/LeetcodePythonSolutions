import functools

class Solution:
    def tribonacci(self, n: int) -> int:
        #Approach 1: Recursion - Time Complexity - [O(2^n), O(N)] and Space Complexity - O(N)
        '''
        if n <= 1:
            return n
        if n == 2:
            return 1
        return self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
        '''

        #Approach 2: Iterative - Time Complexity - O(N) and Space Complexity - O(1)
        '''
        if n <= 1:
            return n
        if n == 2:
            return 1
        a, b, c = 0, 1, 1
        for i in range(3, n+1):
            a, b, c = b, c, a+b+c
        return c
        '''

        #Approach 3: Memoization (without inbuilt function) - Faster Method
        '''
        def trib(n, computed = {0:0, 1:1, 2:1}): #reducing multiple time calculations
            if n not in computed:
                computed[n] = trib(n-1, computed) + trib(n-2, computed) + trib(n-3, computed)
            return computed[n]
        return trib(n, computed = {0:0, 1:1, 2:1})
        '''

        #Approach 4: Memoization (using inbuilt function) - Faster Method
        @functools.lru_cache(None) #decorators
        def trib(n):
            if n <= 1:
                return n
            if n == 2:
                return 1
            return trib(n-1) + trib(n-2) + trib(n-3)
        return trib(n)


if __name__ == '__main__':
    n = 4
    obj = Solution()
    print(obj.tribonacci(n))