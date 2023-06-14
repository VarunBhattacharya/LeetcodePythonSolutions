from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        #Approach 1: Time Complexity - O(N) and Space Complexity - O(N)
        '''
        word1Map = Counter(word1)
        word2Map = Counter(word2)

        word1Map = sorted(word1Map.values())
        word2Map = sorted(word2Map.values())

        word1Set = set(word1)
        word2Set = set(word2)

        return (word1Map == word2Map and word1Set == word2Set)
        '''

        #Approach 2: Time Complexity - O(N) and Space Complexity - O(N)
        '''
        return  sorted(Counter(word1).values()) == sorted(Counter(word2).values()) and set(word1) == set(word2)
        '''
    
        #Approach 3: Time Complexity - O(N) and Space Complexity - O(1) - Test Case Fail - "uau", "ssx" (131/153 passed)
        if len(word1) != len(word2):
            return False

        word1Map = [0] * 26
        word2Map = [0] * 26

        for i in range(len(word1)):
            word1Map[ord(word1[i]) - ord('a')] += 1
            word2Map[ord(word2[i]) - ord('a')] += 1

        word1Map = sorted(word1Map)
        word2Map = sorted(word2Map)

        return (word1Map == word2Map)
    

if __name__ == "__main__":
    s = Solution()
    print(s.closeStrings("abc", "bca"))
    print(s.closeStrings("a", "aa"))
    print(s.closeStrings("cabbba", "abbccc"))
    print(s.closeStrings("cabbba", "aabbss"))
    print(s.closeStrings("uau", "ssx")) #output should be false but it is true (approach 3)