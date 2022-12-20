class Solution:
    def maxProfit(self, prices) -> int:
        #Brute Force
        '''
        maxVal = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                profit = prices[j] - prices[i]
                maxVal = max(profit, maxVal)
        return maxVal
        '''
        
        #Better Solution
        if not prices: return 0
        minVal, maxVal = prices[0], 0
        for i in range(len(prices)):
            profit = prices[i] - minVal
            maxVal = max(profit, maxVal)
            minVal = min(minVal, prices[i])
        return maxVal

if __name__ == '__main__':
    prices = [7,1,5,3,6,4]
    print(Solution().maxProfit(prices))