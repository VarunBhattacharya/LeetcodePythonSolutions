import collections
from math import ceil

class Solution:
    def minimumFuelCost(self, roads, seats: int) -> int:
        #Approach 1: DFS - Time Complexity - O(N) and Space Complexity - O(N)
        adj = collections.defaultdict(list)
        for parent, child in roads:
            adj[parent].append(child)
            adj[child].append(parent)
        
        def dfs(node, parent):
            nonlocal res
            passengers = 0

            for child in adj[node]:
                if child != parent:
                    p = dfs(child, node)
                    passengers += p
                    res += int(ceil(p/seats))
            return passengers + 1
        
        res = 0
        dfs(0,-1)
        return res

if __name__ == '__main__':
    roads = [[0,1],[0,2],[0,3]]
    seats = 5
    print(Solution().minimumFuelCost(roads, seats))