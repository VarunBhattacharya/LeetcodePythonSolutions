class Solution:
    def integerBreak(self, n: int) -> int:
        #Naive Method
        '''
        def dfs(num):
            if num == 1:
                return 1
            res = 0 if num == n else num #for not breaking the decision tree again
            for i in range(1,num): #for getting the left part of the sum
                tempVal = dfs(i) * dfs(num-i) #such that multiplication is done in limit
                res = max(res, tempVal) #consider the maximum multiplied limit
            return res
        return dfs(n)
        '''

        #Better Method - Dynamic Programming - Time Complexity - O(N^2)
        dp = {1:1} #dynamic programming - caching method
        def dfs(num):
            if num in dp:
                return dp[num]
            dp[num] = 0 if num == n else num #for not breaking the decision tree again
            for i in range(1,num): #for getting the left part of the sum
                tempVal = dfs(i) * dfs(num-i) #such that multiplication is done in limit
                dp[num] = max(dp[num], tempVal) #consider the maximum multiplied limit
            return dp[num]
        return dfs(n)

if __name__ == '__main__':
    s = Solution()
    print(s.integerBreak(10))
    