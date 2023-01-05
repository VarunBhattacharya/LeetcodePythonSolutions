class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Naive Approach - Time Complexity - O(N) and Space Complexity - O(N)
        '''
        if len(s) != len(t):
            return False
        sArr = [0]*26
        for i in s:
            indPos = (ord(i) - ord('a'))
            sArr[indPos] += 1
        for i in t:
            indPos = (ord(i) - ord('a'))
            sArr[indPos] -= 1
        cntCheck = 0
        for i in sArr:
            if i == 0:
                cntCheck += 1
        if cntCheck == 26:
            return True
        else:
            return False
        '''

        #Better Approach - Using HashMap - Time Complexity - O(N) and Space Complexity - O(N)
        '''
        if len(s) != len(t):
            return False
        sMap, tMap = {}, {}
        for i in s:
            if i in sMap:
                sMap[i] += 1
            else:
                sMap[i] = 1
        for i in t:
            if i in tMap:
                tMap[i] += 1
            else:
                tMap[i] = 1
        return sMap == tMap
        '''

        #Better Approach - Using Sorting - Time Complexity - O(NlogN) and Space Complexity - O(N)
        return sorted(s) == sorted(t)

if __name__ == '__main__':
    s = Solution()
    print(s.isAnagram("anagram", "nagaram"))