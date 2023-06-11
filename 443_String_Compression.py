class Solution:
    def compress(self, chars) -> int:
        #Approach 1: Time Complexity - O(N^2) and Space Complexity - O(N)
        '''
        if not chars:
            return 0
        res = []
        pnt1 = 0
        while pnt1 < len(chars):
            pnt2 = pnt1 + 1
            while pnt2 < len(chars) and chars[pnt1] == chars[pnt2]:
                pnt2 += 1
            res.append(chars[pnt1])
            if pnt2 - pnt1 > 1:
                res += list(str(pnt2 - pnt1))
            pnt1 = pnt2
        chars[:] = res
        return len(chars)
        '''

        #Approach 2: Two Pointer - Time Complexity - O(N) and Space Complexity - O(1)
        '''
        if not chars:
            return 0
        initialChar = chars[0]
        initialLen = len(chars)
        skips = 0
        chars.append(" ")

        for _ in range(initialLen + 1):
            popChar = chars.pop(0)
            if popChar == initialChar:
                skips += 1
            else:
                if skips == 1:
                    chars.append(initialChar)
                elif skips > 1:
                    chars.append(initialChar)
                    chars += list(str(skips))
                initialChar = popChar
                skips = 1
        return len(chars)
        '''

        #Approach 3: Two Pointer - Time Complexity - O(N) and Space Complexity - O(1)
        if len(chars) < 2:
            return len(chars)
        pnt1, pnt2 = 0, 0
        while pnt1 < len(chars):
            tempCnt = 1
            while pnt1 < len(chars) - 1 and chars[pnt1] == chars[pnt1+1]:
                tempCnt += 1
                pnt1 += 1
            
            chars[pnt2] = chars[pnt1]
            pnt2 += 1
            if tempCnt > 1:
                for num in str(tempCnt):
                    chars[pnt2] = str(num)
                    pnt2 += 1

            pnt1 += 1
        return pnt2
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.compress(["a","a","b","b","c","c","c"]))
    print(sol.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))