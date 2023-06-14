from collections import defaultdict

class Solution:
    def equalPairs(self, grid) -> int:
        #Naive Approach: Time Complexity - O(N^2) and Space Complexity - O(1)
        '''
        cnt = 0
        n = len(grid)

        for ri in range(n):
            for cj in range(n):
                if grid[ri] == [row[cj] for row in grid]:
                    cnt += 1

        return cnt
        '''

        #Approach 2: Time Complexity - O(N) and Space Complexity - O(N) - Test Case Failed
        '''
        hashMap = {}
        for i in range(len(grid)):
            hashMap[i] = grid[i]
        
        transposeMat = list(zip(*grid))
        transposeMat = [list(i) for i in transposeMat]

        cnt = 0
        for i in range(len(transposeMat)):
            if transposeMat[i] == hashMap[i]:
                cnt += 1
        return cnt
        '''

        #Approach 3: Time Complexity - O(N) and Space Complexity - O(1)
        d = defaultdict(int)
        ans = 0

        for row in grid:
            d[tuple(row)] += 1

        for col in zip(*grid):
            ans += d[tuple(col)]

        return ans

if __name__ == '__main__':
    grid = [[3,2,1],[1,7,6],[2,7,7]]
    s = Solution()
    print(s.equalPairs(grid))