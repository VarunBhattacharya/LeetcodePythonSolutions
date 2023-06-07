class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        #Naive Approach: String Manipulation - Time Complexity: O(max(N,M)) and Space Complexity: O(1)
        '''
        finalString = ""
        
        if len(word1) == 0 and len(word2) == 0:
            return
        if len(word1) == 0:
            return word2
        if len(word2) == 0:
            return word1
        
        pnt1, pnt2 = 0, 0
        while pnt1 < len(word1) and pnt2 < len(word2):
            finalString += word1[pnt1]
            finalString += word2[pnt2]
            pnt1 += 1
            pnt2 += 1
        if pnt1 != len(word1):
            while pnt1 < len(word1):
                finalString += word1[pnt1]
                pnt1 += 1
        if pnt2 != len(word2):
            while pnt2 < len(word2):
                finalString += word2[pnt2]
                pnt2 += 1
        return finalString
        '''

        #Solution 2: zip_longest - Time Complexity: O(max(N,M)) and Space Complexity: O(1)
        from itertools import zip_longest
        return "".join(a+b for a,b in zip_longest(word1, word2, fillvalue = ""))

if __name__ == "__main__":
    word1 = "abc"
    word2 = "pqr"
    print(Solution().mergeAlternately(word1, word2))