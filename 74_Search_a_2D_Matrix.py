class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        #Approach 1 - Naive Approach - Time Complexity - O(M*N) and Space Compleity - O(1)
        '''
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if target == matrix[i][j]: return True
        return False
        '''

        #Approach 2 - Binary Search - Time Complexity - O(log(M+N)) and Space Complexity - O(1)
        row = len(matrix)
        col = len(matrix[0])
        x, y = 0, col - 1
        while True:
            if x < row and y >= 0:
                if matrix[x][y] == target:
                    return True
                elif matrix[x][y] < target:
                    x += 1
                else:
                    y -= 1
            else:
                return False

if __name__ == "__main__":
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 3
    print(Solution().searchMatrix(matrix, target))