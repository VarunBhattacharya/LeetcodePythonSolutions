class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """

        #Approach 1: Time Complexity - O(N^2) and Space Complexity - O(1)
        '''
        matrix.reverse() #reverse the matrix
        matrix[:] = list(zip(*matrix)) #transpose of the matrix
        return matrix
        '''

        #Approach 2: Time Complexity - O(N^2) and Space Complexity - O(1)
        #reverse the matrix
        for i in range(len(matrix)):
            for j in range(i,len(matrix)):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        
        #transpose of the matrix
        for i in range(len(matrix)):
            matrix[i].reverse()
        return matrix

if __name__ == "__main__":
    s = Solution()
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print(s.rotate(matrix))