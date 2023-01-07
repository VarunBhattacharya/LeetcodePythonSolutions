class Solution:
    def canCompleteCircuit(self, gas, cost) -> int:
        #Brute Force Solution - Time Complexity - O(N^2) and Space Complexity - O(1)
        '''
        for i in range(len(gas)):
            start = i
            end = i
            tank = gas[i]
            while True:
                tank = tank - cost[end]
                if tank < 0:
                    break
                end = (end + 1) % len(gas)
                tank = tank + gas[end]
                if start == end:
                    return start
        return -1
        '''

        #Better Solution - Greedy Approach - Time Complexity - O(N) and Space Complexity - O(1)
        if sum(gas) < sum(cost):
            return -1
        diff = []
        for i in range(len(gas)):
            diff.append(gas[i] - cost[i])
        tot = 0
        start = 0
        for i in range(len(diff)):
            tot += diff[i]
            if tot < 0:
                start = i + 1
                tot = 0
        return start

if __name__ == '__main__':
    gas = [1,2,3,4,5]
    cost = [3,4,5,1,2]
    print(Solution().canCompleteCircuit(gas, cost))