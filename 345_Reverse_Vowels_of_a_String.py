class Solution:
    def reverseVowels(self, s: str) -> str:
        #Naive Approach: Time Complexity - O(N) and Space Complexity - O(N)
        '''
        if not s:
            return
        
        vowels = 'aeiouAEIOU'
        vowInString = ""
        for i in range(len(s)):
            if s[i] in vowels:
                vowInString += s[i]
        
        vowInStringList = list(vowInString[::-1])

        sList = list(s)
        for i in range(len(sList)):
            if sList[i] in vowels:
                sList[i] = vowInStringList[0]
                vowInStringList.pop(0)
        
        return "".join(sList)
        '''


        #Approach 2: Two Pointer Approach - Time Complexity - O(N) and Space Complexity - O(1)
        if not s:
            return
        vowels = 'aeiouAEIOU'
        s = list(s)
        pnt1, pnt2 = 0, len(s)-1
        while pnt1 < pnt2:
            if s[pnt1] not in vowels and s[pnt2] not in vowels:
                pnt1 += 1
                pnt2 -= 1
            elif s[pnt1] not in vowels:
                pnt1 += 1
            elif s[pnt2] not in vowels:
                pnt2 -= 1
            else:
                s[pnt1], s[pnt2] = s[pnt2], s[pnt1]
                pnt1 += 1
                pnt2 -= 1
        return "".join(s)

if __name__ == "__main__":
    s = Solution()
    print(s.reverseVowels("leetcode"))