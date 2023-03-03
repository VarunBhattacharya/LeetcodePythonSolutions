import functools

class Solution:
    def fib(self, n: int) -> int:
        #Approach 1: Recursion - Time Complexity - [O(2^n), O(N)] and Space Complexity - O(N)
        '''
        if n <= 1:
            return n
        return self.fib(n-1) + self.fib(n-2)
        '''

        #Approach 2: Iterative - Time Complexity - O(N) and Space Complexity - O(1)
        '''
        if n <= 1:
            return n
        a, b = 0, 1
        for i in range(2, n+1):
            a, b = b, a+b
        return b
        '''

        #Approach 3: Memoization (without inbuilt function) - Faster Method
        '''
        def fibonacci(n, computed = {0:0, 1:1}): #reducing multiple time calculations
            if n not in computed:
                computed[n] = fibonacci(n-1, computed) + fibonacci(n-2, computed)
            return computed[n]
        return fibonacci(n, computed = {0:0, 1:1})
        '''

        #Approach 4: Memoization (using inbuilt function) - Faster Method
        @functools.lru_cache(None) #decorators
        def fibonacci(n):
            if n <= 1:
                return n
            return fibonacci(n-1) + fibonacci(n-2)
        return fibonacci(n)


if __name__ == '__main__':
    n = 4
    obj = Solution()
    print(obj.fib(n))