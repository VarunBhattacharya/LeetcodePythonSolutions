class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # Method 1 - Naive Approach, Time Complexity: O(N*M) and Space Complexity: O(N), TLE in LeetCode
        '''
        def checkUglyNumber(n):
            if n == 0: return False
            while n%2 == 0: n /= 2
            while n%3 == 0: n /= 3
            while n%5 == 0: n /= 5
            return n == 1
        res = []
        startNum = 0
        while n > 0:
            if checkUglyNumber(startNum):
                res.append(startNum)
                startNum += 1
                n -= 1
            else:
                startNum += 1
        return res[-1]
        '''

        #Method 2 - Using Dynamic Programming, Time Complexity: O(N) and Space Complexity: O(N)
        res = [1]
        i2 = i3 = i5 = 0
        while n > 1:
            next2, next3, next5 = res[i2]*2, res[i3]*3, res[i5]*5
            nextUgly = min(next2, next3, next5)
            if nextUgly == next2: i2 += 1
            if nextUgly == next3: i3 += 1
            if nextUgly == next5: i5 += 1
            res.append(nextUgly)
            n -= 1
        return res[-1]

if __name__ == "__main__":
    n = 10
    print(Solution().nthUglyNumber(n))