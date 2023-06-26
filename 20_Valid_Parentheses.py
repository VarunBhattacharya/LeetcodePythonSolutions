class Solution:
    def isValid(self, s: str) -> bool:
        #Approach 1: Time Complexity - O(N*K) and Space Complexity - O(N)
        if not s:
            return
        
        stack = []
        hashMap = {']':'[', ')':'(', '}':'{'}

        for i in s:
            if i in hashMap:
                if stack and stack[-1] == hashMap[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        
        return True if not stack else False


if __name__ == "__main__":
    print(Solution().isValid("()[]{}")) #True
    print(Solution().isValid("([)]")) #False
    print(Solution().isValid("{[]}")) #True
    print(Solution().isValid("(([]){})")) #True
    print(Solution().isValid("(([]){})(")) #False
    print(Solution().isValid("((")) #False
    print(Solution().isValid("))")) #False