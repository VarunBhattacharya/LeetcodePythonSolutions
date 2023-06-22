class Solution:
    def maximumWealth(self, accounts) -> int:
        #Approach 1: Time Complexity - O(N) and Space Complexity - O(1)
        maxAmt = 0
        for i in accounts:
            maxAmt = max(maxAmt, sum(i))
        return maxAmt

        #Approach 2: Time Complexity - O(N) and Space Complexity - O(1)
        '''
        return max([sum(i) for i in accounts])
        '''

if __name__ == "__main__":
    s = Solution()
    accounts = [[1,2,3],[3,2,1]]
    print(s.maximumWealth(accounts))