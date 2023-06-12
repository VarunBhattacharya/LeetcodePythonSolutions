class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        #Approach 1: Using dictionary and set - Time Complexity: O(N), Space Complexity: O(N)
        '''
        return len(set(zip(pattern, s.split()))) == len(set(pattern)) == len(set(s.split())) and len(pattern) == len(s.split())
        '''

        #Approach 2: Using HashMap - Time Complexity: O(N), Space Complexity: O(N)
        words = s.split(" ")
        if len(pattern) != len(words):
            return False
        charToWord, wordToChar = {}, {}
        for p, w in zip(pattern, words):
            if p in charToWord and charToWord[p] != w:
                return False
            if w in wordToChar and wordToChar[w] != p:
                return False
            charToWord[p] = w
            wordToChar[w] = p
        return True

if __name__ == '__main__':
    pattern = "abba"
    s = "dog cat cat dog"
    print(Solution().wordPattern(pattern, s))