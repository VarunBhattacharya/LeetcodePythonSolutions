from functools import lru_cache
import math
class Solution:
    def climbStairs(self, n: int) -> int:
        #Naive Approach
        uptilValue = n//2 + 1

        maxComValue = 0

        for i in range(uptilValue):
            maxComValue += math.comb(n-i,(n-(2*i)))
        
        return maxComValue

        #Better Approach
        '''
        one, two = 1,1
        for i in range(n-1):
            temp = one
            one = one+two
            two = temp
        return one
        '''

        #Fibonacci Approach
        '''
        @lru_cache(None)
        def fibonacci(n):
            if n <= 1:
                return n
            else:
                return fibonacci(n-1) + fibonacci(n-2)
        return fibonacci(n+1)
        '''

        #One Line Approach
        '''
        #return int(((1+math.sqrt(5))**n-(1-math.sqrt(5))**n)/(2**n*math.sqrt(5)))
        return 1 if n < 2 else self.climbStairs(n-1) + self.climbStairs(n-2)
        '''


if __name__ == '__main__':
    n = 2
    print(Solution().climbStairs(n))