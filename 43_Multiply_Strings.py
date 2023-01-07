class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        #Naive Method - Time Complexity: O(N^2) and Space Complexity: O(1)
        '''
        num1 = num1[::-1]
        num2 = num2[::-1]
        res = [0] * (len(num1) + len(num2))
        for i in range(len(num1)):
            for j in range(len(num2)):
                res[i+j] += int(num1[i]) * int(num2[j])
                res[i+j+1] += res[i+j] // 10
                res[i+j] %= 10
        while len(res) > 1 and res[-1] == 0:
            res.pop()
        return ''.join(map(str, res[::-1]))
        '''

        #Better Method - Time Complexity: O(N) and Space Complexity: O(1)
        def getInt(num):
            intNum = 0
            cnter = pow(10, len(num)-1)
            for i in num:
                tempVal = ord(i) - ord('0')
                intNum += tempVal * cnter
                cnter = cnter // 10
            return intNum
        
        intNum1 = getInt(num1)
        intNum2 = getInt(num2)

        return str(intNum1 * intNum2)

if __name__ == '__main__':
    sol = Solution()
    num1 = "123"
    num2 = "456"
    print(sol.multiply(num1, num2))