class Solution:
    def diagonalSum(self, mat) -> int:
        matSum = 0
        for i in range(len(mat)):
            matSum += mat[i][i]
            matSum += mat[i][len(mat) - i - 1]
        if len(mat) % 2 == 1:
            matSum -= mat[len(mat)//2][len(mat)//2]
        return matSum
    
if __name__ == '__main__':
    mat = [[1,2,3], [4,5,6], [7,8,9]]
    print(Solution().diagonalSum(mat))