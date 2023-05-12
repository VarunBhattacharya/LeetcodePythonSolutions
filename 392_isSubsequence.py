class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        #Approach 1: Two Pointer - Time Complexity - O(N+M) and Space Complexity - O(1)
        pnt1, pnt2 = 0, 0
        while pnt1 < len(s) and pnt2 < len(t):
            if s[pnt1] == t[pnt2]:
                pnt1 += 1
            pnt2 += 1
        return True if pnt1 == len(s) else False

        #Approach 2: Time Complexity - O(N^2) and Space Complexity - O(1) - Wrong Solution(15/18 testcase passed)
        '''
        resStr = ""
        for i in t:
            if i in s and i not in resStr:
                resStr += i
        return True if len(resStr) == len(s) else False
        '''

if __name__ == '__main__':
    s = "abc"
    t = "ahbgdc"
    sol = Solution()
    print(sol.isSubsequence(s,t))