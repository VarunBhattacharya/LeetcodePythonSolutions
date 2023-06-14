class Solution:
    def removeStars(self, s: str) -> str:
        #Approach 1: Time Complexity - O(N) and Space Complexity - O(N)
        s = list(s)
        stack = []

        for i in range(len(s)):
            if s[i] == '*':
                if stack:
                    stack.pop()
            else:
                stack.append(s[i])
        
        return "".join(stack)



if __name__ == "__main__":
    s = 'leet**cod*e'
    print(Solution().removeStars(s))