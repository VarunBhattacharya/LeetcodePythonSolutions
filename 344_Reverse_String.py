class Solution:
    def reverseString(self,s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s = s[::-1]
        #s = s.reverse()
        return s

if __name__ == "__main__":
    s = Solution()
    print(s.reverseString(["h","e","l","l","o"]))