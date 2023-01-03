class Solution:
    def isToeplitzMatrix(self, matrix) -> bool:
        #Naive Approach - Time Complexity - O(M*N) and Space Complexity - O(1)
        '''
        for row in range(len(matrix)-1):
            for col in range(len(matrix[0])-1):
                if matrix[row][col] != matrix[row+1][col+1]:
                    return False
        return True
        '''

        #Another Approach - Time Complexity - O(M*N) and Space Complexity - O(1)
        def checkDiagVals(row, col):
            val = matrix[row][col]
            while row < len(matrix) and col < len(matrix[0]):
                if matrix[row][col] != val:
                    return False
                row += 1
                col += 1
            return True
        
        for col in range(len(matrix[0])):
            if not checkDiagVals(0,col): #if col diag vals not same
                return False
            for row in range(1, len(matrix)):
                if not checkDiagVals(row,0):
                    return False
        return True

if __name__ == '__main__':
    s = Solution()
    print(s.isToeplitzMatrix([[1,2,3,4],[5,1,2,3],[9,5,1,2]]))