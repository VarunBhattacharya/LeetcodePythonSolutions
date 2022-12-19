class Solution:
    def __init__(self,matrix):
        self.matrix = matrix

    def spiralOrder(self):
        res = []
        left, right = 0, len(self.matrix[0])
        top, bottom = 0, len(self.matrix)

        while left < right and top < bottom:
            #element in the top row
            for i in range(left, right):
                res.append(self.matrix[top][i])
            top += 1

            #element in the right col
            for i in range(top, bottom):
                res.append(self.matrix[i][right - 1])
            right -= 1

            if not (left < right and top < bottom):
                break
            
            #element in the bottom row
            for i in range(right-1, left-1, -1):
                res.append(self.matrix[bottom - 1][i])
            bottom -= 1

            #element in the left col
            for i in range(bottom-1, top-1, -1):
                res.append(self.matrix[i][left])
            left += 1
            
        return res


if __name__ == "__main__":
    matrix = [[1,2,3],[4,5,6],[7,8,9]]  #res = [1,2,3,6,9,8,7,4,5]
    # matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]  #res = [1,2,3,4,8,12,11,10,9,5,6,7]
    s = Solution(matrix)
    print(s.spiralOrder())