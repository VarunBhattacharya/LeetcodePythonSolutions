class Solution:
    def getRow(self, rowIndex: int):
        #Initial Approach
        res = [[1]]
        for i in range(rowIndex + 1):
            temp = [0] + res[-1] + [0]
            rows = []
            for j in range(len(res) + 1):
                rows.append(temp[j] + temp[j+1])
            res.append(rows)
        return res[-2]

if __name__ == "__main__":
    rowIndex = 3
    print(Solution().getRow(rowIndex))