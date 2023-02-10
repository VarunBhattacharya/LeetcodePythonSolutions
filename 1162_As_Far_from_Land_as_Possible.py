import collections

class Solution:
    def maxDistance(self, grid) -> int:
        #Approach 1: BFS - Time: O(n^2), Space: O(n^2)
        '''
        n = len(grid)
        q = collections.deque()
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append((i, j))
        if len(q) == 0 or len(q) == n * n:
            return -1
        distance = -1
        while q:
            distance += 1
            for _ in range(len(q)):
                i, j = q.popleft()
                for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                    if 0 <= x < n and 0 <= y < n and grid[x][y] == 0:
                        grid[x][y] = 2
                        q.append((x, y))
        return distance
        '''

        #Approach 2: Multisource BFS - Time: O(n^2), Space: O(n^2)
        n = len(grid)
        queue = collections.deque()
        for row in range(n):
            for col in range(n):
                if grid[row][col]:
                    queue.append([row, col])
        res = -1
        directions = [[0,1], [1,0], [-1,0], [0,-1]]

        while queue: #bfs
            row, col = queue.popleft()

            res = grid[row][col]
            for directRow, directCol in directions:
                newR, newC = row + directRow, col + directCol
                if (min(newR, newC) >= 0 and max(newR, newC) < n and grid[newR][newC] == 0): #check for in-bounds
                    queue.append([newR, newC])
                    grid[newR][newC] = grid[row][col] + 1

        return res - 1 if res > 1 else -1


if __name__ == "__main__":
    grid = [[1,0,1],[0,0,0],[1,0,1]]
    print(Solution().maxDistance(grid))