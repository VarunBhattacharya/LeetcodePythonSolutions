class Solution:
    def findRotation(self, mat, target):
        #Approach 1 - Time Complexity - O(N^2) and Space Complexity - O(1)
        '''
        for i in range(4):
            mat.reverse() #reverse matrix
            mat = list(zip(*mat)) #transpose matrix
            mat = [list(j) for j in mat] #tuple to list
            if mat == target:
                return True
        return False
        '''

        #Approach 2 - Time Complexity - O(N^2) and Space Complexity - O(1)
        for i in range(4):
            for j in range(len(mat)):
                for k in range(j,len(mat)):
                    mat[j][k],mat[k][j] = mat[k][j],mat[j][k]
            for j in range(len(mat)):
                mat[j].reverse()
            if mat == target:
                return True
        return False

if __name__ == "__main__":
    s = Solution()
    mat = [[0,1],[1,0]]
    target = [[1,0],[0,1]]
    print(s.findRotation(mat,target))