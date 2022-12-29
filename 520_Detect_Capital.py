class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        #Method - 1
        '''
        return word == word.lower() or word == word.upper() or (word[0] == word[0].upper() and word[1:] == word[1:].lower())
        '''

        #Method - 2
        return word.islower() or word.isupper() or word.istitle()

if __name__ == '__main__':
    s = Solution()
    print(s.detectCapitalUse("USA"))
    print(s.detectCapitalUse("FlaG"))