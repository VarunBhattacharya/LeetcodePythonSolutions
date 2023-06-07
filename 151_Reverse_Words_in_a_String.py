class Solution:
    def reverseWords(self, s: str) -> str:
        #Naive Approach: Time Complexity: O(N) and Space Comeplexity: O(1)
        return " ".join(s.strip().split()[::-1])


if __name__ == "__main__":
    s = Solution()
    print(s.reverseWords("  hello world!  "))