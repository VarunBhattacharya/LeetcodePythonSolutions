class Solution:
    def countNegatives(self, grid) -> int:
        #Naive Approach: Time Complexity - O(M*N) and Space Complexity - O(1)
        '''
        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] < 0:
                    cnt += 1
        return cnt
        '''

        #One-Liner Approach: Time Complexity - O(M*N) and Space Complexity - O(1)
        '''
        return sum(num < 0 for row in grid for num in row)
        '''

        #Approach 2: Time Complexity - O(M+N) and Space Complexity - O(1)
        '''
        row, col, cnt = len(grid)-1, 0, 0
        while row >= 0 and col < len(grid[0]):
            if grid[row][col] < 0:
                cnt += len(grid[0]) - col
                row -= 1
            else:
                col += 1
        return cnt
        '''

        #Approach 3: Binary Search - Time Complexity - O(M*logN) and Space Complexity - O(1)
        def binSearch(row):
            start, end = 0, len(row)
            while start < end:
                mid = start + (end - start) // 2
                if row[mid] < 0:
                    end = mid
                else:
                    start = mid + 1
            return len(row) - start
        
        cnt = 0
        for row in grid:
            cnt += binSearch(row)
        return cnt


if __name__ == "__main__":
    grid = [[4,3,2,-1],
            [3,2,1,-1],
            [1,1,-1,-2],
            [-1,-1,-2,-3]]
    print(Solution().countNegatives(grid)) #8

    grid = [[3,2],
            [1,0]]
    print(Solution().countNegatives(grid)) #0

    grid = [[1,-1],
            [-1,-1]]
    print(Solution().countNegatives(grid)) #3

    grid = [[-1]]
    print(Solution().countNegatives(grid)) #1