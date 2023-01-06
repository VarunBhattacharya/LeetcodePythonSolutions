class Solution:
    def maxIceCream(self, costs, coins: int) -> int:
        #Naive Approach - Time Complexity - O(NlogN) and Space Complexity - O(1)
        '''
        costs.sort()
        iceBars = 0
        if costs[0] > coins: return 0
        for i in costs:
            if coins >= i:
                coins -= i
                iceBars += 1
        return iceBars
        '''

        #Better Approach - Bucket Sort - Time Complexity - O(N) and Space Complexity - O(1)
        '''
        bucket = [0]*(max(costs)+1)
        for price in costs:
            bucket[price] += 1
        iceBars = 0
        for price, count in enumerate(bucket):
            if price > coins:
                break
            if count > 0:
                iceBars += min(count, coins//price)
                coins -= min(coins, price*count)
        return iceBars
        '''

        #Better Approach - One Liner - Time Complexity - O(N) and Space Complexity - O(1)
        return sum(1 for cost in sorted(costs) if (coins:= coins-cost) >= 0)

if __name__ == '__main__':
    s = Solution()
    print(s.maxIceCream([1,3,2,4,1], 7))
    print(s.maxIceCream([10,6,8,7,7,8], 5))
    print(s.maxIceCream([1,6,3,1,2,5], 20))