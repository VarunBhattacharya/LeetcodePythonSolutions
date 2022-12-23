class Solution:
    def getNoZeroIntegers(self, n: int):
        #Naive Approach - Time Complexity - O(N) and Space Complexity - O(1)
        '''
        for i in range(1,n):
            if '0' not in str(i) and '0' not in str(n-i):
                return [i, n-i]
        return []
        '''

        #Better Approach - Time Complexity - O(lonN) and Space Complexity - O(N)
        def checkZero(n):
            while n > 0:
                if n%10 == 0:
                    return False
                n = n//10
            return True
        for i in range(1,n):
            if checkZero(i) and checkZero(n-i):
                return [i, n-i]
        return []

        #Best Approach - Divide and Conquer Technique, Time Complexity - O(logN) and Space Complexity - O(1)
        #works only for n >= 10
        '''
        def getNoZeroIntegers(n: int):
            # base case: if n is less than 10, return an empty list
            if n < 10:
                return []
            
            # if n is 10 or greater, divide n by 10 and check the remainder
            remainder = n % 10
            if remainder > 1:
                # if the remainder is 2 or greater, return [1, n-1]
                return [1, n-1]
            else:
                # if the remainder is 1, divide n-1 by 10 and check the remainder
                sub_remainder = (n-1) % 10
                if sub_remainder > 1:
                    # if the sub_remainder is 2 or greater, return [2, n-2]
                    return [2, n-2]
                else:
                    # if the sub_remainder is 1 or 0, recursively call the function with n-3
                    return getNoZeroIntegers(n-3)
        return getNoZeroIntegers(n)
        '''


if __name__ == '__main__':
    n = 2
    print(Solution().getNoZeroIntegers(n))