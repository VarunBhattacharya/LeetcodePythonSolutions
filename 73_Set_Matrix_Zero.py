'''
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.
'''


class Solution:
    def setZeroes(self, matrix):
        #Brute Force Method - Time Complexity - O(M*N) and Space Complexity - O(M*N)
        '''
        matrixCopy = matrix
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    for k in range(m):
                        if matrix[k][j] != 0:
                            matrixCopy[k][j] = 'a' #set col values to 'a'
                    for k in range(n):
                        if matrix[i][k] != 0: #set row values to 'a'
                            matrixCopy[i][k] = 'a'
        for i in range(m):
            for j in range(n):
                if matrixCopy[i][j] == 'a': #set 'a' to 0
                    matrix[i][j] = 0
        return matrix
        '''

        #Better Method - Time Complexity - O(M*N) and Space Complexity - O(M+N)
        '''
        m = len(matrix)
        n = len(matrix[0])
        rows = set()
        cols = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        for i in range(m):
            for j in range(n):
                if i in rows or j in cols:
                    matrix[i][j] = 0
        return matrix
        '''
        
        #Best Method - Time Complexity - O(M*N) and Space Complexity - O(1)
        m = len(matrix)
        n = len(matrix[0])
        isCol = False
        for i in range(m):
            if matrix[i][0] == 0:
                isCol = True
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1, m):
            for j in range(1, n):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0
        if matrix[0][0] == 0:
            for j in range(n):
                matrix[0][j] = 0
        if isCol:
            for i in range(m):
                matrix[i][0] = 0
        return matrix


if __name__ == "__main__":
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    print(Solution().setZeroes(matrix))

    matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    print(Solution().setZeroes(matrix))