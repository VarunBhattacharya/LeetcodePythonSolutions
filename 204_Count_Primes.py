import math

class Solution:
    def countPrimes(self, n: int) -> int:
        #Better Method
        '''
        def checkPrime(num):
            if num <= 1:
                return False
            for i in range(2,1+int(math.sqrt(num))):
                if num%i == 0:
                    return False
            return True

        cntPrime = 0

        for i in range(n):
            if checkPrime(i):
                cntPrime += 1
        return cntPrime
        '''

        #Sieve Method -- Efficient Solution
        


if __name__ == '__main__':
    s = Solution()
    print(s.countPrimes(10))