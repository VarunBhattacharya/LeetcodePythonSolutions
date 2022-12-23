from primePy import primes
class Solution:
    def isUgly(self, n: int) -> bool:
        # Method 1 - Using Library, Time Complexity: O(N) and Space Complexity: O(N)
        givenPrimeArr = [2,3,5]
        if n == 0: return False
        if n == 1: return True
        primeArrN = primes.factors(n)
        for i in primeArrN:
            if i not in givenPrimeArr:
                return False
        return True

        #Better Method - Time Complexity: O(N) and Space Complexity: O(1)
        '''
        if n == 0: return False
        if n == 1: return True
        while n % 2 == 0:
            n = n/2
        while n%3 == 0:
            n = n/3
        while n%5 == 0:
            n = n/5
        return n == 1
        '''

if __name__ == "__main__":
    n = 14
    print(Solution().isUgly(n))