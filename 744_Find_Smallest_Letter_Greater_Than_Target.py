class Solution:
    def nextGreatestLetter(self, letters, target: str) -> str:
        #Naive Approach: Time Complexity - O(N) and Space Complexity - O(1) -> Wrong Solution
        '''
        minChar = ord('z')
        for i in letters:
            if i != target:
                minChar = min(minChar, (ord(i) - ord(target)))
        return chr(ord(target) + minChar)
        '''

        #Better Approach: Binary Search - Time Complexity - O(logN) and Space Complexity - O(1)
        start, end = 0, len(letters)
        while start < end:
            mid = (start + end) // 2
            if target < letters[mid]:
                end = mid
            else:
                start = mid + 1
        return letters[end] if end < len(letters) else letters[0]
    
if __name__ == '__main__':
    sol = Solution()
    print(sol.nextGreatestLetter(["c", "f", "j"], "a"))