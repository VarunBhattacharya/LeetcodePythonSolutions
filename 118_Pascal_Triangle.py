class Solution:
    def generate(self, numRows: int):
        #For numRows till 5
        '''
        res = []
        for i in range(numRows):
            tempNum = pow(11,i)
            tempList = [int(x) for x in str(tempNum)]
            res.append(tempList)
        return res
        '''

        #Generic Method
        res = [[1]]
        for i in range(numRows - 1):
            temp = [0] + res[-1] + [0]
            rows = []
            for j in range(len(res) + 1):
                rows.append(temp[j] + temp[j+1])
            res.append(rows)
        return res

if __name__ == "__main__":
    numRows = 5
    print(Solution().generate(numRows))