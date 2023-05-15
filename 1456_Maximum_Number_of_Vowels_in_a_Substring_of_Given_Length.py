'''
Given a string s and an integer k, return the maximum number of vowel letters in any 
substring of s with length k.
Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

Example1:
Input: s = "abciiidef", k = 3
Output: 3

Example2:
Input: s = "aeiou", k = 2
Output: 2

Example3:
Input: s = "leetcode", k = 3
Output: 2

Example4:
Input: s = "tryhard", k = 4
Output: 1
'''

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        #Approach 1: Two Pointer Sliding Window - Time Complexity - O(N), Space Complexity: O(1) - Wrong Answer
        '''
        vowels = ['a', 'e', 'i', 'o', 'u']
        s.lower()
        pnt1, pnt2 = 0, k
        maxCnt = 0

        if len(s) == 0 or len(s) < k:
            return 0

        while pnt1 < pnt2 and pnt2 < len(s):
            tempCnt = 0
            while pnt1 < pnt2:
                if s[pnt1] in vowels:
                    tempCnt += 1
                pnt1 += 1
            maxCnt = max(maxCnt, tempCnt)
            pnt1 = pnt2
            pnt2 += k
        return maxCnt
        '''

        #Approach 2: Sliding Window - Time Complexity: O(N), Space Complexity: O(1)
        vowels = ['a', 'e', 'i', 'o', 'u']

        if len(s) == 0 or len(s) < k:
            return 0
        
        pnt1, pnt2 = 0, 0
        maxCnt = 0
        tempCnt = 0

        while pnt2 < len(s):
            if s[pnt2] in vowels:
                tempCnt += 1
            if pnt2 - pnt1 + 1 == k:
                maxCnt = max(maxCnt, tempCnt)
                if s[pnt1] in vowels:
                    tempCnt -= 1
                pnt1 += 1
            pnt2 += 1
        return maxCnt


if __name__ == "__main__":
    s = "tryhard"
    k = 4
    print(Solution().maxVowels(s, k))