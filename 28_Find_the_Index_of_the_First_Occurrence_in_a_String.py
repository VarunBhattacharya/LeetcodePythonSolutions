class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        #Naive Approach: List properties - Time Complexity - O(M*N) and Space Complexity - O(1)
        if needle == "":
            return 0
        for i in range(len(haystack)):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1

        #Approach 2: KMP Algorithm - Time Complexity - O(M+N) and Space Complexity - O(N)


if __name__ == "__main__":
    sol = Solution()
    print(sol.strStr("sadbutsad", "sad"))