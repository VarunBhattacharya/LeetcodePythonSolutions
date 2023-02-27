# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid):
        #Approach 1: DFS solution - Time Complexity - O(N^2logN) and Space Complexity - O(N)
        def dfs(n,r,c):
            allSame = True
            for i in range(n):
                for j in range(n):
                    if grid[r][c] != grid[r+i][c+j]:
                        allSame = False
                        break
            if allSame:
                return Node(grid[r][c], True)

            n = n//2
            topleft = dfs(n,r,c)
            topright = dfs(n,r,c+n)
            bottomleft = dfs(n,r+n,c)
            bottomright = dfs(n,r+n,c+n)
            return Node(0, False, topleft, topright, bottomleft, bottomright)

        return dfs(len(grid),0,0)

if __name__ == '__main__':
    s = Solution()
    grid = [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]
    print(s.construct(grid))