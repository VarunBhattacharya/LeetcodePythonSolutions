class Solution:
    def minDeletionSize(self, strs) -> int:
        N = len(strs)
        M = len(strs[0])
        deleted = 0
        for col in range(M):
            for row in range(N-1):
                if strs[row][col] > strs[row+1][col]:
                    deleted += 1
                    break
        return deleted

if __name__ == '__main__':
    strs = ["cba","daf","ghi"]
    print(Solution().minDeletionSize(strs))