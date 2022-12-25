class Solution:
    def getSum(self, a: int, b: int) -> int:
        #Naive Solution --> Wrong Answer
        '''
        binA = bin(a).lstrip('0b')
        binB = bin(b).lstrip('0b')
        def appendBits(binVal, lenVal):
            binVal = binVal[::-1]
            for i in range(len(binVal), lenVal):
                binVal += '0'
            return binVal[::-1]

        if len(binA) < len(binB): appendBits(binA, len(binB))
        if len(binA) > len(binB): appendBits(binB, len(binB))

        carryOver = '0'
        res = ''
        binA = binA[::-1]
        binB = binB[::-1]
        for i in range(len(binA)):
            tempAddVal = binA[i] or binB[i]
            if carryOver == '1':
                tempAddVal = carryOver or tempAddVal
            if binA[i] == '1' and binB[i] == '1':
                tempAddVal = '0'
                carryOver = '1'
            res += tempAddVal
        return int(res,2)
        '''

        #Bit Manipulation Solution - Correct logic but TLE for negative numbers
        '''
        while b != 0:
            temp = (a&b) << 1
            a = a ^ b
            b = temp
        return a
        '''

        #Bit Manipulation
        mask = 0xffffffff #32-bit mask value

        while (b & mask) > 0:
            carry = (a & b) << 1
            a = (a ^ b) 
            b = carry
        return (a & mask) if b > 0 else a

if __name__ == '__main__':
    sol = Solution()
    print(sol.getSum(-1,1))