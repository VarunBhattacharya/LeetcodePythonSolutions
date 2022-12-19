class Solution:
    def exist(self, board, word) -> bool:
        #BackTracking
        #Time Complexity = O(row * col * 4^(len(word)))

        ROWS, COLS = len(board), len(board[0])
        redundantPath = set()

        def dfs(row, col, charPos):
            if (charPos == len(word)):
                return True
            
            if (row < 0 or col < 0 or
                row >= ROWS or col >= COLS or
                word[charPos] != board[row][col] or
                (row, col) in redundantPath):
                return False
            
            redundantPath.add((row,col)) #visited (row,col) path

            res = (dfs(row+1, col, charPos+1) or
                    dfs(row-1, col, charPos+1) or
                    dfs(row, col+1, charPos+1) or
                    dfs(row, col-1, charPos+1))
            redundantPath.remove((row, col)) #removing the path after execution
            return res
        
        for i in range(ROWS):
            for j in range(COLS):
                if (dfs(i,j,0)):
                    return True
        return False

if __name__ == "__main__":
    s = Solution()
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCCED"
    print(s.exist(board, word))