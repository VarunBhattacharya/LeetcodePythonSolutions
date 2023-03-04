'''
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the 
cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

Example 1:
Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.
'''

class Solution:
    def minCostClimbingStairs(self, cost) -> int:
        #Approach 1: Time Complexity - O(2^N) and Space Complexity - O(N)
        '''
        def helper(cost, i, n, dp):
            if i >= n:
                return 0
            if dp[i] != -1:
                return dp[i]
            dp[i] = cost[i] + min(helper(cost, i+1, n, dp), helper(cost, i+2, n, dp))
            return dp[i]
        
        n = len(cost)
        dp = [-1] * n
        return min(helper(cost, 0, n, dp), helper(cost, 1, n, dp))
        '''

        #Naive Approach - Time Complexity - O(N) and Space Complexity - O(1)
        '''
        cost1 = cost2 = 0
        for i in range(2, len(cost)):
            cost1 = cost[i-1] + cost[i]
            cost2 = cost[i-2] + cost[i]
            cost[i] = min(cost1, cost2)
        return min(cost[-1], cost[-2])
        '''

        #Approach 2: Dynamic Programming(Forward Traversal) - Time Complexity - O(N) and Space Complexity - O(1)
        '''
        for i in range(2, len(cost)):
            cost[i] += min(cost[i-1], cost[i-2])
        return min(cost[-1], cost[-2])
        '''

        #Approach 3: Dynamic Programming(Backward Traversal) - Time Complexity - O(N) and Space Complexity - O(N)
        cost.append(0)
        for i in range(len(cost)-3, -1, -1):
            cost[i] += min(cost[i+1], cost[i+2])
        return min(cost[0], cost[1])

if __name__ == "__main__":
    # cost = [10,15,20]
    cost = [1,100,1,1,1,100,1,1,100,1]
    print(Solution().minCostClimbingStairs(cost))