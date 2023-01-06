class Solution:
    def isPalindrome(self, s: str) -> bool:
        #Approach - 1
        '''
        newStr = ""
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        
        if newStr == newStr[::-1]: return True
        else: return False
        '''
        #Approach - 2
        def alNum(c):
            return (ord('A') <= ord(c) <= ord('Z') or 
                    ord('a') <= ord(c) <= ord('z') or
                    ord('0') <= ord(c) <= ord('9'))

        l, r = 0, len(s)-1
        while l < r:
            while l < r and not alNum(s[l]):
                l += 1
            while r > l and not alNum(s[r]):
                r -= 1
            
            if s[l].lower() != s[r].lower(): return False
            
            l,r = l+1, r-1
            
        return True

if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome("A man, a plan, a canal: Panama"))