import itertools

class Solution:
    def letterCombinations(self, digits: str):
        #Approach 1: Product of characters - Time Complexity - O(4^N) and Space Complexity - O(N)
        valMap = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        
        charMap = [valMap[digit] for digit in digits] #mapping the digit characters

        charComb = itertools.product(*charMap) #take product of each chars

        res = []

        for i in charComb:
            if not i:
                continue
            tempStr = ''.join(i)
            res.append(tempStr)

        return res

        #Approach 2: One Liner - Time Complexity - O(4^N) and Space Complexity - O(N)
        '''
        return list(map(''.join, product(*({'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}[dig] for dig in digits)))) if digits else []
        '''

if __name__ == '__main__':
    s = Solution()
    print(s.letterCombinations('23'))